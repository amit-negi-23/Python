# Set Method
collection = set()

# set.add(el)
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("radha") #string added
collection.add((79, 89, 99)) #tuple added
#collection.add([1,2])  # can not add list

print(collection)



# set.remove(el)
collection.remove(2) 
print(collection)


# set.clear()
print("collection len", len(collection))
collection.clear()
print("collection len", len(collection))


# set.pop()

words = { "a", "b", "c", "d"}
print(words)
print("pop val :",words.pop())
print(words)
