class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        try:
            a = (y1 - y0) / (x1 - x0)
        except:
            a = 0
        b = y0 - (a * x0)

        for xy in coordinates:
            x, y = xy
            if y != a*x + b:
                return False

        return True
