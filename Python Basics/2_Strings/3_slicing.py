# String slicing lets you extract a portion of a string or work with only a specific part of it.
# string[start:stop:step]

# If you want to extract characters from a certain index to another, you just separate the start and stop indices with a colon:
my_str = 'Hello world'
print(my_str[1:4]) # ell
# Note that the stop index is non-inclusive, so [1:4] just extracted the characters from index 1, and up to, but not including, the character at index 4.


# You can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively.
my_str_1 = 'Hello world'
print(my_str_1[:7])  # Hello w
# This extracts everything from index 0 up to (but not including), the character at index 7. 


#For the stop index
my_str_2 = 'Hello world'
print(my_str_2[8:])  # rld
# This extracts everything from the character at index 8 until the end of the string.



# Note that slicing a string does not modify the original string!
my_str_3 = 'Hello world'
print(my_str_3[8:])  # rld
print(my_str_3)  # Hello world



# You can also omit both the start and stop indices, which will extract the whole string. 
my_str_4 = 'Hello world'
print(my_str_4[:])  # Hello world



# Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.
# Syntax: string[start:stop:step]
my_str_5 = 'Hello world'
print(my_str_5[0:11:2])  # Hlowrd



# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank. 
my_str_reversed = 'Hello world'
print(my_str_reversed[::-1]) # dlrow olleH




