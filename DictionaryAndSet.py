# Nested dictionary 

student = {
    "name": "Amit Negi",
    "subject": {
        "phy": 95,
        "chem": 94,
        "math": 98
    }
}

print(student["subject"])
print(student["subject"]["math"])

