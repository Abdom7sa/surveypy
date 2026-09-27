class HelmertTransformation2D:
    def __init__(self):
        self.a, self.b = 1.0, 0.0
        self.tx, self.ty = 0.0, 0.0

    def fit_control_points(self, source_pts, target_pts):
        n = len(source_pts)
        if n < 2:
            raise ValueError("يلزم نقطتان معلومتان كحد أدنى.")

        sum_x, sum_y = sum(p[0] for p in source_pts), sum(p[1] for p in source_pts)
        sum_X, sum_Y = sum(p[0] for p in target_pts), sum(p[1] for p in target_pts)

        mx, my = sum_x / n, sum_y / n
        mX, mY = sum_X / n, sum_Y / n

        num_a, num_b, denom = 0.0, 0.0, 0.0
        for (x, y), (X, Y) in zip(source_pts, target_pts):
            dx, dy = x - mx, y - my
            dX, dY = X - mX, Y - mY
            num_a += dx * dX + dy * dY
            num_b += dx * dY - dy * dX
            denom += dx**2 + dy**2

        self.a = num_a / denom
        self.b = num_b / denom
        self.tx = mX - self.a * mx + self.b * my
        self.ty = mY - self.b * mx - self.a * my

    def transform(self, x, y):
        X = self.tx + self.a * x - self.b * y
        Y = self.ty + self.b * x + self.a * y
        return round(X, 3), round(Y, 3)