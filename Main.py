import Shapes as sh
import time as t

class PolyMain:

    n = 0
    sl = 0
    r = 0

    def __init__(self, n, sl, r):
        self.n = n
        self.sl = sl
        self.r = r
        self.mainMenu()

    def mainMenu(self):
        print("Choose shape type:")
        print("1. Regular polygon")
        print("2. Irregular polygon")
        print("3. Cricle")
        print("4. Draw a star!")
        print("5. Quit")
        shType = float(input("(1/2/3/4): "))

        if shType == 1:
            self.regMenu()
        if shType == 2:
            self.irregMenu()
        if shType == 3:
            self.circleMenu()
        if shType == 4:
            self.starMenu()
        if shType == 5:
            print("\n  ####       ####       ####     ######     ######     ##      ##   ########")
            t.sleep(0.25)
            print("##    ##   ##    ##   ##    ##   ##    ##   ##    ##    ##    ##    ##")
            t.sleep(0.25)
            print("##         ##    ##   ##    ##   ##    ##   ##    ##     ##  ##     ##")
            t.sleep(0.25)
            print("##  ####   ##    ##   ##    ##   ##    ##   ######        ####      ########")
            t.sleep(0.25)
            print("##    ##   ##    ##   ##    ##   ##    ##   ##    ##       ##       ##")
            t.sleep(0.25)
            print("##    ##   ##    ##   ##    ##   ##    ##   ##    ##       ##       ##")
            t.sleep(0.25)
            print("  ####       ####       ####     ######     ######         ##       ########")
            t.sleep(0.25)
            quit()
        else:
            ()

    def regMenu(self):
        n = float(input("\nHow many sides?\n"))
        sl = float(input("How long are the sides?\n"))
        pol = sh.RegPol(n, sl)
        pol.go()

    def irregMenu(self):
        print("\nChoose a shape:")
        print("1. Triangle")
        print("2. Quadrilateral")
        irreg = float(input("(1/2): "))

        if irreg == 1:
            print("\nWhat information do you have?")
            print("1. Three sides")
            print("2. One angle and two adjacent sides")
            print("3. One angle, the opposite side and one other side")
            print("4. Two angles and the side between them")
            print("5. Two angles and one of their opposites")
            print("6. Three angles")
            triChoice = float(input("(1/2/3/4/5/6): "))

            if triChoice == 1:
                a = float(input("\nFirst side: "))
                b = float(input("Second side: "))
                c = float(input("Third side: "))
                triangle = sh.Triangle(a, b, c, 0, 0, 0)
                triangle.threeSides()
                triangle.go()

            if triChoice == 2:
                A = float(input("\nAngle: "))
                b = float(input("First adjacent side: "))
                c = float(input("Second adjacent side: "))
                triangle = sh.Triangle(0, b, c, A, 0, 0)
                triangle.oneAngleAdj()
                triangle.go()

            if triChoice == 3:
                A = float(input("\nAngle: "))
                a = float(input("Opposite side: "))
                b = float(input("adjacent side: "))
                triangle = sh.Triangle(a, b, 0, A, 0, 0)
                triangle.oneAngleOpp()
                triangle.go()

            if triChoice == 4:
                A = float(input("\nFirst angle: "))
                B = float(input("Second angle: "))
                c = float(input("Side in between: "))
                triangle = sh.Triangle(0, 0, c, A, B, 0)
                triangle.oneSideBetween()
                triangle.go()

            if triChoice == 5:
                A = float(input("\nFirst angle: "))
                B = float(input("Second angle: "))
                a = float(input("Opposite side: "))
                triangle = sh.Triangle(a, 0, 0, A, B, 0)
                triangle.oneSideAdj()
                triangle.go()

            if triChoice == 6:
                print("\nCan't help ya, buddy")

        if irreg == 2:
            print("We only have rectangles...")
            print("1. Rectangle")
            quadChoice = float(input("(1): "))

            if quadChoice == 1:
                a = float(input("First side length: "))
                b = float(input("Second side length: "))
                quad = sh.Quadrilateral(a, b, 0, 0, 0, 0, 0, 0)
                quad.rect()
                quad.go()

    def circleMenu(self):
        r = float(input("\nWhat's the radius of the circle?\n"))
        circle = sh.Circle(r)
        circle.go()

    def starMenu(self):
        n = int(input("How many points will your star have?\n"))
        star = sh.Star(n)
        star.turtle()


PolyMain(0, 0, 0)
