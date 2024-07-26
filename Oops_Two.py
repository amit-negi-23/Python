# Polymorphism : 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +",self.img, "j")
        
    def __add__(self, newNum):
        newReal = self.real + newNum.real
        newImg = self.img + newNum.img
        return Complex(newReal, newImg)
    
    def __sub__(self, newNum):
        newReal = self.real - newNum.real
        newImg = self.img - newNum.img
        return Complex(newReal, newImg)
    
num1 = Complex(2, 3)
num1.showNumber()

num2 = Complex(4, 5)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()