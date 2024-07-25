# If no file is present , then new file will be created
file = open("sample.txt", "w")

data = file.write("I am Learning Python from Youtube")
print(data)

file.close()