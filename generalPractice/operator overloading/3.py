class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return self.a, self.b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b


Ob1 = Point(1, 2)
Ob2 = Point(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)
