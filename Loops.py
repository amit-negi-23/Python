# while loop Practice Question


# PQ 3: Print a multiplication table of a number n.
n= int(input("Create multiplication table of :"))
k = 1
while k<=10:
    print(n*k)
    k+=1


# PQ 4: Print the element of following list using a loop
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(num):
    print(num[idx])
    idx +=1