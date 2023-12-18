class Compute:
    def sum(self, x=None, y=None, z=None):
        if x is not None and y is not None and z is not None:
            return x + y
        elif x is None and y is not None and z is not None:
            return z + y


obj = Compute()
print("sum Value:", obj.sum(2, 5, 1))
print("sum Value:", obj.sum(3, 10))
