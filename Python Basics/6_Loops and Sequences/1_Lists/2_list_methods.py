# append method
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]


# To add one list at the end of the other 
numbers2 = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers2.append(even_numbers)
print(numbers2) # [1, 2, 3, 4, 5, [6, 8, 10]]  # entire even_numbers list is nested inside of the numbers list.


# extend method -> Adds elements individually 
numbers3 = [1, 2, 3, 4, 5]
even_numbers2 = [6, 8, 10]
numbers3.extend(even_numbers2)
print(numbers3) # [1, 2, 3, 4, 5, 6, 8, 10]


# insert method 
numbers4 = [1, 2, 3, 4, 5]
numbers4.insert(2, 2.5) # (index to insert in, element to insert)
print(numbers4) # [1, 2, 2.5, 3, 4, 5]


# remove method 
numbers5 = [10, 20, 30, 40, 50, 50]
numbers5.remove(50) # takes the element to remove as an argument 
print(numbers5) # [10, 20, 30, 40, 50]


# pop method -> removes element at a specefic index 
numbers6 = [1, 2, 3, 4, 5]
numbers6.pop(1) # The number 2 is returned


# clear method -> to clear the list 
numbers7= [1, 2, 3, 4, 5]
numbers7.clear()

print(numbers7) # []


# sort method  -> for sorting the random list 
numbers8 = [19, 2, 35, 1, 67, 41]
numbers8.sort()
print(numbers8) # [1, 2, 19, 35, 41, 67]


# sorted method -> returns a new list after sorting 
numbers9 = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers9)
print(numbers9) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]


# Reverse method 
numbers10 = [6, 5, 4, 3, 2, 1]
numbers10.reverse()
print(numbers10) # [1, 2, 3, 4, 5, 6]


# index method 
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1


# If the element in a list can't be found -> it gives ValueError 




