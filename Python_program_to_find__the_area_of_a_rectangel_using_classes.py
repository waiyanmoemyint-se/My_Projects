#python program to find the area of triangle

class rectangle():
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length  = length

    def Area(self):
        return self.breadth*self.length

a  = int(input("Enter a breadth number"))
b  = int(input("Enter a length number"))

obj = rectangle(a,b)
print("Area of the rectangle is  ",obj.Area())
