def loop1():
    programming_languages = ['Rust', 'Java', 'Python', 'C++']
    for languages in programming_languages:
        print(languages)

def loop2():
    for char in 'code':
        print(char)
    

def nested_loop():
    categories = ['Fruit', 'Vegetable']
    foods = ['Apple', 'Carrot', 'Banana']

    for category in categories:
        for food in foods:
            print(category, food)


# while LOOPS

def Wloop1():
    secret_number = 3
    guess = 0

    while guess != secret_number:
        guess = int(input("Enter the secret number: "))
        if guess != secret_number:
            print("Try again!")
    
    print("You got it!")


