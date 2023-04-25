import numpy as np
    
class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
    
    def __call__(self, x):
        return self.c0 + self.c1 * x + self.c2 * x**2

    def print_point(self, L, R, n):
        print("Parabel")
        print("x\tf(x)")
        for x in np.linspace(L, R, n):
            print(f"{x:.1f}\t{self(x):.1f}")

class Line(Parabola):
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
        self.c2 = 0

if __name__ == "__main__":
    l1 = Line(1, 2)
    p1 = Parabola(1, 2, 3)

    #x = 2
    #print(f"Line 1 evaluate at {x}: {l1(x)}")
    #print(f"Parabola 1 evaluate at {x}: {p1(x)}")

    l1.print_point(0, 10, 4)
    p1.print_point(0, 10, 4)
