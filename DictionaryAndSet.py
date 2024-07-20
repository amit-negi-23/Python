# Dictionary Method

student = {
    "name": "Amit Negi",
    "subject": {
        "phy": 95,
        "chem": 94,
        "math": 98
    }
}


# myDict.keys()       # return all keys
print(student.keys())


# myDict.values()      # return all values
print(student.values())


# myDict.items()       # return all (key, val) pair as tuples
print(student.items())


# myDict.get()          # return the value , and did not gives error if the key is not present
print(student.get("name"))  # return value
print(student.get("name1")) # return None


# myDict.update(newDict)        # insert the specified items to the 
student.update({"city": "Delhi"})
print(student)


newDict = {"age": "23", "email": "amit@gmail.com"}
student.update(newDict)
print(student)

