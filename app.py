import math

from check import print_rectangle_properties

class Rectangle:
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

def main():
    
    a = Rectangle(9.0, 12.0)
    print_rectangle_properties(a)
    b = Rectangle(17.0, 13.0)
    print_rectangle_properties(b)
    c = Rectangle(30.0, 45.0)
    print_rectangle_properties(c)

if __name__ == "__main__":
    main()
