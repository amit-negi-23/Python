# Inheritance: When one class (child/ derived) derives the properties & method of another class (parent/ base).

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name


car1 = ToyotaCar("Fortuner")
print(car1.name)
car1.start()