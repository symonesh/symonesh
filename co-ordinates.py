class location:
    def __init__(self,x=0,y=0):
       self.x=x
       self.y=y
    def move(self,x,y):
        self.x+=x
        self.y+=y
        self.cord=(self.x,self.y)
    def __add__(self, p):
        return location(self.x+p.x,self.y+p.y)
    def __sub__(self,p):

        return location(self.x-p.x,self.y-p.y)
    def length(self):
        import math
        return math.sqrt(self.x**2+self.y**2)
    def __eq__(self,p):

        return self.x==p.x and self.y==p.y
    def __gt__(self,p):
        return self.length() > p.length()
    def __ge__(self,p):
        return self.length() >= p.length()

    def __le__(self,p):
        return self.length() <= p.length()

    def __lt__(self,p):
        return self.length() < p.length()
    def __mul__(self,p):
        return location(self.x * p.x, self.y * p.y)
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
p1=location(4,5)
p2=location(9,10)
p3=location(1,4)
p4=location(1,9)
print(p1+p2)
print(p1>p2)
print(p3<p4)
print(p4<=p2)
print(p4>=p2)
print(p3-p1)
print(p1*p2)