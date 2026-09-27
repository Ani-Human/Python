#tuples 
developer = ('Alice', 34, 'Rust Developer')

print(developer[1]) # 34


numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4

dev = 'Jessica'
tuple(dev) # ('J', 'e', 's', 's', 'i', 'c', 'a')



programming_languages = ('Python', 'Java', 'C++', 'Rust')

print('Rust' in programming_languages) # True
print('C' in programming_languages) # False



developer1 = ('Max', 34, 'Rust Developer')
name, age, job = developer1

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'



developer2 = ('Jay', 34, 'Rust Developer')
name, *rest = developer2

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']


desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')


# Tuples are immutable 




















