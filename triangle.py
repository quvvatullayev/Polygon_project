import math
class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a=a 
        self.b=b
        self.c=c

    def is_valid(self):
        if self.a + self.b > self.c and self.c + self.b > self.a and self.c + self.a > self.b and self.a>0 and self.b>0 and self.c>0 :
            return True
        return False
    def get_type(self):
        s = ''
        if self.a ** 2 + self.b ** 2 == self.c ** 2 :
            s += 'based on angles -> right, ' # one angle is 90

        elif self.a ** 2 + self.b ** 2 > self.c **2 :
            s += 'based on angles -> acute, ' # each angle is < 90

        elif self.a ** 2 + self.b ** 2 < self.c **2 :
            s += 'based on angles -> obtuse, ' # one angle is > 90

        elif self.a == self.b or self.a == self.c or self.c == self.b :
            s += 'based on sides -> Isoscelec, '  # Length of two sides are equal

        elif self.a == self.b and self.a == self.c and self.c == self.b :
            s += 'based on sides -> Equilateral, ' # Length of all sides are equal

        elif self.a != self.b and self.a != self.c and self.c != self.b :
            s += 'based on sides -> Scalene, ' # Length of all sides are different

        elif self.c**2 == self.a**2 + self.b**2:
            return 'right angle'

        elif self.b == self.c:
            return 'equilateral'
            
        elif self.c == self.a == self.b:
            return "equal side"

    def perimeter(self):
        if self.is_valid():
            return self.a+self.b+self.c
        return 0

    def area(self):
        if self.is_valid():
            p = (self.a + self.b + self.c)/2
            return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
