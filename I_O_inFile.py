#Pq 2: 
with open("practice.txt", "r") as file:
    data = file.read()
    file.close()
    
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as file:
    file.write(new_data)
    file.close()