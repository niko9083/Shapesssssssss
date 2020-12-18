import math
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def asin(x):
    return math.degrees(math.asin(x))
def acos(x):
    return math.degrees(math.acos(x))

from turtle import *

class RegPol:
    sl = 0
    n = 0

    def __init__(self, n, sl):
        self.n = n
        self.sl = sl

    def area(self):
        global A, b

        try:
            A = float(360 / self.n)
            B = float((180 - A) / 2)
        except:
            print("The side amount needs to be a number")
            quit()

        b = (sin(B) * self.sl) / sin(A)

        s = (self.sl + b + b) / 2
        triArea = math.sqrt(abs(s * (s - self.sl) * (s - b) * (s - b)))

        return triArea * self.n

    def circ(self):
        return self.sl * self.n

    def turtle(self):
        TurtleScreen._RUNNING = True
        hideturtle()
        delay(1)
        color("red", "yellow")

        penup()
        right(90)
        fd(b)
        left(90)

        pendown()
        begin_fill()
        for i in range(int(self.n)):
            try:
                fd(int(self.sl))
            except:
                print("Side length needs to be a number")
            left(A)
        end_fill()
        done()

    def go(self):
        print("Side count:", self.n)
        print("Side length:", self.sl)
        print("Area:", self.area())
        print("Circumference:", self.circ())
        self.turtle()


class Triangle:
    a = 0
    b = 0
    c = 0
    A = 0
    B = 0
    C = 0

    def __init__(self, a, b, c, A, B, C):
        self.a = a
        self.b = b
        self.c = c
        self.A = A
        self.B = B
        self.C = C

    def threeSides(self):
        self.A = acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        self.B = acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
        self.C = acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b))

    def oneAngleAdj(self):
        self.a = math.sqrt(self.b**2 + self.c**2 - cos(self.A) * 2 * self.b * self.c)
        self.B = acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))
        self.C = acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))

    def oneAngleOpp(self):
        self.B = asin((self.b * sin(self.A)) / self.a)
        self.C = 180 - (self.A + self.B)
        self.c = (self.a * sin(self.C)) / sin(self.A)

    def oneSideBetween(self):
        self.C = 180 - (self.A + self.B)
        self.a = (self.c * sin(self.A)) / sin(self.C)
        self.b = (self.a * sin(self.B)) / sin(self.A)

    def oneSideAdj(self):
        self.C = 180 - (self.A + self.B)
        self.b = (self.a * sin(self.B)) / sin(self.A)
        self.c = (self.a * sin(self.C)) / sin(self.A)

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(abs(s * (s - self.a) * (s - self.b) * (s - self.c)))

    def turtle(self):
        TurtleScreen._RUNNING = True
        hideturtle()
        delay(1)
        color("red", "yellow")

        penup()
        right(90)
        fd(self.b/2)
        right(90)
        fd(self.a/2)
        right(180)

        pendown()
        begin_fill()
        fd(int(self.b))
        left(int(180 - self.C))
        fd(int(self.a))
        left(int(180 -self. B))
        fd(int(self.c))
        end_fill()
        done()

    def go(self):
        print("\nSides:")
        print("    a:", self.a)
        print("    b:", self.b)
        print("    c:", self.c)
        print("Angles:")
        print("    A:", self.A, "degrees")
        print("    B:", self.B, "degrees")
        print("    C:", self.C, "degrees")
        print("Area:", self.area())
        self.turtle()

class Quadrilateral:
    a = 0
    b = 0
    c = 0
    d = 0
    A = 0
    B = 0
    C = 0
    D = 0

    def __init__(self, a, b, c, d, A, B, C, D):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def rect(self):
        self.c = self.a
        self.d = self.b
        self.A = 90
        self.B = 90
        self.C = 90
        self.D = 90
        global Area
        Area = self.a * self.b

    def turtle(self):
        TurtleScreen._RUNNING = True
        hideturtle()
        delay(1)
        color("red", "yellow")

        penup()
        left(90)
        fd(self.a / 2)
        left(90)
        fd(self.b / 2)
        left(90)

        pendown()
        begin_fill()
        fd(int(self.a))
        left(int(360 - self.A))
        fd(int(self.b))
        left(int(360 - self.B))
        fd(int(self.c))
        left(int(360 - self.C))
        fd(int(self.d))
        end_fill()
        done()

    def go(self):
        print("Angles:")
        print("    A:", self.A)
        print("    B:", self.B)
        print("    C:", self.C)
        print("    D:", self.D)
        print("Sides:")
        print("    a:", self.a)
        print("    b:", self.b)
        print("    c:", self.c)
        print("    b:", self.d)
        print("Area:", Area)
        self.turtle()


class Circle:
    r = 0

    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2

    def circ(self):
        return math.pi * (self.r * 2)

    def turtle(self):
        TurtleScreen._RUNNING = True
        hideturtle()
        delay(1)
        color("red", "yellow")

        penup()
        right(90)
        fd(self.r)
        left(90)

        pendown()
        begin_fill()
        circle(self.r)
        end_fill()
        done()

    def go(self):
        print("Radius:", self.r)
        print("Diameter:", self.r * 2)
        print("Area:", self.area())
        print("circumference:", self.circ())
        self.turtle()


class Star:
    n = 0

    def __init__(self, n):
        self.n = n

    def turn(self):
        return float(720 / self.n)

    def turtle(self):
        if self.n % 2 == 0:
            print("\nSadly, there needs to be an odd number of points...")
        else:
            TurtleScreen._RUNNING = True
            hideturtle()
            delay(1)
            color("red", "yellow")

            penup()
            back(1000 / self.n)
            left(90)
            fd(500 / self.n)
            right(90)

            pendown()
            begin_fill()
            for i in range(self.n):
                fd(2000 / self.n)
                right(self.turn())
            end_fill()
            done()
