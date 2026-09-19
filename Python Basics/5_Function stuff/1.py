def input_hello():
    name = input('What is your name?: ') # User types "Habibi" and presses Enter  
    print('Hello', name) # Output: Hello Habibi

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

def hello():
    print('Hello World using a function!')
#hello()

def calculate_sum(a, b):
    print(a + b)
my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None

# calculate_sum(5, 9) # if no arguments passed -> will show an error 

def add(a, b):
    return a + b

my_sum = add(3, 1)
print(my_sum) # 4









