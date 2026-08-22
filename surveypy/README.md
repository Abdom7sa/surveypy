# SurveyPy - Surveying & Geomatics Calculations Toolkit

**SurveyPy** is an open-source Python toolkit designed for Geomatics and Surveying Engineers to automate field boundary computations, closed traverse adjustments, planar geometric transformations, area estimations, and CAD interoperability.

---

## 🌟 Key Features

* **Distance & Azimuth Calculation**: Computes Euclidean distance and full 360° forward bearings with Degree-Minute-Second (DMS) conversion.
* **Forward Coordinate Computation (Polar to Rectangular)**: Calculates target coordinates given a starting point, distance, and azimuth angle.
* **Bowditch (Compass Rule) Traverse Adjustment**: Distributes linear misclosures ($\Delta E, \Delta N$) proportionally across traverse sides and evaluates total linear precision ratios ($1 : N$).
* **Coordinate Area Computation (Shoelace Formula)**: Calculates closed polygon surface area in both square meters ($m^2$) and hectares ($Ha$).
* **Automated Technical Report Generation**: Generates clean, ready-to-print text reports (`traverse_report.txt`) summarizing misclosures, precision, area, and final adjusted coordinates.
* **AutoCAD Integration (`.dxf` Export)**: Exports adjusted traverse boundaries and vertices directly to standard ASCII DXF format (`traverse_output.dxf`) for AutoCAD and Civil 3D workflows.
* **Interactive Graphical Visualization**: Render real-time scaled vector graphics of traverse geometry using built-in interactive plotting engines.

---

## 📂 Project Structure

```text
surveypy/
│
├── survey.py              # Main Python interactive application script
├── traverse_report.txt    # Generated technical adjustment report
├── traverse_output.dxf    # Generated AutoCAD DXF file
└── README.md              # Project documentation