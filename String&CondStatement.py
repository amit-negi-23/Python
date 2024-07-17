msg = "i am learning Python myself"
print(msg)
print(len(msg))


#String Functions

# 1  msg.endswith("elf")     # return True or False
print(msg.endswith("elf"))  #True
print(msg.endswith("amit")) #False


# 2  msg.capitalize()       # capitalize  1st char
print(msg.capitalize())


# 3  msg.replace("old", "new")     # replace all occurrences of old
print(msg.replace("Python", "React"))


# 4  msg.find(word)    # return 1st index of 1st occurrer
print(msg.find("a"))
              

# 5  msg.count()       # count the occurrences of substr
print(msg.count("n"))