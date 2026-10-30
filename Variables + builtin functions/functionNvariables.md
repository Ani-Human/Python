1. abs(): Returns the absolute value of a number 
# abs(-7) -> 7

2. complex(): Creates a complex number from real and imaginary part. 
# complex(2, 3) -> 2 + 3j 

3. divmod(): Returns the quotient and remainder of a division of a tuple. 
# divmod(10, 3) -> (3, 1)

4. float(): Converts a number or compatible-string into a floating point number. 
# float(20) -> 20.0 | float('3.14') -> 3.14 

5. int(): Converts a number of compatible-string into a regular integer. 
# int('3.14') -> 3 | int(3.14) -> 3 

7. max(): Returns the largest number in an iterable or among multiple arguments.
# max(1, 5, 2) -> 5

8. min(): Returns the smallest number in a iterable or among multiple arguments. 
# min(1, 5, 2) -> 1

10. pow(): Raises a number to the specified power. 
# pow(10, 3) -> 1000

11. round(): Rounds a floating point number to the specified decimal places. 
# round(3.14159, 2) -> 3.14 

12. sum(): Sums up all the numerical items inside a container. 
# sum([1, 3, 4]) -> 8



#Iterables and Collection
1. all(): Returns True if every single item in an iterable returns True. 
# all([True, 2, 'yes]) -> True

2. any(): Returns True if any item in an iterable returns True.
# any([False, 0, "yes"]) -> True

3. enumerate(): Takes a collection and returns it as an indexed enumerate object. 
# list(enumerate(['a', 'b'])) ->  [(0, 'a'), (1, 'b')]

4. filter(): Extracts items from an iterable which passes a specified condition. 
# list(filter(lambda x: x > 2, [1, 2, 3, 4])) -> [3, 4]

5. iter(): Returns an iterator object generated from a collection. 
#  my_iterator = iter([1, 2])

6. len(): Returns a local count of items belonging to an object. 
# len("hello") -> 5

7. map(): Applies a specified function to every item inside an iterable. 
# list(map(lambda x: x * 2, [1, 2])) -> [2, 4]

8. next(): Retrievies the next consecutive items from an active iterator. 
# next(iter([5, 6])) -> 5

9. range(): Generates an immutable sequence of numbers over a specefic interval. 
# list(range(3)) -> [0, 1, 2]

10. reversed(): Returns a reverse-order iterator over a sequence.
# list(reversed([1, 2, 3])) -> [3, 2, 1]

11. slice(): Creates a slice object representing a range of indices for sequence slicing. 
# [1, 2, 3, 4][slice(0, 2)] -> [1, 2]

12. sorted(): Returns a new new sorted list containing all the items from an iterable. 
# sorted([3, 1, 2]) -> [1, 2, 3]

13. zip(): Merges elements from multiple iterables into tuples based on index matching. 
# list(zip([1, 2], ['a', 'b'])) -> [(1, 'a'), (2, 'b')]



#DATA STRUCTURE AND CONVERSION 
1. bool(): Converts a given value into true or false. 
#  bool(0) -> False

2. dict(): Creates a key-value pair dictionary collection. 
#  dict(a=1, b=2) -> {'a': 1, 'b': 2}

3. list(): Creates a mutable ordered list collection. 
# list((1, 2)) -> [1, 2]

4. set(): Creates a mutable collection containing unique, unordered elements. 
# set([1, 2, 2, 3]) -> {1, 2, 3}

5. tuple(): Creates an immutable, ordered sequence collection. 
# tuple([1, 2]) -> (1, 2)

6. str(): Coverts any specified object into its user friendly

6. bytearray(): Creates a mutable array structure of raw byte values. 
# bytearray([65, 66]) -> bytearray(b'AB')

7. bytes(): Creates an immutable array structure of raw byte values. 
# bytes([65, 66]) -> b'AB'


#OBJECT AND CLASSES
1. isinstance(): Checks if an object belongs to a specified class type. 
# isinstance("hi", str) -> True

2. type(): Returns the underlying data type of an object. 
# type(5) -> <class 'int'>


#Input/Output & System Reflection
1. Compile(): Pareses source codes into executable code objects. 
# compile('print(5)', 'test.py', 'exec')

2. format(): Formats a specified value based on a custom format specification. 
# format(0.5, '%') -> '50.000000%'

3. globals(): Returns a dictionary containing the active global symbol table. 
# global()

4. help(): Triggers built-in system helper utility documentation. 
# help(str.replace)

5. input(): Pauses program execution to read a text line from the console user. 
# name = input("Enter name: ")

6. locals(): Returns a dictionary containing the current local symbol table entries. 
# locals()

7. open(): Opens a file system path to return a workable file. 
# file() = open("test.txt", "r")

8. print(): Outputs text values directly to the console or stream file. 
# print("Hello World")

9. __import__(): Invokes the underlying system function that handles import statements. 
# math = __import__('math')




















































