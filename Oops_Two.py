# Practice Question

# PQ 1:
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def Area(self):
        return 3.14 * (self.radius)**2

    def Perimeter(self):
        return 2 * 3.14 * self.radius


c1 = Circle(7)
print(c1.Area())
print(c1.Perimeter())


# PQ 2:

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("Engineer", "IT", "75,000")
        self.name = name
        self.age = age


engg1 = Engineer("Rohit", 25)
print(engg1.name)
engg1.showDetails()