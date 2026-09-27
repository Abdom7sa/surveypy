import csv
import math
from reports.builder import StepReportBuilder

class TraverseProcessor:
    def __init__(self, start_e=0.0, start_n=0.0):
        self.start_e = start_e
        self.start_n = start_n
        self.distances = []
        self.azimuths = []
        self.adjusted_coords = []
        self.reporter = StepReportBuilder(title="تقرير ضبط الترافيرس المغلق")

    def load_from_csv(self, filename="data.csv"):
        self.distances.clear()
        self.azimuths.clear()
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader, start=2):
                dist = float(row["Distance"])
                az = float(row["Azimuth"])
                if dist <= 0:
                    raise ValueError(f"خطأ في السطر {idx}: المسافة يجب أن تكون موجبة.")
                if not (0 <= az <= 360):
                    raise ValueError(f"خطأ في السطر {idx}: الانحراف بين 0° و 360°.")
                self.distances.append(dist)
                self.azimuths.append(az)

    def process_bowditch_adjustment(self):
        total_length = sum(self.distances)
        delta_e = [d * math.sin(math.radians(az)) for d, az in zip(self.distances, self.azimuths)]
        delta_n = [d * math.cos(math.radians(az)) for d, az in zip(self.distances, self.azimuths)]
        w_e, w_n = sum(delta_e), sum(delta_n)

        linear_error = math.sqrt(w_e**2 + w_n**2)
        accuracy_ratio = total_length / linear_error if linear_error != 0 else float("inf")

        curr_e, curr_n = self.start_e, self.start_n
        self.adjusted_coords = [(curr_e, curr_n)]

        for i in range(len(self.distances)):
            corr_e = delta_e[i] - (self.distances[i] / total_length) * w_e
            corr_n = delta_n[i] - (self.distances[i] / total_length) * w_n
            curr_e += corr_e
            curr_n += corr_n
            self.adjusted_coords.append((curr_e, curr_n))

        area_m2, area_ha = self.calculate_area()
        summary_data = {
            "error": linear_error,
            "accuracy": accuracy_ratio,
            "area_m2": area_m2,
            "area_ha": area_ha
        }
        return summary_data

    def calculate_area(self):
        n = len(self.adjusted_coords) - 1
        area = 0.0
        for i in range(n):
            j = i + 1
            area += self.adjusted_coords[i][0] * self.adjusted_coords[j][1]
            area -= self.adjusted_coords[j][0] * self.adjusted_coords[i][1]
        area_m2 = abs(area) / 2.0
        return area_m2, area_m2 / 10000.0