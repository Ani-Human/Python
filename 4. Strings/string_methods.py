challenge = 'thirty days of python'

# capitalize(): Converts the first character of the string to capital letter
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# find(): Returns the index of the first occurrence of a substring, if not found returns -1. 
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1. 
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# isalnum(): Checks alphanumeric character. Space is excluded. 
# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z). Space is excluded. 
# isdecimal(): Checks if all characters in a string are decimal (0-9)
# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers). 
# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½). 

# islower(): Checks if all alphabet characters in the string are lowercase. 
# isupper(): Checks if all alphabet characters in the string are uppercase

# strip(): Removes all given characters starting from the beginning and end of the string
print(challenge.strip('noth')) # 'irty days of py'

# replace(): Replaces substring with a given string
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# title(): Returns a title cased string
print(challenge.title()) # Thirty Days Of Python

# startswith(): Checks if String Starts with the Specified String
print(challenge.startswith('thirty')) # True
print(challenge.startswith('thirty')) # False



web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
















