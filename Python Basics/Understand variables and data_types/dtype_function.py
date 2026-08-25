#type function to get the type of the value which a variable has. 
human = 'ani'
print(type(human))  # <class 'str'>

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>


#isinstance function is used to check if a variable mathces the desired datatype. 
human= 'ani'
# print(isinstance(human, str))
# print(isinstance(human, int)) # Very helpful for verifying the datatype. 
# print(isinstance(human, bool))
# print(isinstance(human, range))
# Multiple types can be checked at once!
print(isinstance(human, (int, bool, range, str))) # is it int or bool or range or str? ITS STRING


