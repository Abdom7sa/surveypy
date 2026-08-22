import math
import turtle


# --- 1. الدوال الأساسية ---
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


# --- 2. حساب المساحة الإحداثية (Shoelace Formula) ---
def calculate_polygon_area(coords):
    n = len(coords) - 1  # النقطة الأخيرة هي تكرار للأولى
    area = 0.0
    for i in range(n):
        j = i + 1
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    area_sq_m = abs(area) / 2.0
    area_hectares = area_sq_m / 10000.0
    return area_sq_m, area_hectares


# --- 3. تصدير DXF لبرنامج الكاد (AutoCAD DXF Generator) ---
def export_to_dxf(coords, filename="traverse_output.dxf"):
    with open(filename, "w", encoding="utf-8") as f:
        # DXF Header & Entities Section
        f.write("0\nSECTION\n2\nENTITIES\n")

        # رسم الأضلاع (LINES)
        for i in range(len(coords) - 1):
            f.write("0\nLINE\n8\nTRAVERSE_BOUNDARY\n")
            f.write(
                f"10\n{coords[i][0]}\n20\n{coords[i][1]}\n30\n0.0\n"
            )  # Start Point
            f.write(
                f"11\n{coords[i+1][0]}\n21\n{coords[i+1][1]}\n31\n0.0\n"
            )  # End Point

        # رسم النقاط (POINTS)
        for i, (e, n) in enumerate(coords[:-1]):
            f.write("0\nPOINT\n8\nTRAVERSE_POINTS\n")
            f.write(f"10\n{e}\n20\n{n}\n30\n0.0\n")

        f.write("0\nENDSEC\n0\nEOF\n")
    print(f"[+] DXF File exported successfully as '{filename}'")


# --- 4. تعديل المضلع والتصدير والرسم ---
def adjust_bowditch(distances, azimuths, start_e, start_n):
    total_length = sum(distances)

    delta_e_list = [
        d * math.sin(math.radians(az)) for d, az in zip(distances, azimuths)
    ]
    delta_n_list = [
        d * math.cos(math.radians(az)) for d, az in zip(distances, azimuths)
    ]

    w_e = sum(delta_e_list)
    w_n = sum(delta_n_list)
    linear_error = math.sqrt(w_e**2 + w_n**2)
    accuracy_ratio = (
        total_length / linear_error if linear_error != 0 else float("inf")
    )

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
        t.write(
            f" P{i} ({coords[i][0]:.1f}, {coords[i][1]:.1f})",
            font=("Arial", 10, "normal"),
        )

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
    print("\n[+] Report saved successfully as 'traverse_report.txt'")


# --- 5. القائمة الرئيسية ---
def main():
    print("========================================")
    print("         SurveyPy - Main Menu           ")
    print("========================================")
    print("1. Calculate Distance & Azimuth")
    print("2. Forward Computation (Polar to Rect)")
    print("3. Traverse Adjustment, Area, DXF & Plot")
    print("========================================")

    choice = input("Enter choice (1, 2, or 3): ")

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

    elif choice == "3":
        print("\n--- Traverse Adjustment & Processing ---")
        num_sides = int(input("Enter number of sides: "))
        start_e = float(input("Enter Start E: "))
        start_n = float(input("Enter Start N: "))

        distances, azimuths = [], []
        for i in range(num_sides):
            print(f"\nSide {i+1}:")
            d = float(input("  Distance (m): "))
            az = float(input("  Azimuth (Deg): "))
            distances.append(d)
            azimuths.append(az)

        coords, w_e, w_n, err, acc = adjust_bowditch(
            distances, azimuths, start_e, start_n
        )
        area_m2, area_ha = calculate_polygon_area(coords)

        print("\n================ Results ================")
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
        draw_traverse_turtle(coords)


if __name__ == "__main__":
    main()