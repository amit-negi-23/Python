# while loop Practice Question

# PQ 5: 
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(num):
    if (num[i] == x):
        print("Found at idx ", i)
    else:
        print("Finding..")
    i+=1