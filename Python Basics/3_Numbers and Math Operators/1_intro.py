# Integers and floats are the primary numeric data types in Python. With them, you can store numeric data and perform mathematical operations.

# Integers are whole numbers without decimal points, either positive or negative. 
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>


# addition operation
int_1 = 56
int_2 = 12

sum_ints = int_1 + int_2  # +=
print('Integer Addition:', sum_ints) # Integer Addition: 68


#subtraction operation
my_int_3 = 56
my_int_4 = 12

# Subtraction
diff_ints = my_int_3 - my_int_4  # -=
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44


#multiplication operation
my_int_5 = 12
my_int_6 = 4

# Multiplication
product_ints = my_int_5 * my_int_6  # *=
print('Integer Multiplication:', product_ints) # Integer Multiplication: 48


# Division Operation
my_int_7 = 56
my_int_8 = 12

# Division
div_ints = my_int_7 / my_int_8  # /=
print('Division:', div_ints) # Division: 4.666666666666667






# Floats
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4


# Subtraction Operation
my_float_3 = 5.4
my_float_4 = 12.0

float_subtraction = my_float_4 - my_float_3
print('Float Subtraction:', float_subtraction) # Float Subtraction: 6.6


# Product Operation
my_float_5 = 5.4
my_float_6 = 12.0

float_multiplication = my_float_6 * my_float_5
print('Float Multiplication:', float_multiplication) # Float Multiplication: 64.80000000000001


# Division Operation
my_float_7 = 5.4
my_float_8 = 12.0

float_division = my_float_8 / my_float_7
print('Float Division:', float_division) # Float Division: 2.222222222222222







# If you add an integer and a float, the result is automatically converted to a float. 
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>



# The modulo operator (%) returns the remainder when the value on the left is divided by the value on the right. 
my_int_9 = 56
my_int_10 = 12

my_float_11 = 5.4
my_float_12 = 12.0

mod_ints = my_int_9 % my_int_10
mod_floats = my_float_12 % my_float_11

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993



# Floor division divides two numbers and returns the greatest integer less than or equal to the result. This is done with the double forward slash operator (//). 
my_int_13 = 56
my_int_14 = 12

my_float_15 = 5.4
my_float_16 = 12.0

floor_div_ints = my_int_13 // my_int_14
floor_div_floats = my_float_16 // my_float_15

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0



# Exponentiation raises a number to the power of another, and is done with the double asterisk operator (**):
my_int_17 = 56
my_int_18 = 12

my_float_19 = 5.4
my_float_20 = 12.0

exp_ints = my_int_17 ** my_int_18
exp_floats = my_float_19 ** my_float_20

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089


# Sometimes, you might notice that the result of an operation involving floats has more decimal digits than expected. 
# This happens because numbers are stored in binary format, and some fractions cannot be represented exactly in binary. As a result, they are stored as finite approximations, in the same way the fraction 1/3 cannot be represented with a finite number of digits in decimal and is truncated after a certain number of its infinite digits (0.33333...).
# This leads to small rounding errors.
# Python also provides built-in functions for converting either numeric data or strings into integers or floats.



# The float() function returns a floating-point number constructed from the given number
int_1 = 56
float_1 = float(int_1)

print(float_1)  # 56.0
print(type(float_1))  # <class 'float'>


# The int() function returns an integer constructed from the given number
my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>



# Also, you can use the same built-in functions to convert a string into either a float or integer
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>





# METHODS FOR NUMBERICAL STUFF

# round(): Rounds a number to the specified number of decimal places. By default this function rounds to the nearest integer, and returns a whole number with no decimal places. 
int_3 = 4.798
int_4 = 4.253

rounded_int_1 = round(int_3)
rounded_int_2 = round(int_4, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3



# abs(): returns the absolute value of a number. 
num = -15

absolute_value = abs(num)
print(absolute_value) # 15



# pow(): raises a number to the power of another or performs modular exponentiation.
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3
