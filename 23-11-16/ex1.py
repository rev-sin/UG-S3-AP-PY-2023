class Employee:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def display(self):
        print(self.name, self.age)


e1 = Employee("rev", 19)
e1.display()
