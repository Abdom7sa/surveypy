class GridLevelingEngine:
    def __init__(self, design_elevation):
        self.design_elevation = design_elevation
        self.grid_points = []

    def load_grid_data(self, grid_records):
        self.grid_points = grid_records

    def calculate_volumes(self, cell_width, cell_height):
        cell_area = cell_width * cell_height
        total_cut_vol = 0.0
        total_fill_vol = 0.0

        for pt in self.grid_points:
            diff = pt['RL'] - self.design_elevation
            if diff > 0:
                total_cut_vol += diff * cell_area
            else:
                total_fill_vol += abs(diff) * cell_area

        return {
            "cell_area": cell_area,
            "cut_volume": total_cut_vol,
            "fill_volume": total_fill_vol,
            "net_volume": total_cut_vol - total_fill_vol
        }