
'''
This module provides the access to the geometrical objects (points, lines, two dimention shapes).
'''

# Copyright information.
__author__ = 'MengZe'
__copyright__ = '(C) MengZe 2020-present'
__license__ = 'Public Domain'
__version__ = '1.0.0'

import math
import matplotlib.pyplot as plt


class Point(object):
    '''
    Create a point object with two coordinate arguments x and y.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def coordinate(self):
        '''
        Return the coordinate of the point.
        '''
        return '({},{})'.format(self.x, self.y)
    
    def __add__(self, p1):
        return '({},{})'.format((self.x + p1.x), (self.y + p1.y))
    
    def __sub__(self, p1):
        return '({},{})'.format((self.x - p1.x), (self.y - p1.y))
    
    def plot(self):
        '''
        Plot the point on a graph.
        '''
        plt.title("Geometry")
        plt.grid(True)  
        plt.ylabel('y-axis')
        plt.xlabel('x-axis')
        plt.plot([self.x], [self.y], 'ro')
        plt.axis([0, 10, 0, 10])
        plt.show()
    
    def rotate(self, center, degree):
        '''
        Return the final coordinate of the point after rotation.

        The center of rotation is 0 if no argument is passed.
        '''
        pass


class Line(Point):
    '''
    Create a line object with four coordinate arguments x, y, x1, y1.
    '''
    def __init__(self, x, y, x1, y1):
        super().__init__(x, y)
        self.x1 = x1
        self.y1 = y1

    def coordinate(self):
        '''
        Return a tuple consisting two coordinates (point one, point two).
        '''
        return ('({},{})'.format(self.x, self.y)), ('({},{})'.format(self.x1, self.y1))

    
    def length(self):
        '''
        Return the length (i.e distance between the two points) of the line
        '''
        return round(math.sqrt((self.x1-self.x)**2 +(self.y1-self.y)**2), 5)
    
    def mid(self):
        '''
        Return the mid-point coordinate of the line
        '''
        return '({},{})'.format((self.x + self.x1)/2, (self.y + self.y1)/2)
    
    def gradient(self):
        '''
        Return the gradient (slope) of the line
        '''
        try:
            m = (self.y1 - self.y)/(self.x1 - self.x)
        except:
            return 0
        return m
    
    def inclination(self):
        '''
        Return the angle of inclination.

        The value is returned in degrees.
        '''
        return math.degrees(math.atan(self.gradient()))
    
    def equation(self):
        '''
        Return the Point-Slope equation of the line in the form " y - y1 = m(x - x1) ".
        '''
        return "y - {} = {}(x - {})".format(self.y, round(self.gradient(), 2), self.x)
    
    def rotate(self, center, degree):
        '''
        Return the final coordinates of the point after rotation.

        The center of rotation is 0 if no argument is passed.
        '''
        pass
    
    def plot(self):
        '''
        Plot the line on a graph.
        '''
        plt.title("Geometry")
        plt.grid(True)  
        plt.ylabel('y-axis')
        plt.xlabel('x-axis')
        plt.plot([self.x, self.x1], [self.y, self.y1])
        plt.axis([0, 10, 0, 10])
        plt.show()
    
  

class Dimention2(object):
    '''
    Create a two dimentional shape object with six coordinate arguments x, y, x1, y1, x2, y2.
    '''
    def __init__(self, x, y, x1, y1, x2, y2, x3 = None, y3 = None, x4 = None, y4 = None, x5 = None, y5 = None ):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.x5 = x5
        self.y5 = y5

        if (x3 != None and y3 == None) or (x4 != None and y4 == None) or (x5 != None and y5 == None):
            self.enclosed = False
        else:
            self.enclosed = True

    def coordinate(self):
        '''
        Return a tuple consisting three or more coordinates (point one, point two).
        '''
        return ('({},{})'.format(self.x, self.y)), ('({},{})'.format(self.x1, self.y1)), ('({},{})'.format(self.x2, self.y2)),('({},{})'.format(self.x3, self.y3)), ('({},{})'.format(self.x4, self.y4)), ('({},{})'.format(self.x5, self.y5))

    def shape(self):
        '''
        Return the shape of the 2-Dimentional shape.
        '''
        if self.enclosed == True:
            if self.y3 == None:
                # s stands for shape
                self.s = "triangle"
                return "Triangle"
            elif self.y4 == None:
                l0 = Line(self.x, self.y, self.x1, self.y1)
                l1 = Line(self.x1, self.y1, self.x2, self.y2)
                l2 = Line(self.x2, self.y2, self.x3, self.y3)
                l3 = Line(self.x3, self.y3, self.x, self.y)
                if (l0.gradient() == l2.gradient() and l1.gradient() * l3.gradient() == 0) or (l0.gradient() * l2.gradient() == 0 and l1.gradient() == l3.gradient()): 
                    if l0.length() == l1.length() == l2.length() == l3.length():
                        self.s = "square"
                        return "Square"
                    else:
                        self.s = "rectangle"
                        return "Rectangle"
                else:
                    self.s = "quadrilateral"
                    return "Quadrilateral"
            elif self.y5 == None:
                self.s = "pentagon"
                return "Pentagon"
            else:
                self.s = "hexagon"
                return "Hexagon"
        else:
            return "Invalid Shape"
        
    def area(self):
        self.shape()
        if self.s == 'triangle':
            l0 = Line(self.x, self.y, self.x1, self.y1)
            l1 = Line(self.x, self.y, self.x2, self.y2)
            l2 = Line(self.x1, self.y1, self.x2, self.y2)
            a = int(l0.length())
            b = int(l1.length())
            c = int(l2.length())
            # Heron's formula
            p = int((a + b + c) / 2) 
            area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
            return area
        elif self.s == 'square':
            l0 = Line(self.x, self.y, self.x1, self.y1)
            area = (l0.length()) ** 2
            return area
        elif self.s == 'rectangle':
            l0 = Line(self.x, self.y, self.x1, self.y1)
            l1 = Line(self.x1, self.y1, self.x2, self.y2)
            l2 = Line(self.x, self.y, self.x3, self.y3)
            # multiply the length of two perpendicular line
            if l0.gradient() == l1.gradient():
                area = l0.length() * l2.length()
            else:
                area = l0.length() * l1.length()
            return area
        else:
            return 'Unknown'
    
    def plot(self):
        '''
        Plot the shape on a graph.
        '''
        plt.title("Geometry")
        plt.grid(True)  
        plt.ylabel('y-axis')
        plt.xlabel('x-axis')
        if self.x3 == None:
            plt.plot([self.x, self.x1, self.x2, self.x], [self.y, self.y1, self.y2, self.y], 'r-')
        elif self.x4 == None:
            plt.plot([self.x, self.x1, self.x2, self.x3, self.x], [self.y, self.y1, self.y2, self.y3, self.y], 'r-')
        elif self.x5 == None:
            plt.plot([self.x, self.x1, self.x2, self.x3, self.x4, self.x], [self.y, self.y1, self.y2, self.y3, self.y4, self.y], 'r-')
        else:
            plt.plot([self.x, self.x1, self.x2, self.x3, self.x4, self.x5, self.x], [self.y, self.y1, self.y2, self.y3, self.y4, self.y5, self.y], 'r-')

        plt.axis([0, 10, 0, 10])
        plt.show()

if __name__ == '__main__':
    l1 = Line(1,1,3,2)
    l2 = Line(2,3,5,10)
    p1 = Point(1,2)

    s1 = Dimention2(1,1,5,5,10,1)
    print(s1.plot())




