import numpy as np

# Task 1: Create a 3x3 matrix and find its determinant
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

determinant = np.linalg.det(matrix)
print(f"Determinant of the matrix: {determinant}")


import math

# Task 1: 2D Array and Upper Triangle
def display_upper_triangle(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Upper Triangle:")
display_upper_triangle(matrix)

# Task 2: Rectangle Class
class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.area = 0

    def set(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))

    def calculate(self):
        self.area = self.length * self.breadth
        print("Area of Rectangle:", self.area)

class Imain:
    @staticmethod
    def main():
        rect = Rectangle()
        rect.set()
        rect.calculate()

Imain.main()

# Task 3: Quadratic Equation
class Quadratic:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.x1 = 0
        self.x2 = 0

    def input_values(self):
        self.a = int(input("Enter a: "))
        self.b = int(input("Enter b: "))
        self.c = int(input("Enter c: "))

    def calculate(self):
        d = (self.b ** 2) - (4 * self.a * self.c)
        if d >= 0:
            self.x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            self.x2 = (-self.b - math.sqrt(d)) / (2 * self.a)
        else:
            print("No real roots")

    def display(self):
        print("Roots:", self.x1, self.x2)

class Imain:
    @staticmethod
    def main():
        quad = Quadratic()
        quad.input_values()
        quad.calculate()
        quad.display()

Imain.main()

# Task 4: Compare Two Rectangles
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = 0

    def compute_area(self):
        self.area = self.length * self.breadth

    def display_area(self):
        print("Area:", self.area)

rect1 = Rectangle(4, 5)
rect2 = Rectangle(6, 7)

rect1.compute_area()
rect2.compute_area()

rect1.display_area()
rect2.display_area()

if rect1.area > rect2.area:
    print("Rectangle 1 is larger")
else:
    print("Rectangle 2 is larger")

# Task 5: Factorial Calculation
class Factorial:
    def find_fact(self, n):
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

fact_obj = Factorial()
n = int(input("Enter a number: "))
print("Factorial:", fact_obj.find_fact(n))



# Task 2: Class to sum an integer array
class ArraySum:
    def __init__(self):
        self.sum = 0

    def Sum(self, a):
        self.sum = sum(a)
        return self.sum

# Main function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    obj = ArraySum()
    result = obj.Sum(arr)
    
    print(f"Sum = {result} & uk")