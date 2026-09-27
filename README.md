

```markdown
# 📐 SurveyPy: Advanced Geomatics & Spatial Analytics Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![QGIS](https://img.shields.io/badge/QGIS-Compatible-589632.svg?style=for-the-badge&logo=qgis&logoColor=white)
![ArcGIS](https://img.shields.io/badge/ArcGIS_Pro-Supported-007AC2.svg?style=for-the-badge&logo=esri&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**SurveyPy** is a modular Python library engineered for field geomatics, boundary geodesy, and automated CAD/GIS spatial output delivery. Designed for surveying engineers, GIS analysts, and spatial software developers, it bridges field measurement analytics with executive reporting and modern spatial pipelines.

---

## ✨ Key Capabilities & Modules

* 📍 **Surveying Mechanics (`surveying/`)**: Forward & Reverse Intersection solvers, closed traverse calculations, and grid leveling cut/fill volume computation.
* 📐 **Adjustment Computations (`adjustment/`)**: Least Squares adjustment engines, Bowditch traverse balancing, and residual analysis.
* 🌐 **Geodetic Core (`geodesy/`)**: 2D/3D Helmert transformation models, datum shifts, and coordinate conversions.
* 🛰️ **GNSS Quality Audit (`gnss/`)**: Automated RTK fix validator inspecting satellite count, status thresholds, and PDOP metrics.
* 📊 **Executive HTML Dashboards (`reports/`)**: Automated generation of interactive HTML evaluation reports featuring dynamic **SVG Vector Graphics**, scale bars, grid lines, and North arrow indicators.
* 🗺️ **Multi-Format Interoperability (`visualization/`)**: Direct export pipelines targeting **QGIS**, **ArcGIS Pro** (`.geojson`, `.csv`), and CAD platforms (`.dxf`).

---

## 🏗️ Project Architecture

```text
surveypy/
├── adjustment/       # Least Squares & Bowditch traverse adjustments
│   ├── __init__.py
│   └── traverse.py
├── geodesy/          # Helmert transformations & datum shifts
│   ├── __init__.py
│   └── transformations.py
├── gnss/             # RTK/PPK GNSS quality control validator
│   ├── __init__.py
│   └── rtk_config.py
├── reports/          # Executive HTML & SVG report builders
│   ├── __init__.py
│   └── builder.py
├── surveying/        # Intersections, grid leveling & COGO algorithms
│   ├── __init__.py
│   ├── intersections.py
│   └── leveling.py
├── visualization/    # CAD (.dxf) & GIS (.geojson, .csv) exporters
│   ├── __init__.py
│   └── exporters.py
├── Test_survey.py    # Automated unittest validation suite
├── survey.py         # Main Interactive CLI Engine & Exporter
├── .gitignore        # Version control exclude patterns
└── README.md         # Project documentation

```

---

## 🚀 Quick Start Guide

### 1. Installation & Setup

Clone the repository and switch to the project directory:

```bash
git clone [https://github.com/Abdom7sa/surveypy.git](https://github.com/Abdom7sa/surveypy.git)
cd surveypy

```

### 2. Run Main Interactive CLI Engine

Launch the central interactive CLI menu to compute measurements or generate project deliverables:

```bash
python survey.py

```

### 3. Run Automated Unit Tests

Verify mathematical integrity and module health:

```bash
python Test_survey.py

```

---

## 📊 Generated Deliverables

Executing Option `3` inside `survey.py` automatically exports all spatial artifacts into the root directory:

* 📄 **`traverse_dashboard.html`**: Interactive HTML dashboard with embedded SVG vector map, station coordinates, perimeter, area (m² & ha), and leg bearings.
* 🗺️ **`traverse_layer.geojson`**: GIS vector layer ready for direct Drag & Drop into **QGIS** or **ArcGIS Pro**.
* 📊 **`traverse_points.csv`**: Attribute table formatted for XY table import in GIS software.
* 📐 **`traverse_output.dxf`**: Vector drawing compatible with **AutoCAD** and **Civil 3D**.

---

## 💻 Python Code Examples

### 1. Forward Intersection Computation

```python
from surveying.intersections import calculate_forward_intersection

# Calculate coordinates of point C from stations A and B
easting_c, northing_c = calculate_forward_intersection(
    e_a=100.0, n_a=200.0, az_a=45.0,
    e_b=300.0, n_b=200.0, az_b=315.0
)
print(f"Target Point C: Easting = {easting_c}, Northing = {northing_c}")

```

### 2. GNSS RTK Quality Evaluation

```python
from gnss.rtk_config import GNSSQualityControl

qc = GNSSQualityControl()
result = qc.evaluate_point_quality(pdop=1.5, sat_count=12, status="FIXED")
print(f"Point Quality Valid: {result['is_valid']}")

```

### 3. Generating Dashboard & GIS Exports

```python
from reports.builder import generate_html_report
from visualization.exporters import export_to_geojson

points = [
    {"id": "P1", "easting": 100.0, "northing": 200.0, "elevation": 10.5},
    {"id": "P2", "easting": 250.0, "northing": 200.0, "elevation": 11.0},
    {"id": "P3", "easting": 200.0, "northing": 350.0, "elevation": 10.8},
    {"id": "P4", "easting": 100.0, "northing": 300.0, "elevation": 10.2}
]

# Generate Dashboard & GIS Files
generate_html_report(points, filename="traverse_dashboard.html")
export_to_geojson(points, filename="traverse_layer.geojson")

```

---

## 👤 Author & Maintainer

* **Abdalrhman Musa Mohmed**
* *Geomatics Engineer & Spatial Software Developer*
* **GitHub:** [@Abdom7sa](https://www.google.com/search?q=https://github.com/Abdom7sa&utm_source=gemini)



---

## 📜 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE&utm_source=gemini).

```

```
