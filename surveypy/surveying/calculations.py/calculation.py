from surveying.calculations import calculate_distance

print("================================")
print("          SurveyPy")
print("Surveying & Geodesy Software")
print("================================")

# نقطتين تجريبيتين
e1, n1 = 1000.0, 1000.0
e2, n2 = 1030.0, 1040.0

# حساب المسافة
dist = calculate_distance(e1, n1, e2, n2)

print(f"Distance between points = {dist:.2f} m")