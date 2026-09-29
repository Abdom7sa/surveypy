# 🗺️ SurveyPy

### A Python-Based Geomatics & Spatial Data Processing Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![QGIS](https://img.shields.io/badge/QGIS-Compatible-589632?style=for-the-badge&logo=qgis&logoColor=white)](https://qgis.org/)
[![CAD](https://img.shields.io/badge/CAD-DXF-E51050?style=for-the-badge&logo=autodesk&logoColor=white)](https://www.autodesk.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[![GitHub](https://img.shields.io/badge/GitHub-Abdom7sa-181717?style=flat-square&logo=github)](https://github.com/Abdom7sa)

---

## 📐 About

**SurveyPy** is a Python-based geomatics and spatial data processing engine developed to automate common surveying calculations and reduce repetitive field-to-office workflows.

The project combines:

- 📍 Surveying computations
- 📐 Traverse adjustment
- 📊 Grid leveling
- 🌐 Coordinate transformation
- 🗺️ GIS data export
- 📏 CAD/DXF export
- 📑 Automated HTML reporting

The goal is simple:

> **Field observations → Mathematical processing → Adjusted coordinates → CAD/GIS deliverables**

---

## 🚀 Key Features

### 📍 Closed Traverse Adjustment

SurveyPy can process closed traverse observations and calculate:

- Latitudes
- Departures
- Linear misclosure
- Relative precision
- Bowditch / Compass Rule adjustment
- Adjusted coordinates
- Polygon area
- Area in hectares

---

### 📐 Forward Intersection

Computes the coordinates of an inaccessible point using observations from two known control stations.

This provides a practical solution for basic surveying and coordinate determination workflows.

---

### 📊 Grid Leveling & Earthwork

Processes grid leveling observations and calculates:

- Reduced levels
- Cut volume
- Fill volume
- Net earthwork quantities

The calculations can be based on a specified design elevation and grid cell dimensions.

---

### 🌐 2D Helmert Transformation

SurveyPy supports a 4-parameter 2D Helmert transformation using:

- Translation X
- Translation Y
- Rotation
- Scale

This can be used to transform local survey coordinates into a target coordinate reference system.

---

## 🗺️ GIS & CAD Export

SurveyPy connects mathematical surveying workflows with GIS and CAD software.

| Format | Use |
|---|---|
| `.dxf` | AutoCAD / Civil 3D |
| `.geojson` | QGIS / ArcGIS Pro / Web GIS |
| `.shp` | ESRI Shapefile |
| `.gpkg` | GeoPackage |
| `.csv` | Survey data |
| `.html` | Processing reports |

---

## 📑 Automated Reports

The traverse workflow can generate an HTML report containing:

- Survey observations
- Coordinate calculations
- Misclosure results
- Adjustment results
- Area calculations
- Summary statistics
- Polygon visualization
- SVG graphics

---

---

---

🛠️ Technology Stack
Programming
�
Spatial Processing
� �
Visualization
� �
GIS & CAD
� � �


📁 Project Structure
SurveyPy/
│
├── survey.py
├── Test_survey.py
├── data.csv
│
├── adjustment/
│   ├── __init__.py
│   └── traverse.py
│
├── geodesy/
│   ├── __init__.py
│   └── transformations.py
│
├── surveying/
│   ├── __init__.py
│   ├── intersections.py
│   └── leveling.py
│
├── visualization/
│   ├── __init__.py
│   └── exporters.py
│
├── reports/
│   ├── __init__.py
│   └── builder.py
│
├── .gitignore
├── LICENSE
└── README.md


⚡ Quick Start
1. Clone the Repository
git clone https://github.com/Abdom7sa/SurveyPy.git
cd SurveyPy
2. Install Dependencies
pip install geopandas shapely matplotlib
3. Prepare Your Data
Example data.csv:
Distance,Azimuth
120.50,45.25
85.30,135.10
110.15,225.80
90.40,315.40
4. Run SurveyPy
python survey.py



📤 Generated Outputs
Depending on the workflow, SurveyPy can generate:
traverse_dashboard.html
traverse_output.dxf
traverse_layer.geojson
traverse_layer.gpkg
traverse_layer_points.shp
traverse_points.csv
These files can be imported directly into common GIS and CAD environments.


🧪 Testing
Run the available test suite with:
python Test_survey.py


🎯 Project Goals
SurveyPy is being developed to:
Automate repetitive surveying calculations
Reduce manual calculation errors
Connect surveying with GIS workflows
Generate CAD-ready outputs
Generate GIS-ready datasets
Produce reproducible calculation reports
Explore Python-based automation in geomatics engineering


🔮 Future Development
Planned or possible future additions include:
Least Squares Network Adjustment
Resection / Free Station
Additional coordinate transformations
GNSS data processing
COGO tools
Additional CAD export capabilities
Expanded GIS formats
Automated quality-control reports
Graphical User Interface


🤝 Contributing
Contributions and suggestions are welcome.
If you are interested in surveying, geomatics, GIS, CAD automation, or Python-based spatial processing, feel free to:
Open an Issue
Suggest an improvement
Fork the repository
Submit a Pull Request


👨‍💻 Author
Abdalrhman Musa Mohmed
Geomatics Engineering Student
Surveying Engineering | GIS | Remote Sensing | Python
GitHub:
https://github.com/Abdom7sa⁠

SurveyPy:
https://github.com/Abdom7sa/SurveyPy⁠
---

## 🔄 Workflow

```text
┌──────────────────────┐
│   FIELD OBSERVATIONS │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      SurveyPy        │
│    Python Engine     │
└──────────┬───────────┘
           │
     ┌─────┼─────┐
     ▼     ▼     ▼
 Traverse  Grid  Intersection
 Adjustment Leveling
     │      │      │
     └──────┼──────┘
            ▼
┌──────────────────────┐
│ Coordinate Processing│
└──────────┬───────────┘
           │
           ▼
   ┌───────┼────────┐
   ▼       ▼        ▼
  DXF    GeoJSON   GeoPackage
   │       │        │
   ▼       ▼        ▼
AutoCAD   QGIS   ArcGIS Pro

 


📜 License
This project is licensed under the MIT License.
See the LICENSE file for details.
