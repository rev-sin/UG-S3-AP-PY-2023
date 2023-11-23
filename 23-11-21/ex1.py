class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Project:
    def __init__(self, i_mark, v_mark):
        self.imp_mark = i_mark
        self.viva_mark = v_mark


class Student(Person, Project):
    def __init__(self, fname, lname, r, im, v):
        Person.__init__(self, fname, lname)
        Project.__init__(self, im, v)
        self.roll = r

    def printdetails(self):
        print(self.firstname, self.lastname, self.roll, self.imp_mark, self.viva_mark)


s1 = Student("rev", "sin", 149, 20, 5)
s1.printdetails()
