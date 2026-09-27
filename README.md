
```markdown
# 🗺️ SurveyPy: Advanced Geomatics & Spatial Analytics Engine

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=36BCF7&width=500&lines=Geomatics+Engineering+Engine;Python+Spatial+Analytics;QGIS+%26+ArcGIS+Pro+Exporter;Automated+CAD%2FGIS+Deliverables)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdalrhman-musa-372216249)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:hatmm2749@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdom7sa)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

---

## 🧑‍💻 About SurveyPy
**SurveyPy** is a high-performance Python library engineered for field geomatics, boundary geodesy, and automated CAD/GIS spatial output delivery. Designed for surveying engineers, GIS analysts, and spatial software developers, it bridges field measurement analytics with interactive HTML reports and modern spatial software workflows.

---

## 🛠️ Key Capabilities & Modules

* 📍 **Surveying Mechanics (`surveying/`)**: Forward & Reverse Intersection solvers, closed traverse adjustments, and grid leveling volume calculations.
* 📐 **Adjustment Computations (`adjustment/`)**: Least Squares adjustment engines, Bowditch traverse balancing, and residual analysis.
* 🌐 **Geodetic Core (`geodesy/`)**: 2D/3D Helmert transformation models, datum shifts, and coordinate conversions.
* 🛰️ **GNSS Quality Audit (`gnss/`)**: Automated RTK fix validator inspecting satellite count, status thresholds, and PDOP metrics.
* 📊 **Executive HTML Dashboards (`reports/`)**: Automated generation of interactive HTML evaluation reports featuring dynamic **SVG Vector Graphics**, scale bars, grid lines, and North arrow indicators.
* 🗺️ **Multi-Format Interoperability (`visualization/`)**: Direct export pipelines targeting **QGIS**, **ArcGIS Pro** (`.geojson`, `.csv`), and CAD platforms (`.dxf`).

---

## 💻 Tech Stack & Compatibility

### GIS & Remote Sensing
![QGIS](https://img.shields.io/badge/QGIS-589632?style=flat-square&logo=qgis&logoColor=white)
![ArcGIS](https://img.shields.io/badge/ArcGIS_Pro-007AC2?style=flat-square&logo=esri&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-336791?style=flat-square&logo=postgresql&logoColor=white)

### Programming & Automation
![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![GeoJSON](https://img.shields.io/badge/GeoJSON-Standard-000000?style=flat-square&logo=json&logoColor=white)

### CAD & Engineering
![AutoCAD](https://img.shields.io/badge/AutoCAD-E51222?style=flat-square&logo=autodesk&logoColor=white)
![Civil 3D](https://img.shields.io/badge/Civil_3D-0696D7?style=flat-square&logo=autodesk&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

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

### 1. Installation & Environment Setup

Clone the repository and verify your Python environment:

```bash
git clone [https://github.com/Abdom7sa/surveypy.git](https://github.com/Abdom7sa/surveypy.git)
cd surveypy

```

### 2. Run Interactive CLI Engine

Execute the central CLI menu to calculate survey points or export deliverables:

```bash
python survey.py

```

### 3. Run Unit Test Suite

Verify module integrity and mathematical consistency:

```bash
python Test_survey.py

```

---

## 📂 Generated Deliverables

Executing Option `3` inside `survey.py` automatically generates all spatial artifacts into the root directory:

* 📄 **`traverse_dashboard.html`**: Executive dashboard with embedded SVG vector map, station coordinates, perimeter, area, and leg bearings.
* 🗺️ **`traverse_layer.geojson`**: Vector layer compatible with **QGIS** and **ArcGIS Pro** via direct Drag & Drop.
* 📊 **`traverse_points.csv`**: Attribute table formatted for XY table import in GIS software.
* 📐 **`traverse_output.dxf`**: Vector drawing compatible with **AutoCAD** and **Civil 3D**.

---

## 👤 Author & Maintainer

* **Abdalrhman Musa Mohmed**
* *Geomatics Engineer & Geospatial Software Developer*
* **GitHub:** [@Abdom7sa](https://github.com/Abdom7sa?utm_source=gemini)
* **LinkedIn:** [Abdalrhman Musa](https://www.linkedin.com/in/abdalrhman-musa-372216249?utm_source=gemini)
* **Email:** [hatmm2749@gmail.com](https://www.google.com/search?q=mailto%3Ahatmm2749%40gmail.com)



---

## 📊 Developer Stats

---

## 📜 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE&utm_source=gemini).

```

```
