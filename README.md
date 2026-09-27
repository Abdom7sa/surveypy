
```markdown
# 📐 SurveyPy - Geomatics & GIS Processing Engine

**SurveyPy** is an open-source Python library designed to automate field survey reductions, coordinate transformations, RTK GNSS quality control, and multi-format spatial data exports for CAD and GIS platforms.

---

## 🚀 Key Features & Modules

* **Closed Traverse Adjustment:** Computes Bowditch balancing (Compass Rule), linear misclosure error, relative precision, and total surface area in $m^2$ and hectares.
* **Forward Intersection:** Calculates 2D coordinates for inaccessible target stations using observed azimuth directions.
* **Grid Leveling & Cut/Fill Volumes:** Processes grid leveling matrices and calculates total earthwork volumes based on a design elevation.
* **Coordinate Transformations:** Executes 2D conformal Helmert transformations (scale, rotation, translation) between local site coordinates and global UTM reference systems.
* **GNSS Quality Control:** Validates RTK observation metrics including PDOP limits, satellite visibility counts, and solution fix statuses.
* **Multi-Format Spatial Exports:** Generates native vector formats for `AutoCAD (.dxf)`, `GeoJSON`, `ESRI Shapefile (.shp)`, and `GeoPackage (.gpkg)`.
* **Interactive HTML Reports:** Produces standalone mathematical audit reports complete with step-by-step reduction breakdowns and SVG polygon graphics.

---

## 📁 Project Architecture

```text
surveypy/
│
├── adjustment/             # Traverse adjustment & Bowditch reduction modules
│   ├── __init__.py
│   └── traverse.py
│
├── geodesy/                # Coordinate systems & Helmert 2D transformations
│   ├── __init__.py
│   └── transformations.py
│
├── gnss/                   # RTK quality control & observation metrics
│   ├── __init__.py
│   └── rtk_config.py
│
├── reports/                # Step-by-step HTML dashboard builder
│   ├── __init__.py
│   └── builder.py
│
├── surveying/              # Core surveying algorithms (Intersection & Grid Leveling)
│   ├── __init__.py
│   ├── intersections.py
│   └── leveling.py
│
├── visualization/          # CAD and GIS vector exporters (.dxf, .shp, .gpkg, .geojson)
│   ├── __init__.py
│   └── exporters.py
│
├── data/                   # Raw field observation inputs
│   └── data.csv
│
├── survey.py               # Main CLI entry point
├── test_survey.py          # Automated unit testing suite
└── README.md               # Project documentation

```

---

## 📥 Installation & Setup

### Option A: Direct ZIP Download

You can download the full repository directly as a ZIP archive:

> 📦 **[Download SurveyPy Source Code (.zip)](https://www.google.com/search?q=https://github.com/Abdom7sa/SurveyPy/archive/refs/heads/main.zip&utm_source=gemini)**

1. Extract the downloaded `SurveyPy-main.zip` file.
2. Open your terminal/command prompt inside the extracted project folder.

---

### Option B: Clone via Git

```bash
git clone [https://github.com/Abdom7sa/SurveyPy.git](https://github.com/Abdom7sa/SurveyPy.git)
cd SurveyPy

```

---

### Prerequisites & Dependencies

Ensure Python 3.8+ is installed on your environment. To enable advanced spatial layer exports (`Shapefile` & `GeoPackage`), install the recommended dependencies:

```bash
pip install geopandas shapely

```

---

## 📖 Quick Start & Execution

### 1. Running the Interactive Engine

Launch the CLI interface to access all calculation tools:

```bash
python survey.py

```

### 2. Running Automated Unit Tests

Verify module integration and mathematical functions:

```bash
python test_survey.py

```

---

## 📊 Generated Output Artifacts

Upon processing, `SurveyPy` outputs ready-to-use spatial files:

* **`traverse_dashboard.html`**: Interactive calculation dashboard for browser viewing.
* **`traverse_output.dxf`**: Structured CAD drawing for AutoCAD & Civil 3D.
* **`traverse_layer.gpkg` / `.shp**`: GIS layers ready for QGIS & ArcGIS Pro.

---

## 👨‍💻 Author

* **Abdalrhman Musa** - Geomatics Engineering

```

```

https://img.shields.io/badge/python-3.8%2B-blue.svg