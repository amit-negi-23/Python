class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = name
        
p1 = Person()
p1.changeName("Rahul")
print(p1.name)
print(Person.name)