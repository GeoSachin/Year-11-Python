import math
import turtle

Side1 = int(input("What is the length of side 1? "))
Side2 = int(input("What is the length of side 2? "))
Side3 = int(input("What is the length of side 3? "))


def Checker():
    if TriangleChecker() == "false":
        print("This is a not a triangle")
    else:
        if EquilateralChecker() == "Equilateral":
            print("Equilateral")
        if ScaleneChecker() == "Scalene":
            print("Scalene")
        elif (
            Side1 == Side2 != Side3
            or Side2 == Side3 != Side1
            or Side3 == Side1 != Side2):
            return "Isosceles"


def TriangleChecker():
    if Side1 + Side2 < Side3 or Side2 + Side3 < Side1 or Side1 + Side3 < Side2:
        return "false"
    else:
        return "true"


def EquilateralChecker():
    if Side1 == Side2 and Side2 == Side3:
        return "Equilateral"


def ScaleneChecker():
    if Side1 != Side2 and Side2 != Side3 and Side3 != Side1:
        return "Scalene"


Checker()
A = round(
    math.degrees(math.acos((Side2**2 + Side3**2 - Side1**2) / (2 * Side2 * Side3))), 2)
print(A)
B = round(
    math.degrees(math.acos((Side3**2 + Side1**2 - Side2**2) / (2 * Side3 * Side1))), 2)
print(B)
C = round(
    math.degrees(math.acos((Side1**2 + Side2**2 - Side3**2) / (2 * Side1 * Side2))), 2)
print(C)

turtle.forward(Side1 * 10)
turtle.left(180 - C)
turtle.forward(Side2 * 10)
turtle.left(180 - A)
turtle.forward(Side3 * 10)
