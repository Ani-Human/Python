# you will often run into situations where you need to compare multiple values at once. This can lead to nested conditional statements

#EXAMPLE
is_citizen = True
age = 25

if is_citizen: #  if is_citizen is True. If so, it will then go to the nested if statement and check if age is greater than or equal to 18
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')



# In Python, every value has an inherent boolean value, or a built-in sense of whether it should be treated as True or False in a logical context. 
# Many values are considered truthy, that is, they evaluate to True in a logical context. Others are falsy, meaning they evaluate to False.

'''
Few FALSY Values 
- False
- Integer 0
- Float 0.0
- Empty Strings

Few TRUTHY Values
- True
- Integer 1
- Float 1.0
- Strings
'''


# If you want to check whether a value is truthy or falsy, you can use the built-in bool() function. It explicitly converts a value to its boolean equivalent and returns True for truthy values and False for falsy values.
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True


# Logical operators are special operators that allow you to combine multiple expressions to create more complex decision-making logic in your code.
# There are three Boolean operators in Python: and, or, and not.


# The 'and' operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value.
is_citizen = True
age = 25

print(is_citizen and age) # 25
# The 'and' operator is known as a short-circuit operator. Short-circuiting means Python checks values from left to right and stops as soon as it determines the final result.


# You'll often use and within if statements to check if multiple conditions are met. 
# REFACTORED EXAMPLE
is_a_citizen = True
aged = 25

if is_a_citizen and aged >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')


#  'or' operator returns the first operand if it is truthy, otherwise, it returns the second operand.
# An 'or' expression results in a truthy value if at least one operand is truthy. The or operator is also known as a short-circuit operator.
year = 19
is_employed = False

print(year or is_employed) # 19

# EXAMPLE CODE
agedd = 19
is_student = True

if agedd < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')


# 'not' operator takes a single operand and inverts its boolean value. It converts truthy values to False and falsy values to True. Unlike the previous operators we looked at, not always returns True or False.
print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy


# Example code 
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')


