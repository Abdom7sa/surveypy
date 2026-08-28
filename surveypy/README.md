# SurveyPy 📐🧭

**SurveyPy** is a Python-based geomatics tool designed for processing field survey data, adjusting closed traverses using the **Bowditch (Compass) Rule**, and generating multi-format geospatial outputs.

---

## ✨ Features
- **Field Data Input:** Read distances and azimuths manually or directly from a structured `data.csv` file.
- **Data Validation:** Built-in checks to ensure distances are positive and azimuths fall within valid bounds ($0^\circ - 360^\circ$).
- **Traverse Adjustment:** Computes misclosures ($W_x, W_y$), linear error ($W$), precision ratio, and adjusted coordinates using the **Bowditch method**.
- **Area Calculation:** Automatic polygon area calculation in square meters ($\text{m}^2$) and hectares.
- **Multi-Format Export:**
  - **AutoCAD DXF (`.dxf`):** Boundary lines and point layers for CAD software.
  - **GIS GeoJSON (`.geojson`):** Polygon boundaries and point layers for QGIS and spatial analysis.
  - **Interactive HTML Dashboard (`.html`):** Clean web preview of the traverse layout with point coordinates.
  - **Text Summary Report (`.txt`):** Plaintext report of adjustment results.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.x (Uses standard libraries: `math`, `csv`, `json`, `turtle`).

### 2. CSV Data Structure (`data.csv`)
Place a `data.csv` file in the project directory formatted as follows:

```csv
Point,Distance,Azimuth
A-B,120.45,45.5
B-C,85.30,112.3
C-D,140.10,210.8
D-A,110.25,315.2
## 📄 License & Copyright

Copyright © 2026 Abdalrhman Musa. All rights reserved.
Licensed under the [MIT License](LICENSE).