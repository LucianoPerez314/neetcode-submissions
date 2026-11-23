class CountSquares:

    def __init__(self):
        # raw set of points
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) not in self.points:
            self.points[(x, y)] = 1
        else:
            self.points[(x, y)] += 1

        

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        num = 0
        for x2, y2 in self.points.keys():
            # ignore point passed in. 
            if (x1, y1) == (x2, y2): 
                continue
            dx = x2 - x1
            dy = y2 - y1
            # if two points make a valid square diagonal check if there are points on the other two squares of the diagonal
            if abs(dx) == abs(dy) and (x1, y2) in self.points and (x2, y1) in self.points:
                num += self.points[(x2, y2)] * self.points[(x2, y1)] *self.points[(x1, y2)]
        return num

