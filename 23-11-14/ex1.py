class Student:
    college_name = "Amrita Vishwa Vidyapeetham"

    def __init__(self):
        self.name = input()
        self.roll = int(input())

    def display(self):
        print(self.college_name, self.name, self.roll)


s1 = Student()
s1.display()

Student.college_name = "PSG Tech"

s2 = Student()
s2.display()
s1.display()
