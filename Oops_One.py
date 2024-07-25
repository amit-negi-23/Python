class Student:
    
    def __init__(self, name, email, age, phone):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
        


s1 = Student("Amit", "amit@gmail.com", 24, 9632587415)
print(s1.name, s1.email)

s2 = Student("Rohit", "rohit@gmail.com", 28, 9874563214)
print(s2.name, s2.email)