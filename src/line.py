from src.point import Point


class Line():

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    # TODO: DEPRECATED
    @staticmethod
    def new_from_points(p1: Point, p2: Point):
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = -b * p1.y - a * p1.x
        return Line(a, b, c)

    # TODO: DEPRECATED
    @staticmethod
    def new_from_function(k: int, m: int):
        a = k
        b = -1
        c = m
        return Line(a, b, c)

    @staticmethod
    def is_parallel(l1, l2):
        return l1.a * l2.b == l2.a * l1.b

    @staticmethod
    def get_intersect(l1, l2):
        """
        If the lines intersect, return point, otherwise false
        """
        if not Line.is_parallel(l1, l2):
            return False

        y = (l2.a * l1.c - l1.a * l2.c) / (l1.a * l2.c - l2.a * l1.b)

        x = (-l1.b * y - l1.c) / l1.a

        return Point(x, y)


class LineBuilder():

    @staticmethod
    def from_points(p1: Point, p2: Point):
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = -b * p1.y - a * p1.x
        return Line(a, b, c)

    @staticmethod
    def from_function(k: int, m: int):
        a = k
        b = -1
        c = m
        return Line(a, b, c)

    @staticmethod
    def from_segment(segment):
        return LineBuilder.from_points(segment.a, segment.b)
