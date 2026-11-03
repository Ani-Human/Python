# Strings: Characters enclosed in quotes(any type)

# Multiline comment
multiline_comment = """hello
i am a habibi"""

# String concatenation
first_name = 'Habibi'
last_name = 'Sheikh'
space = ' '
full_name = first_name  +  space + last_name

# String Formatting + Interpolating
name= "Habibi"
print(f"Hi {name}")

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')


# Unpacking characters 
language = 'Python'
g,h,c,d,e,f = language # unpacking sequence characters into variables



# String Indexing

# -6 -5 -4 -3 -2 -1
#  p  y  t  h  o  n
#  0  1  2  3  4  5

first_letter = language[0] # p
last_letter = language[-1] # n
last_three = language[3:] # hon
pto = language[0:6:2] # skipped 

# Reversing a string 
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH


