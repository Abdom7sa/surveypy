🗺️ SurveyPy

A Python-Based Geomatics & Spatial Data Processing Engine

""Python" (https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)" (https://www.python.org/)
""QGIS" (https://img.shields.io/badge/QGIS-Compatible-589632?style=for-the-badge&logo=qgis&logoColor=white)" (https://qgis.org/)
""AutoCAD" (https://img.shields.io/badge/CAD-DXF-E51050?style=for-the-badge&logo=autodesk&logoColor=white)" (https://www.autodesk.com/)
""License" (https://img.shields.io/badge/License-MIT-green?style=for-the-badge)" (LICENSE)

""GitHub" (https://img.shields.io/badge/GitHub-Abdom7sa-181717?style=flat-square&logo=github)" (https://github.com/Abdom7sa)
""Repository" (https://img.shields.io/badge/Repository-SurveyPy-blue?style=flat-square&logo=github)" (https://github.com/Abdom7sa/SurveyPy)

---

📐 About

SurveyPy is a Python-based geomatics and spatial data processing engine developed to automate common surveying calculations and reduce repetitive field-to-office workflows.

The project brings together surveying computations, coordinate transformations, spatial data processing, CAD export, GIS export, and automated reporting in one Python workflow.

Instead of performing the same calculations manually or moving repeatedly between different software environments, SurveyPy is designed to process survey data programmatically and produce ready-to-use outputs for AutoCAD, QGIS, and ArcGIS Pro.

«From field observations → mathematical reduction → adjusted coordinates → CAD/GIS deliverables.»

---

🚀 Key Features

📍 Closed Traverse Adjustment

SurveyPy processes closed traverse observations and performs:

- Distance and azimuth calculations
- Latitude and departure computation
- Linear misclosure calculation
- Relative precision calculation
- Bowditch / Compass Rule adjustment
- Adjusted coordinate computation
- Polygon area calculation
- Area conversion to hectares

The workflow is designed to turn raw field observations into an adjusted traverse with minimal manual processing.

---

📐 Forward Intersection

Computes the coordinates of an inaccessible target point using observations from two known control stations.

This module can be used for basic surveying and coordinate determination workflows where the target point cannot be directly occupied.

---

📊 Grid Leveling & Earthwork

Processes grid leveling observations and calculates:

- Reduced ground levels
- Grid-based elevation information
- Cut volumes
- Fill volumes
- Net earthwork quantities

A design elevation and grid cell dimensions can be used to estimate the required earthwork quantities.

---

🌐 2D Helmert Transformation

SurveyPy includes a 4-parameter 2D Helmert transformation for transforming local coordinates between coordinate systems using control points.

The transformation handles:

- Translation in X
- Translation in Y
- Rotation
- Scale

This provides a practical workflow for converting local survey coordinates into a target coordinate reference system such as a projected UTM system.

---

🗺️ GIS & CAD Export

SurveyPy is designed to connect mathematical survey processing with common geospatial software.

Supported output formats include:

Format| Purpose
".dxf"| AutoCAD / Civil 3D
".geojson"| Web GIS / QGIS / ArcGIS Pro
".shp"| ESRI Shapefile
".gpkg"| GeoPackage
".csv"| Tabular survey data
".html"| Interactive processing report

---

📑 Automated HTML Reports

The traverse workflow can generate a standalone HTML dashboard containing:

- Survey observations
- Coordinate calculations
- Misclosure information
- Adjustment results
- Area calculations
- Summary statistics
- Polygon visualization
- SVG-based graphical output

This makes it easier to review and document the complete calculation process.

---

🧩 Workflow

                FIELD OBSERVATIONS
                       │
                       ▼
                ┌──────────────┐
                │   SurveyPy   │
                │ Python Engine│
                └──────┬───────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Traverse     Intersection   Leveling
      Adjustment     Analysis     & Volumes
          │            │            │
          └────────────┼────────────┘
                       ▼
              Coordinate Processing
                       │
                       ▼
              Spatial Data Outputs
             ┌─────────┼─────────┐
             ▼         ▼         ▼
            DXF      GeoJSON    GPKG
             │         │         │
             ▼         ▼         ▼
         AutoCAD     QGIS    ArcGIS Pro

---

🛠️ Technology Stack

Programming

"Python" (https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

SurveyPy is primarily developed in Python, using Python-based mathematical and spatial processing workflows.

Geospatial

"GeoPandas" (https://img.shields.io/badge/GeoPandas-139C5A?style=flat-square&logo=python&logoColor=white)
"Shapely" (https://img.shields.io/badge/Shapely-Geometry-blue?style=flat-square)

Used for spatial data processing and vector geometry operations.

Visualization & Reporting

"Matplotlib" (https://img.shields.io/badge/Matplotlib-Visualization-orange?style=flat-square&logo=python&logoColor=white)
"HTML" (https://img.shields.io/badge/HTML-Reports-E34F26?style=flat-square&logo=html5&logoColor=white)
"SVG" (https://img.shields.io/badge/SVG-Graphics-FFB13B?style=flat-square&logo=svg&logoColor=black)

GIS & CAD Ecosystem

"QGIS" (https://img.shields.io/badge/QGIS-589632?style=flat-square&logo=qgis&logoColor=white)
"ArcGIS" (https://img.shields.io/badge/ArcGIS_Pro-007AC2?style=flat-square&logo=esri&logoColor=white)
"AutoCAD" (https://img.shields.io/badge/AutoCAD-E51050?style=flat-square&logo=autodesk&logoColor=white)

---

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

«The structure may evolve as new surveying and spatial processing modules are added.»

---

⚡ Quick Start

1. Clone the Repository

git clone https://github.com/Abdom7sa/SurveyPy.git
cd SurveyPy

---

2. Install Dependencies

Install the required spatial and visualization libraries:

pip install geopandas shapely matplotlib

---

3. Prepare Your Survey Data

For a closed traverse, prepare your field observations in a CSV file:

Distance,Azimuth
120.50,45.25
85.30,135.10
110.15,225.80
90.40,315.40

---

4. Run SurveyPy

Launch the interactive command-line interface:

python survey.py

The CLI provides access to the available surveying and spatial processing workflows.

---

📤 Output Examples

After processing survey data, SurveyPy can generate outputs such as:

traverse_dashboard.html
traverse_output.dxf
traverse_layer.geojson
traverse_layer.gpkg
traverse_layer_points.shp
traverse_points.csv

These outputs can then be opened or imported into common engineering and GIS software.

---

🧪 Testing

The project includes a test script for checking the implemented surveying calculations.

Run:

python Test_survey.py

---

🎯 Project Goals

SurveyPy is being developed with several practical goals:

- Automate repetitive surveying calculations
- Reduce manual calculation errors
- Connect field surveying with GIS workflows
- Provide lightweight Python-based alternatives for routine processing
- Produce CAD and GIS-ready outputs directly from calculations
- Make surveying computations easier to reproduce and document
- Explore the use of Python for modern geomatics engineering workflows

---

🔮 Future Development

Possible future additions include:

- Least Squares Network Adjustment
- Resection / Free Station
- Additional coordinate transformations
- GNSS data processing
- COGO tools
- Additional CAD export capabilities
- More GIS formats
- Automated quality-control reports
- Expanded visualization tools
- Graphical user interface

---

🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you are interested in surveying, geomatics, GIS, CAD automation, or Python-based spatial processing, feel free to explore the repository, open an issue, or submit a Pull Request.

git fork https://github.com/Abdom7sa/SurveyPy

---

👨‍💻 Author

Abdalrhman Musa Mohmed

Geomatics Engineering Student
Surveying Engineering | GIS | Remote Sensing | Python

🔗 GitHub:
https://github.com/Abdom7sa

🔗 SurveyPy Repository:
https://github.com/Abdom7sa/SurveyPy

---

📜 License

This project is licensed under the MIT License.

See the "LICENSE" (LICENSE) file for more information.

---

<div align="center">📐 Surveying + 🐍 Python + 🗺️ GIS + 💻 Automation

SurveyPy — Turning Survey Computations into Reproducible Spatial Workflows.

⭐ If you find the project useful, consider giving it a star.

</div> 
