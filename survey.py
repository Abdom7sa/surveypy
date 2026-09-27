"""
SurveyPy - Main Interactive CLI Engine & Exporter
Author: Abdalrhman Musa
"""
import sys
import os

# 1. Check module imports safely
try:
    from surveying.intersections import calculate_forward_intersection
except ImportError:
    calculate_forward_intersection = None

try:
    from gnss.rtk_config import GNSSQualityControl
except ImportError:
    GNSSQualityControl = None


def generate_sample_html_report(points, filename="traverse_dashboard.html"):
    """Fallback built-in HTML report generator."""
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>SurveyPy - Traverse Calculation Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f4f6f9; }}
        h1 {{ color: #2c3e50; }}
        table {{ border-collapse: collapse; width: 100%; background: white; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: center; }}
        th {{ background-color: #3498db; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>📐 SurveyPy Calculation Report</h1>
    <p><strong>Status:</strong> Successfully Processed</p>
    <table>
        <tr>
            <th>Point ID</th>
            <th>Easting (m)</th>
            <th>Northing (m)</th>
            <th>Elevation (m)</th>
        </tr>
"""
    for pt in points:
        html_content += f"""        <tr>
            <td>{pt['id']}</td>
            <td>{pt['easting']:.3f}</td>
            <td>{pt['northing']:.3f}</td>
            <td>{pt['elevation']:.3f}</td>
        </tr>\n"""

    html_content += """    </table>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)


def generate_sample_dxf(points, filename="traverse_output.dxf"):
    """Fallback built-in DXF generator."""
    dxf_content = "0\nSECTION\n2\nENTITIES\n"
    for pt in points:
        dxf_content += f"0\nPOINT\n8\nSURVEY_POINTS\n10\n{pt['easting']}\n20\n{pt['northing']}\n30\n{pt['elevation']}\n"
    dxf_content += "0\nENDSEC\n0\nEOF\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(dxf_content)


def main_menu():
    print("=" * 50)
    print(" 📐 Welcome to SurveyPy CLI Engine ")
    print("=" * 50)
    print("1. Forward Intersection Calculation")
    print("2. GNSS RTK Quality Assessment")
    print("3. Generate Full Project Outputs (HTML & DXF)")
    print("4. Exit")
    print("=" * 50)

    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        print("\n--- Forward Intersection ---")
        if calculate_forward_intersection is None:
            print("[!] Error: 'surveying.intersections' module is not found.")
            return

        try:
            ea = float(input("Enter Stn A Easting (E): "))
            na = float(input("Enter Stn A Northing (N): "))
            aza = float(input("Enter Azimuth A->C (degrees): "))
            eb = float(input("Enter Stn B Easting (E): "))
            nb = float(input("Enter Stn B Northing (N): "))
            azb = float(input("Enter Azimuth B->C (degrees): "))

            ec, nc = calculate_forward_intersection(ea, na, aza, eb, nb, azb)
            print(f"\n[✓] Calculated Target Coordinates: Easting = {ec}, Northing = {nc}")
        except Exception as e:
            print(f"\n[!] Calculation Error: {e}")

    elif choice == "2":
        print("\n--- GNSS Quality Check ---")
        if GNSSQualityControl is None:
            print("[!] Error: 'gnss.rtk_config' module is not found.")
            return

        try:
            pdop = float(input("Enter PDOP value: "))
            sats = int(input("Enter Satellite Count: "))
            status = input("Enter Fix Status (FIXED/FLOAT): ").strip().upper()

            qc = GNSSQualityControl()
            res = qc.evaluate_point_quality(pdop, sats, status)
            print(f"\n[✓] Quality Check Result: Valid = {res['is_valid']}")
        except Exception as e:
            print(f"\n[!] Input Error: {e}")

    elif choice == "3":
        print("\n--- Generating Spatial Data & HTML Report ---")
        sample_points = [
            {"id": "P1", "easting": 100.0, "northing": 200.0, "elevation": 10.5},
            {"id": "P2", "easting": 200.0, "northing": 200.0, "elevation": 11.0},
            {"id": "P3", "easting": 200.0, "northing": 300.0, "elevation": 10.8},
            {"id": "P4", "easting": 100.0, "northing": 300.0, "elevation": 10.2}
        ]

        # 1. HTML Report
        try:
            from reports.builder import generate_html_report
            generate_html_report(sample_points, filename="traverse_dashboard.html")
        except Exception:
            generate_sample_html_report(sample_points, filename="traverse_dashboard.html")
        print("[✓] Report saved: traverse_dashboard.html")

        # 2. DXF File
        try:
            from visualization.exporters import export_to_dxf
            export_to_dxf(sample_points, filename="traverse_output.dxf")
        except Exception:
            generate_sample_dxf(sample_points, filename="traverse_output.dxf")
        print("[✓] CAD Drawing saved: traverse_output.dxf")

        print("\n[+] All output artifacts generated successfully in the root folder!")

    elif choice == "4":
        print("\nExiting SurveyPy...")
        sys.exit(0)
    else:
        print("\n[!] Invalid choice, please try again.")


if __name__ == "__main__":
    try:
        main_menu()
    except Exception as err:
        print(f"\n[!] Execution error: {err}")
    finally:
        input("\n[+] Press Enter to exit...")