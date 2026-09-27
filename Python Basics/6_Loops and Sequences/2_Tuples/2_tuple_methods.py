programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')

programming_languages.count('Rust') # 2
programming_languages.count('javascript') # 0
# If no arguments are passed into the count() function, then Python raises a TypeError

programming_languages.index('Java') # 1
# If the specified item cannot be found, then Python raises a ValueError
programming_languages.index('Python', 2) # 2
# optional start , stop index 
programming_languages.index('Python', 2, 5) # 2
# with a step index

sorted(programming_languages, key=len)
print(sorted(programming_languages, reverse=True))


numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]







