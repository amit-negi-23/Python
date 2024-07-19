# Practice Question 

# Write a program to ask the user to enter names of their 3 favorite movies & store them in a list.

movies = []
movies.append(input("Enter 1st movie name :"))
movies.append(input("Enter 2nd movie name :"))
movies.append(input("Enter 3rd movie name :"))

print(movies)


# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

list1 = [1, 2, 3, 2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):  # Here == is comparing the inner value only , not comparing the address ref 
    print("palidrome")
else:
    print("NOT palidrome")
    
    
# Note : if you want to compare the address ref use  ( is )
print(copy_list1 is list1)