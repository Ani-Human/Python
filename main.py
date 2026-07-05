def get_full_name(first_name: str, last_name: str):         #The function with the parameters equipped with type hints (str)
    full_name= first_name.title() + ' ' + last_name.title()  #String concatenation, giving the parameters a way to express them selves. Used .title() to capitalize the first letter.
    return full_name                                        #Returning the output

print(get_full_name('john', 'doe'))

#type hints are used for annotations for variables, to declare the type of data they give.