"""
SurveyPy - GNSS & RTK Processing Engine
Handles GNSS quality control, elevation masks, and PDOP evaluations.
"""

class GNSSQualityControl:
    """كلاس التحقق من جودة رصد أجهزة GNSS / RTK"""

    def __init__(self, max_pdop=3.0, min_satellites=5, elevation_mask=15.0):
        self.max_pdop = max_pdop
        self.min_satellites = min_satellites
        self.elevation_mask = elevation_mask  # زاوية الحجب بالدرجات

    def evaluate_point_quality(self, pdop, sat_count, status="FIXED"):
        """تقييم صلاحية نقطة الرصد بناءً على المعايير الجيوديسية"""
        warnings = []

        if status.upper() != "FIXED":
            warnings.append(f"الحالة ليست FIXED (الحالة الحالية: {status})")

        if pdop > self.max_pdop:
            warnings.append(f"قيمة PDOP مرتفعة: {pdop:.2f} (الحد الأقصى: {self.max_pdop})")

        if sat_count < self.min_satellites:
            warnings.append(f"عدد الأقمار غير كافٍ: {sat_count} (الحد الأدنى: {self.min_satellites})")

        is_valid = len(warnings) == 0
        return {
            "is_valid": is_valid,
            "status": "مقبولة" if is_valid else "مرفوضة",
            "warnings": warnings
        }