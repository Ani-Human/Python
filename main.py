def get_name_with_age(name: str, age: int):                   #Type hints declared but unsupported combination (str + int)
    name_with_age = name + " is this old: " + str(age)        #Converted age to str for compatibiltiy.
    return name_with_age

print(get_name_with_age('ani', 18))