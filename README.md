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
