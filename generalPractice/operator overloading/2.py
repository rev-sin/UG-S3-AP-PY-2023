class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return self.a, self.b

    def __add__(self, other):
        temp = Point(0, 0)
        temp.a = self.a + other.a
        temp.b = self.b + other.b
        return temp

    def displaypoint(self):
        print(self.a, self.b)


Ob1 = Point(1, 2)
Ob2 = Point(2, 3)
Ob3 = Ob1 + Ob2
Ob3.displaypoint()
