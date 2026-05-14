class Circle:
        
    def __init__(self, radius):
        self.radius = radius
        print (f"The circle has {self.radius} radius.")

    def get_area(self):
        area = ((3.14 * self.radius) * self.radius)

        return area


circle_1 = Circle(9)
result=circle_1.get_area()
print(f"The cirlce has a {result} area.")