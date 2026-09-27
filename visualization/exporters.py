"""
SurveyPy - GIS Data Exporter for QGIS & ArcGIS Pro
Author: Abdalrhman Musa
"""
import json
import csv


def export_to_geojson(points, filename="traverse_layer.geojson"):
    """
    Exports points and polygon geometry to GeoJSON format compatible with QGIS & ArcGIS Pro.
    """
    features = []

    # 1. Add Point Features with Attributes
    for pt in points:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [pt["easting"], pt["northing"], pt["elevation"]]
            },
            "properties": {
                "Station_ID": pt["id"],
                "Easting_m": pt["easting"],
                "Northing_m": pt["northing"],
                "Elevation_m": pt["elevation"],
                "Software": "SurveyPy"
            }
        })

    # 2. Add Polygon Geometry Feature if 3 or more points exist
    if len(points) >= 3:
        poly_coords = [[pt["easting"], pt["northing"], pt["elevation"]] for pt in points]
        poly_coords.append(poly_coords[0])  # Close polygon loop

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [poly_coords]
            },
            "properties": {
                "Layer_Type": "Traverse Boundary",
                "Total_Stations": len(points),
                "Software": "SurveyPy"
            }
        })

    geojson_data = {
        "type": "FeatureCollection",
        "name": "SurveyPy_Traverse_Export",
        "features": features
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(geojson_data, f, indent=4)


def export_to_gis_csv(points, filename="traverse_points.csv"):
    """
    Exports points to CSV formatted for easy import into ArcGIS Pro / QGIS XY Table to Point.
    """
    fieldnames = ["Station_ID", "Easting", "Northing", "Elevation"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for pt in points:
            writer.writerow({
                "Station_ID": pt["id"],
                "Easting": pt["easting"],
                "Northing": pt["northing"],
                "Elevation": pt["elevation"]
            })