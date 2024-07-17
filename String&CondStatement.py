#Practice Question

# WAP to check if a number enter by user is even or odd

num = int(input("Enter a number : "))

if(num%2==0):
    print("Even number", num)
else:
    print("Odd number", num)
    
    
    
# WAP to find the greatest of 3 numbers entered by user.

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))

if(num1>num2 and num1>num3):
    print("first number is largest =",num1)
elif(num2>num3):
    print("second number is largest =",num2)
else:
    print("third number is largest =",num3)