class Student:
    
    def __init__(self, name, email, age, phone):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
        
    def welcome(self):
        print("Welcome to Python,", self.name)
    
    def get_age(self):
        return self.age



s1 = Student("Amit", "amit@gmail.com", 24, 9632587415)
s1.welcome()
print(s1.get_age())