'''
Q Create a RectangleGeometry class which takes in length and breadth as initialize parameter. Make two methods getArea and getPerimeter inside this class.
Which when invoked returns area and perimeter of each rectangle instance.
'''

class RectangleGeometry:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def getArea(self):
        return self.length*self.breadth

    def getPerimeter(self):
        return 2*self.length+2*self.breadth


s= RectangleGeometry(2,3)
print(s.getArea())
print(s.getPerimeter())

