import math

def calculate_forward_intersection(e_a, n_a, az_a, e_b, n_b, az_b):
    rad_a = math.radians(az_a)
    rad_b = math.radians(az_b)
    numerator = (e_b - e_a) * math.cos(rad_b) - (n_b - n_a) * math.sin(rad_b)
    denominator = math.sin(rad_a - rad_b)

    if abs(denominator) < 1e-7:
        raise ValueError("الخطوط متوازية تقريباً ولا يوجد نقطة تقاطع محددة.")

    s_a = numerator / denominator
    e_c = e_a + s_a * math.sin(rad_a)
    n_c = n_a + s_a * math.cos(rad_a)
    return round(e_c, 3), round(n_c, 3)