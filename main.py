#Generic Type Perimeters
#THIS METHOD HELPS TO CATCH BUGS EARLIER, and auto completions.

#LIST
def process_stuff (thing: list[str]):   #Items would be a list of strings with type parameters.
    for letter in thing:
        print(letter)


#SETS AND TUPLES
def process_stuff_2(thing_1:tuple[int, int, str], thing_2: set[bytes]):
    return (thing_1, thing_2)

#DICTIONARY
def process_stuff_3(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
# process_stuff_3({'bag' : 4.99})

#Union
def process_stuff_4(item: int | str):
    print (item)

#Possibly NONE
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hi {name}")
    else:
        print("duh")
