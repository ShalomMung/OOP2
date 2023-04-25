class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2

if __name__ == "__main__":
    l1 = Line(1, 2)
    p1 = Parabola(1, 2, 3)
    