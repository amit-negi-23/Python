#Practice Question
    
# WAP to find the greatest of 4 numbers entered by user.

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))
num4 = int(input("enter fourth number :"))

if(num1>num2 and num1>num3 and num1>num4):
    print("first number is largest =",num1)
elif(num2>num3 and num2>num4):
    print("second number is largest =",num2)
elif(num3>num4):
    print("third number is largest =",num3)
else:
    print("fourth number is largest =",num4)
    