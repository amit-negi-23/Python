# PQ 3
word = "learning"
with open("practice.txt","r") as file:
    data = file.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")
        
    file.close()   