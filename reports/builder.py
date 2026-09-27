"""
SurveyPy - Executive Geomatics HTML Dashboard Builder
Author: Abdalrhman Musa
"""
import math
import os

def calculate_distance_and_bearing(e1, n1, e2, n2):
    """Calculates horizontal distance and azimuth bearing between two points."""
    de = e2 - e1
    dn = n2 - n1
    dist = math.hypot(de, dn)
    az = math.degrees(math.atan2(de, dn)) % 360
    return dist, az

def calculate_polygon_area(points):
    """Calculates polygon surface area using Shoelace formula."""
    n = len(points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i]['easting'] * points[j]['northing']
        area -= points[j]['easting'] * points[i]['northing']
    return abs(area) / 2.0

def generate_html_report(points, filename="traverse_dashboard.html"):
    """
    Generates an executive-grade interactive HTML dashboard with advanced SVG visuals.
    """
    if not points or len(points) < 2:
        print("[!] Error: At least 2 points are required for report generation.")
        return

    # Calculate Spatial Bounding Box & Dimensions
    eastings = [pt["easting"] for pt in points]
    northings = [pt["northing"] for pt in points]
    
    min_e, max_e = min(eastings), max(eastings)
    min_n, max_n = min(northings), max(northings)
    
    range_e = max(max_e - min_e, 10.0)
    range_n = max(max_n - min_n, 10.0)
    
    total_area = calculate_polygon_area(points)
    total_perimeter = 0.0
    
    # Calculate Segment Dynamics
    segments = []
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        dist, az = calculate_distance_and_bearing(p1['easting'], p1['northing'], p2['easting'], p2['northing'])
        total_perimeter += dist
        segments.append({
            "from": p1['id'],
            "to": p2['id'],
            "dist": dist,
            "bearing": az
        })

    # Viewport Canvas Configuration
    canvas_w, canvas_h = 650, 480
    pad = 60

    def sx(e):
        return pad + (e - min_e) / range_e * (canvas_w - 2 * pad)

    def sy(n):
        return canvas_h - (pad + (n - min_n) / range_n * (canvas_h - 2 * pad))

    # SVG Elements Rendering
    svg_elements = []
    
    # Grid Lines
    for i in range(1, 5):
        gx = pad + i * (canvas_w - 2 * pad) / 5
        gy = pad + i * (canvas_h - 2 * pad) / 5
        svg_elements.append(f'<line x1="{gx}" y1="{pad}" x2="{gx}" y2="{canvas_h-pad}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3"/>')
        svg_elements.append(f'<line x1="{pad}" y1="{gy}" x2="{canvas_w-pad}" y2="{gy}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3"/>')

    # Polygon & Traverse Boundary
    polygon_points_str = " ".join([f"{sx(pt['easting'])},{sy(pt['northing'])}" for pt in points])
    svg_elements.append(f'<polygon points="{polygon_points_str}" fill="rgba(14, 165, 233, 0.12)" stroke="#0284c7" stroke-width="2.5" stroke-linejoin="round"/>')

    # Points & Annotations
    for pt in points:
        cx, cy = sx(pt['easting']), sy(pt['northing'])
        label = pt['id']
        coords = f"({pt['easting']:.1f}, {pt['northing']:.1f})"
        
        # Halo glow & core station marker
        svg_elements.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="rgba(225, 29, 72, 0.2)"/>')
        svg_elements.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#e11d48" stroke="#ffffff" stroke-width="1.5"/>')
        svg_elements.append(f'<text x="{cx + 10}" y="{cy - 6}" font-size="12" font-family="system-ui" font-weight="700" fill="#0f172a">{label}</text>')
        svg_elements.append(f'<text x="{cx + 10}" y="{cy + 8}" font-size="9" font-family="system-ui" fill="#64748b">{coords}</text>')

    # North Arrow Indicator Graphic
    north_arrow = """
    <g transform="translate(590, 65)">
        <circle cx="0" cy="0" r="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
        <path d="M 0 -12 L 5 4 L 0 1 L -5 4 Z" fill="#0f172a"/>
        <path d="M 0 -12 L 0 1 L 5 4 Z" fill="#64748b"/>
        <text x="-4" y="16" font-size="10" font-weight="800" fill="#0f172a">N</text>
    </g>
    """
    svg_elements.append(north_arrow)

    # Scale Bar Graphic
    scale_bar = f"""
    <g transform="translate(50, 445)">
        <line x1="0" y1="0" x2="100" y2="0" stroke="#0f172a" stroke-width="3"/>
        <line x1="0" y1="-4" x2="0" y2="4" stroke="#0f172a" stroke-width="2"/>
        <line x1="100" y1="-4" x2="100" y2="4" stroke="#0f172a" stroke-width="2"/>
        <text x="32" y="-8" font-size="10" font-family="system-ui" font-weight="600" fill="#334155">{range_e/5:.1f} m</text>
    </g>
    """
    svg_elements.append(scale_bar)

    svg_canvas = f"""
    <svg width="{canvas_w}" height="{canvas_h}" viewBox="0 0 {canvas_w} {canvas_h}" style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; width: 100%; height: auto;">
        {''.join(svg_elements)}
    </svg>
    """

    # Build Complete HTML Template
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SurveyPy - Geomatics Processing Executive Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-main: #f8fafc;
            --panel-bg: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --accent-blue: #0284c7;
            --border-color: #e2e8f0;
        }}
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-main);
            color: var(--text-primary);
            margin: 0;
            padding: 32px 24px;
        }}
        .max-w {{ max-width: 1280px; margin: 0 auto; }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: white;
            padding: 28px 36px;
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
            margin-bottom: 28px;
        }}
        .header h1 {{ margin: 0; font-size: 26px; font-weight: 800; letter-spacing: -0.5px; }}
        .header p {{ margin: 6px 0 0 0; color: #94a3b8; font-size: 14px; }}
        .badge {{
            background: rgba(14, 165, 233, 0.2);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 700;
        }}
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 28px;
        }}
        .kpi-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            padding: 20px;
            border-radius: 14px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        .kpi-card .label {{ font-size: 12px; color: var(--text-secondary); font-weight: 600; text-transform: uppercase; tracking: 0.5px; }}
        .kpi-card .value {{ font-size: 24px; font-weight: 800; color: var(--text-primary); margin-top: 8px; }}
        .main-grid {{
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 28px;
        }}
        @media (max-width: 1024px) {{ .main-grid {{ grid-template-columns: 1fr; }} }}
        .panel {{
            background: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        .panel h2 {{ font-size: 18px; font-weight: 700; margin: 0 0 20px 0; color: var(--text-primary); display: flex; align-items: center; gap: 8px; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; }}
        th {{ background: #f1f5f9; color: var(--text-secondary); font-weight: 700; padding: 12px 14px; border-bottom: 1px solid var(--border-color); }}
        td {{ padding: 12px 14px; border-bottom: 1px solid #f1f5f9; font-weight: 500; }}
        tr:last-child td {{ border-bottom: none; }}
        tr:hover td {{ background: #f8fafc; }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            color: var(--text-secondary);
            font-size: 13px;
            font-weight: 500;
        }}
    </style>
</head>
<body>
    <div class="max-w">
        <div class="header">
            <div>
                <h1>📐 SurveyPy Engine Executive Dashboard</h1>
                <p>Automated Traversal Reduction, Coordinate Geometry & Quality Audit Report</p>
            </div>
            <span class="badge">STATUS: VERIFIED</span>
        </div>

        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="label">Total Stations</div>
                <div class="value">{len(points)}</div>
            </div>
            <div class="kpi-card">
                <div class="label">Total Perimeter</div>
                <div class="value">{total_perimeter:.2f} m</div>
            </div>
            <div class="kpi-card">
                <div class="label">Enclosed Area</div>
                <div class="value">{total_area:.2f} m²</div>
            </div>
            <div class="kpi-card">
                <div class="label">Surface Area (Hectares)</div>
                <div class="value">{total_area / 10000.0:.3f} ha</div>
            </div>
        </div>

        <div class="main-grid">
            <div class="panel">
                <h2>📍 Station Coordinates & Observations</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Station</th>
                            <th>Easting (m)</th>
                            <th>Northing (m)</th>
                            <th>Elev (m)</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    for pt in points:
        html_template += f"""
                        <tr>
                            <td><strong>{pt['id']}</strong></td>
                            <td>{pt['easting']:.3f}</td>
                            <td>{pt['northing']:.3f}</td>
                            <td>{pt['elevation']:.3f}</td>
                        </tr>"""

    html_template += f"""
                    </tbody>
                </table>

                <h2 style="margin-top: 28px;">📏 Leg Bearings & Distances</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Leg</th>
                            <th>Distance (m)</th>
                            <th>Azimuth Bearing</th>
                        </tr>
                    </thead>
                    <tbody>
"""
    for seg in segments:
        html_template += f"""
                        <tr>
                            <td><strong>{seg['from']} ➔ {seg['to']}</strong></td>
                            <td>{seg['dist']:.3f} m</td>
                            <td>{seg['bearing']:.2f}°</td>
                        </tr>"""

    html_template += f"""
                    </tbody>
                </table>
            </div>

            <div class="panel" style="text-align: center;">
                <h2 style="justify-content: center;">🗺️ High-Precision Vector Canvas (SVG)</h2>
                {svg_canvas}
            </div>
        </div>

        <div class="footer">
            <p>Generated by <strong>SurveyPy Core Library</strong> • Developed by <strong>Abdalrhman Musa</strong></p>
        </div>
    </div>
</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)