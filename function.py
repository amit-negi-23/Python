#practice question

# PQ 1: WAF to print the length of a list (list is the parameter)
cities = ["delhi", "mumbai", "hyderabad", "chennai", "koltata", "bengaluru", "noida ", "gurgaon"]

fruits = ["Custard Apple", "Pomegranate", "Orange", "Papaya", "Strawberry"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(fruits)


# PQ 2: WAF to print the elements of a list in a single line. (list is the parameter)

def print_list(list):
    for item in list:
        print(item, end=", ")

print_list(cities)