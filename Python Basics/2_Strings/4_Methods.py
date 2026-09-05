# A method is a function that you call on a value. 
#  To call a string method, write the string or its variable name followed by a dot and the method call.


# upper(): Returns a new string with all characters converted to uppercase.
my_str_1= 'hello world'

uppercase_my_str = my_str_1.upper()
print(uppercase_my_str)  # HELLO WORLD



# lower(): Returns a new string with all characters converted to lowercase.
my_str_2 = 'Hello World'

lowercase_my_str = my_str_2.lower()
print(lowercase_my_str)  # hello world



# strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.
my_str_3 = '  hello world  '

trimmed_my_str = my_str_3.strip()
print(trimmed_my_str)  # "hello world"



# replace(old, new): Returns a new string with all occurrences of old replaced by new.
my_str_4 = 'hello world'

replaced_my_str = my_str_4.replace('hello', 'hi')
print(replaced_my_str)  # hi world



# split(separator): Splits a string on a specified separator into a list of strings. A list groups values between square brackets. If no separator is specified, split() splits on whitespace.
my_str_5 = 'hello world'

split_words = my_str_5.split()
print(split_words)  # ['hello', 'world']



# join(): Joins the strings in a collection into a single string with a separator.
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world



# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.
my_str_6 = 'hello world'

starts_with_hello = my_str_6.startswith('hello')
print(starts_with_hello)  # True



# endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
my_str_7 = 'hello world'

ends_with_world = my_str_7.endswith('world')
print(ends_with_world)  # True



# find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
my_str_8 = 'hello world'

world_index = my_str_8.find('world')
print(world_index)  # 6



# count(substring): Returns the number of times a substring appears in a string.
my_str_9 = 'hello world'

o_count = my_str_9.count('o')
print(o_count)  # 2



# capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
my_str_10 = 'hello world'

capitalized_my_str = my_str_10.capitalize()
print(capitalized_my_str)  # Hello world



# isupper(): Returns True if all letters in the string are uppercase and False if not.
my_str_11 = 'hello world'

is_all_upper = my_str_11.isupper()
print(is_all_upper)  # False



# islower(): Returns True if all letters in the string are lowercase and False if not. 
my_str_12 = 'hello world'

is_all_lower = my_str_12.islower()
print(is_all_lower)  # True



# title(): Returns a new string with the first letter of each word capitalized.
my_str_13 = 'hello world'

title_case_my_str = my_str_13.title()
print(title_case_my_str)  # Hello World




