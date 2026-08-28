import math
import csv
import json
import turtle

# --- ألوان للـ Terminal (ANSI Escape Codes) ---
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    banner = f"""{Colors.OKBLUE}{Colors.BOLD}
  ___                           ___       
 / __|_  _ _ ___ _____ _  _    | _ \_  _  
 \__ \ || | '_ \ \ / -_) || |   |  _/ || | 
 |___/\_,_|_| \_\_\___|\_, |   |_|  \_, | 
                       |__/         |__/  
        -- Geomatics & Traverse Processing Engine v1.2 --
    {Colors.ENDC}"""
    print(banner)

# --- 1. فحص البيانات وقراءتها من CSV ---
def validate_and_load_data(filename="data.csv"):
    """قراءة وفحص بيانات الترافرس من ملف CSV لمنع الأخطاء الميدانية"""
    distances, azimuths = [], []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row_idx, row in enumerate(reader, start=2):
            dist = float(row["Distance"])
            az = float(row["Azimuth"])

            if dist <= 0:
                raise ValueError(f"خطأ في السطر {row_idx}: المسافة يجب أن تكون أكبر من الصفر.")
            if not (0 <= az <= 360):
                raise ValueError(f"خطأ في السطر {row_idx}: الانحراف يجب أن يكون بين 0 و 360 درجة.")

            distances.append(dist)
            azimuths.append(az)

    return distances, azimuths

# --- 2. إنشاء تقرير HTML تفاعلي متكامل مع الجداول ---
def generate_html_dashboard(coords, w_e, w_n, err, acc, area_m2, area_ha, filename="traverse_dashboard.html"):
    """توليد لوحة تقرير تفاعلية بصيغة HTML تحوي الخريطة وجداول الإحداثيات والنتائج"""
    svg_points = ""
    e_vals = [pt[0] for pt in coords]
    n_vals = [pt[1] for pt in coords]
    min_e, max_e = min(e_vals), max(e_vals)
    min_n, max_n = min(n_vals), max(n_vals)

    span_e = max_e - min_e if max_e != min_e else 1.0
    span_n = max_n - min_n if max_n != min_n else 1.0

    svg_pts_list = []
    coord_rows = ""

    for idx, (e, n) in enumerate(coords[:-1]):
        # إعداد نقاط الرسم
        x = 50 + ((e - min_e) / span_e) * 400
        y = 350 - ((n - min_n) / span_n) * 300
        svg_pts_list.append(f"{x},{y}")
        svg_points += (
            f'<circle cx="{x}" cy="{y}" r="5" fill="#e74c3c" />'
            f'<text x="{x+8}" y="{y-8}" font-size="12" fill="#2c3e50">P{idx}</text>'
        )
        # إعداد صفوف الجدول
        coord_rows += f"<tr><td><b>P{idx}</b></td><td>{e:.3f}</td><td>{n:.3f}</td></tr>\n"

    # ربط أول نقطة بالنهاية لإغلاق الرسم البياني
    if coords:
        e0, n0 = coords[0]
        x0 = 50 + ((e0 - min_e) / span_e) * 400
        y0 = 350 - ((n0 - min_n) / span_n) * 300
        svg_pts_list.append(f"{x0},{y0}")

    polygon_points = " ".join(svg_pts_list)

    html_content = f"""<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>SurveyPy - Interactive Dashboard</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 25px; background-color: #f4f6f9; color: #333; }}
        .container {{ max-width: 950px; margin: auto; background: #fff; padding: 25px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-bottom: 20px; }}
        .metrics {{ display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 25px; }}
        .metric-box {{ background: #ebf5fb; padding: 15px; border-radius: 8px; flex: 1; min-width: 180px; border-left: 4px solid #3498db; }}
        .metric-title {{ font-size: 0.85em; color: #7f8c8d; font-weight: bold; }}
        .metric-val {{ font-size: 1.3em; font-weight: bold; color: #2c3e50; margin-top: 5px; }}
        .svg-card {{ text-align: center; background: #fafafa; border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; margin-bottom: 25px; }}
        .grid {{ display: flex; flex-wrap: wrap; gap: 20px; }}
        .card {{ flex: 1; min-width: 300px; background: #fff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; }}
        h2 {{ color: #2980b9; font-size: 1.1rem; margin-top: 0; border-bottom: 1px solid #eee; padding-bottom: 8px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: center; }}
        th {{ background-color: #3498db; color: white; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📐 SurveyPy - التقرير التفاعلي للحسابات المساحية</h1>
        
        <div class="metrics">
            <div class="metric-box"><div class="metric-title">خطأ الإغلاق الكلي (W)</div><div class="metric-val">{err:.4f} m</div></div>
            <div class="metric-box"><div class="metric-title">نسبة الدقة (Precision)</div><div class="metric-val">1 : {int(acc)}</div></div>
            <div class="metric-box"><div class="metric-title">المساحة (متر مربع)</div><div class="metric-val">{area_m2:.2f} m²</div></div>
            <div class="metric-box"><div class="metric-title">المساحة (هكتار)</div><div class="metric-val">{area_ha:.4f} Ha</div></div>
        </div>

        <div class="svg-card">
            <h2>المعاينة التفاعلية للمضلع المساحي (Polygon Graphics)</h2>
            <svg width="500" height="400" style="background:#ffffff; border:1px solid #ddd; border-radius:6px;">
                <polygon points="{polygon_points}" fill="rgba(52, 152, 219, 0.15)" stroke="#3498db" stroke-width="2" />
                {svg_points}
            </svg>
        </div>

        <div class="grid">
            <div class="card">
                <h2>جدول الإحداثيات المصححة</h2>
                <table>
                    <thead>
                        <tr>
                            <th>الشرقيات (E)</th>
                            <th>الشماليات (N)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {coord_rows}
                    </tbody>
                </table>
            </div>

            <div class="card">
                <h2>تفاصيل أخطاء القفل (Bowditch)</h2>
                <table>
                    <tr><th>Misclosure East (Wx)</th><td>{w_e:.4f} m</td></tr>
                    <tr><th>Misclosure North (Wy)</th><td>{w_n:.4f} m</td></tr>
                    <tr><th>Linear Misclosure (W)</th><td>{err:.4f} m</td></tr>
                    <tr><th>Precision Ratio</th><td>1 : {int(acc)}</td></tr>
                </table>
            </div>
        </div>
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"{Colors.OKGREEN}[+] HTML Dashboard generated successfully as '{filename}'{Colors.ENDC}")

# --- 3. الدوال المساحية الحسابية ---
def calculate_distance(e1, n1, e2, n2):
    return math.sqrt((e2 - e1) ** 2 + (n2 - n1) ** 2)

def calculate_azimuth(e1, n1, e2, n2):
    delta_e = e2 - e1
    delta_n = n2 - n1
    azimuth_deg = math.degrees(math.atan2(delta_e, delta_n))
    return azimuth_deg + 360 if azimuth_deg < 0 else azimuth_deg

def deg_to_dms(deg):
    d = int(deg)
    minutes_float = (deg - d) * 60
    m = int(minutes_float)
    s = (minutes_float - m) * 60
    return d, m, s

def calculate_forward_position(e1, n1, distance, azimuth_deg):
    azimuth_rad = math.radians(azimuth_deg)
    e2 = e1 + distance * math.sin(azimuth_rad)
    n2 = n1 + distance * math.cos(azimuth_rad)
    return e2, n2

def calculate_polygon_area(coords):
    n = len(coords) - 1
    area = 0.0
    for i in range(n):
        j = i + 1
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    area_sq_m = abs(area) / 2.0
    area_hectares = area_sq_m / 10000.0
    return area_sq_m, area_hectares

# --- 4. التصدير لصيغ DXF و GeoJSON ---
def export_to_dxf(coords, filename="traverse_output.dxf"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("0\nSECTION\n2\nENTITIES\n")
        
        # 1. رسم خطوط المضلع (باللون الأزرق Index 5)
        for i in range(len(coords) - 1):
            f.write("0\nLINE\n8\nTRAVERSE_BOUNDARY\n62\n5\n")
            f.write(f"10\n{coords[i][0]}\n20\n{coords[i][1]}\n30\n0.0\n")
            f.write(f"11\n{coords[i+1][0]}\n21\n{coords[i+1][1]}\n31\n0.0\n")
            
        # 2. رسم النقاط والكتابات (باللون الأصفر Index 2 للنصوص والأحمر Index 1 للنقاط)
        for i, (e, n) in enumerate(coords[:-1]):
            # رسم النقطة
            f.write("0\nPOINT\n8\nTRAVERSE_POINTS\n62\n1\n")
            f.write(f"10\n{e}\n20\n{n}\n30\n0.0\n")
            
            # كتابة اسم النقطة ملونة بالأصفر
            f.write("0\nTEXT\n8\nTRAVERSE_LABELS\n62\n2\n")
            f.write(f"10\n{e + 1.5}\n20\n{n + 1.5}\n30\n0.0\n")
            f.write("40\n2.0\n") # حجم الخط
            f.write(f"1\nP{i}\n")
            
        f.write("0\nENDSEC\n0\nEOF\n")
    print(f"{Colors.OKGREEN}[+] DXF File exported with colors successfully as '{filename}'{Colors.ENDC}")

def export_to_geojson(coords, filename="traverse_output.geojson"):
    features = []
    for i, (e, n) in enumerate(coords[:-1]):
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [e, n]},
            "properties": {"Point_ID": f"P{i}"},
        })

    features.append({
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": [coords]},
        "properties": {"Name": "Traverse Boundary"},
    })

    geojson_data = {"type": "FeatureCollection", "features": features}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(geojson_data, f, indent=4)
    print(f"{Colors.OKGREEN}[+] GeoJSON File exported successfully as '{filename}'{Colors.ENDC}")

# --- 5. تعديل المضلع والتصدير والرسم ---
def adjust_bowditch(distances, azimuths, start_e, start_n):
    total_length = sum(distances)
    delta_e_list = [d * math.sin(math.radians(az)) for d, az in zip(distances, azimuths)]
    delta_n_list = [d * math.cos(math.radians(az)) for d, az in zip(distances, azimuths)]

    w_e = sum(delta_e_list)
    w_n = sum(delta_n_list)
    linear_error = math.sqrt(w_e**2 + w_n**2)
    accuracy_ratio = total_length / linear_error if linear_error != 0 else float("inf")

    curr_e, curr_n = start_e, start_n
    adjusted_coords = [(curr_e, curr_n)]

    for i in range(len(distances)):
        corr_e = delta_e_list[i] - (distances[i] / total_length) * w_e
        corr_n = delta_n_list[i] - (distances[i] / total_length) * w_n
        curr_e += corr_e
        curr_n += corr_n
        adjusted_coords.append((curr_e, curr_n))

    return adjusted_coords, w_e, w_n, linear_error, accuracy_ratio

def draw_traverse_turtle(coords):
    screen = turtle.Screen()
    screen.title("SurveyPy - Traverse Plot")
    screen.setup(width=700, height=700)

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)
    t.color("blue")

    e_vals = [pt[0] for pt in coords]
    n_vals = [pt[1] for pt in coords]
    min_e, max_e = min(e_vals), max(e_vals)
    min_n, max_n = min(n_vals), max(n_vals)

    span_e = max_e - min_e if max_e != min_e else 1.0
    span_n = max_n - min_n if max_n != min_n else 1.0
    scale = 400 / max(span_e, span_n)

    start_x = (coords[0][0] - min_e - span_e / 2) * scale
    start_y = (coords[0][1] - min_n - span_n / 2) * scale

    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.dot(10, "red")
    t.write(f" P0 ({coords[0][0]:.1f}, {coords[0][1]:.1f})", font=("Arial", 10, "bold"))

    for i in range(1, len(coords)):
        x = (coords[i][0] - min_e - span_e / 2) * scale
        y = (coords[i][1] - min_n - span_n / 2) * scale
        t.goto(x, y)
        t.dot(8, "red")
        t.write(f" P{i} ({coords[i][0]:.1f}, {coords[i][1]:.1f})", font=("Arial", 10, "normal"))

    t.hideturtle()
    screen.mainloop()

def save_report(coords, w_e, w_n, err, acc, area_m2, area_ha):
    with open("traverse_report.txt", "w", encoding="utf-8") as f:
        f.write("========================================\n")
        f.write("      SurveyPy - Traverse Report        \n")
        f.write("========================================\n")
        f.write(f"Misclosure E (Wx) : {w_e:.4f} m\n")
        f.write(f"Misclosure N (Wy) : {w_n:.4f} m\n")
        f.write(f"Linear Error (W)  : {err:.4f} m\n")
        f.write(f"Precision Ratio   : 1 : {int(acc)}\n")
        f.write("----------------------------------------\n")
        f.write(f"Calculated Area   : {area_m2:.2f} m² ({area_ha:.4f} Ha)\n")
        f.write("----------------------------------------\n")
        f.write("Adjusted Coordinates:\n")
        for idx, (e, n) in enumerate(coords[:-1]):
            f.write(f"Point P{idx}: E = {e:.3f} m, N = {n:.3f} m\n")
    print(f"\n{Colors.OKGREEN}[+] Report saved successfully as 'traverse_report.txt'{Colors.ENDC}")

# --- 6. القائمة الرئيسية ---
def main():
    print_banner()
    print(f"{Colors.BOLD}========================================{Colors.ENDC}")
    print(f"{Colors.OKGREEN}1.{Colors.ENDC} Calculate Distance & Azimuth")
    print(f"{Colors.OKGREEN}2.{Colors.ENDC} Forward Computation (Polar to Rect)")
    print(f"{Colors.OKGREEN}3.{Colors.ENDC} Traverse Adjustment (Manual Input)")
    print(f"{Colors.OKGREEN}4.{Colors.ENDC} Traverse Adjustment (Load & Validate CSV)")
    print(f"{Colors.BOLD}========================================{Colors.ENDC}")

    choice = input(f"{Colors.WARNING}Enter choice (1, 2, 3, or 4): {Colors.ENDC}")

    if choice == "1":
        e1 = float(input("Enter E1: "))
        n1 = float(input("Enter N1: "))
        e2 = float(input("Enter E2: "))
        n2 = float(input("Enter N2: "))
        dist = calculate_distance(e1, n1, e2, n2)
        az = calculate_azimuth(e1, n1, e2, n2)
        d, m, s = deg_to_dms(az)
        print("\n--- Results ---")
        print(f"Distance: {dist:.3f} m")
        print(f"Azimuth : {az:.4f}° ({d}° {m}' {s:.2f}\")")

    elif choice == "2":
        e1 = float(input("Enter E1: "))
        n1 = float(input("Enter N1: "))
        dist = float(input("Enter Distance (m): "))
        az = float(input("Enter Azimuth (Degrees): "))
        e2, n2 = calculate_forward_position(e1, n1, dist, az)
        print("\n--- Calculated Point ---")
        print(f"E2: {e2:.3f} m")
        print(f"N2: {n2:.3f} m")

    elif choice in ["3", "4"]:
        start_e = float(input("Enter Start E: "))
        start_n = float(input("Enter Start N: "))

        if choice == "3":
            num_sides = int(input("Enter number of sides: "))
            distances, azimuths = [], []
            for i in range(num_sides):
                print(f"\nSide {i+1}:")
                distances.append(float(input("  Distance (m): ")))
                azimuths.append(float(input("  Azimuth (Deg): ")))
        else:
            filename = input("Enter CSV filename (Default: data.csv): ") or "data.csv"
            try:
                distances, azimuths = validate_and_load_data(filename)
                print(f"\n{Colors.OKGREEN}[+] Loaded & Validated {len(distances)} sides from '{filename}' successfully.{Colors.ENDC}")
            except Exception as e:
                print(f"\n{Colors.FAIL}[❌] Data Load Error: {e}{Colors.ENDC}")
                return

        coords, w_e, w_n, err, acc = adjust_bowditch(distances, azimuths, start_e, start_n)
        area_m2, area_ha = calculate_polygon_area(coords)

        print(f"\n{Colors.BOLD}================ Results ================{Colors.ENDC}")
        print(f"Misclosure E (Wx) : {w_e:.4f} m")
        print(f"Misclosure N (Wy) : {w_n:.4f} m")
        print(f"Linear Error (W)  : {err:.4f} m")
        print(f"Precision Ratio   : 1 : {int(acc)}")
        print(f"Calculated Area   : {area_m2:.2f} m² ({area_ha:.4f} Hectares)")
        print("----------------------------------------")
        print("Adjusted Coordinates:")
        for idx, (e, n) in enumerate(coords[:-1]):
            print(f"  Point P{idx}: E = {e:.3f} m, N = {n:.3f} m")

        save_report(coords, w_e, w_n, err, acc, area_m2, area_ha)
        export_to_dxf(coords)
        export_to_geojson(coords)
        generate_html_dashboard(coords, w_e, w_n, err, acc, area_m2, area_ha)
        draw_traverse_turtle(coords)

if __name__ == "__main__":
    main()