# Practice Question 

# PQ 1: Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(num):
    if(num == 0):
        return 0
    return num + calc_sum(num-1)
    
print(calc_sum(12))



# PQ 2: Write a recursive function to print all elements in a list.

cities = ["delhi", "mumbai", "hyderabad", "chennai", "gurgaon", "noida"]

def show_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    show_list(list, idx+1)
    
show_list(cities)