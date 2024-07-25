with open("sample.txt", "r") as file:
    data = file.read()
    print(data)
    file.close()


with open("sample.txt", "w") as file:
    file.write("Learning Python")
    file.close()