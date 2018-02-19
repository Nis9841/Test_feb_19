'''
 Q: Create a class Circle which has a class variable PI with the value=22/7.
 Make two methods getArea and getCircumference inside this Circle class.
  Which when invoked returns area and circumference of each circle instances.
'''
class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return Circle.pi*self.radius**2

    def getCircumference(self):
        return 2*Circle.pi*self.radius


s= Circle(5)
print(s.getArea())
print(s.getCircumference())