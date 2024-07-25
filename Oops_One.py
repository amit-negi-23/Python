# practice Question

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum =0
        for val in self.marks:
            sum+=val
        print("Hi",self.name, "Your avg score is :", sum/3)


s1 = Student("Amit Negi", [97, 92, 99])
s1.get_avg()


s1.hello()

# Update
s1.name="Rohit"
s1.get_avg()