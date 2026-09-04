# A string is a sequence of characters surrounded by either single or double quotation marks.

my_str_1 = 'Hello'
my_str_2 = "World"

my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''



#if the string contains both the types of quotes
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

msg2 = 'It\'s a sunny day'
quote2 = "She said, \"Hello!\""



# In operator: returns a boolean that specifies whether the character or characters exist in the string or not.
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False



#  len() function: To get the length of a string {you can get the length of a string and work with the individual characters in a string, a process called indexing.}
intro = 'Hello world'
print(len(intro))  # 11



# Each character in a string has a position called an index.
# The index is zero-based, meaning that the index of the first character of a string is 0, the index of the second character is 1, and so on.
# To access a character by its index, you use square brackets ([]) with the index of the character you want to access inside. 
string = "Hello world"

print(string[0])  # H
print(string[6])  # w



# A mutable value can be changed after it is created, while an immutable value cannot.
# You can point a variable at a new value, which is called reassignment, but you can't change an immutable value itself by adding, removing, or replacing any of its elements.
# Strings are immutable in Python. This means that you can reassign a different string to a variable.
greetings = 'hi'
greetings = 'hello'
print(greetings) # hello


# But direct modification of a string isn't allowed:

greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

# Integers, floats, and booleans are also immutable.