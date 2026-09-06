# Conditional statements, or conditionals, let you control the flow of your program based on whether certain conditions are true or false.
# Comparison operators are operators that let you compare two or more values, and return a boolean value. 
# booleans are one of the data types in Python, and can only be True or False.

# -COMPARISON OPERATOR-
# == (Equals): Checks if two values are equal
# != (Not Equal): Checks if two values are not equal
# > (Greater than): Checks if the value on the left is greater than the value on the right
# < (Lesser than): Checks if the value on the left is less than the value on the right
# >= (Greater than equal to): Checks if the value on the left is greater than or equal to the value on the right
# <= (Lesser than equal to): Checks if the value on the left is less than or equal to the value on the right. 

print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

# These operators can be used in conditionals to compare values and run certain code based on whether the conditional evaluates to True or False.


# the most basic conditional is the if statement. Here's the basic syntax: 
condition = 8 < 9
if condition:
    pass # Code to execute if condition is True



# EXAMPLE
age = 18

if age >= 18:
    print('You are an adult') # You are an adult



#  The else clause runs when the if condition is false. Here's the syntax for an if…else statement. 
conditions = None
if conditions:
   pass # Code to execute if condition is True
else:
   pass # Code to execute if condition is False

# EXAMPLE
aged = 12

if aged >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet



# Note that you cannot place any statements between the if block and the else clause. The following code would raise a SyntaxError

# There might be situations in which you want to account for multiple conditions. To do that, Python lets you extend your if statement with the elif (else if) keyword.
conditioned = None
if conditioned1:
   pass # Code to execute if condition1 is True
elif conditioned2:
   pass # Code to execute if condition1 is False and condition2 is True
else:
   pass # Code to execute if all conditions are False

#EXAMPLE 
ages = 12

if ages >= 18:
    print('You are an adult')
elif ages >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child


# Note that you can use as many elif clauses as you want. 
years = 2

if years >= 65:
    print('You are a senior citizen')
elif years >= 30:
    print('You are an adult in your prime')
elif years >= 18:
    print('You are a young adult')
elif years >= 13:
    print('You are a teenager')
elif years >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant

