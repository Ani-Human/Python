cities = ['Los Angeles', 'London', 'Tokyo']

# For accesing an element
print(cities[0]) # 'Los Angeles'

# Accesing through negative indexing
print(cities[-1]) # 'Tokyo'


# Using list constructors 
developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']


# to get the total number of elements in a list 
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5


# updating a value at a particular index
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

# checking if an element is in the list 
print('Rust' in programming_languages) # True
print('JavaScript' in programming_languages) # False


# if you pass in an index (either positive or negative) that is out of bounds for the list, then you will receive an IndexError


# To remove an element 
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

# Nested lists 
developer2 = ['Alice', 25, ['Python', 'Rust', 'C++']]

# To access a nested list
print(developer2[2]) # ['Python', 'Rust', 'C++']

# To access an element in the nested list 
developer2[2][1] # 'Rust'



# Value unpacking 
developer3 = ['Max', 34, 'Rust Developer']
name, age, job = developer3

print(name) # 'Max'
print(age) # 34
print(job) # 'Rust Developer'


developer4 = ['John', 34, 'Rust Developer']
name, *rest = developer4

print(name) # 'John'
print(rest) # [34, 'Rust Developer']

# If the numbers of variables on the left side of the assignment operator doesn't match the total numbers of items in the list, then you will receive a ValueError



# List slicing works too
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4]) # ['Cookies', 'Ice Cream', 'Pie']


# Slice operator with step intervals
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2]) # [2, 4, 6]

