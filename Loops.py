# Practice Question 

# PQ 1: WAP to find the sum of first n number. (using while)

n = int(input("Enter number :"))

sum = 0
i = 1
while i<=n :
    sum+=i
    i+=1
print("sum using while loop =",sum)



# PQ 2: WAP to find the sum of first n number. (using for)

n = int(input("Enter number :"))
sum = 0
for i in range(n+1):
    sum+=i
print("sum using for loop =",sum)



# PQ 3: WAP to find the factorial of first n numbers (using while)

n = int(input("Enter number :"))
fac = 1

i = 1
while i<=n:
    fac*=i
    i+=1
print("factorial using while loop =",fac)



# PQ 4: WAP to find the factorial of first n numbers (using for)

n = int(input("Enter number to find factorial :"))
fac =1
for i in range(1,n+1):
    fac*=i
print("factorial using for loop =",fac)