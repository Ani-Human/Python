tax_rate = 0.1 # global scope 

def calculate_tax(price):
    tax = price * tax_rate  # local scope 
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
#   print(tax) # NameError: name 'tax' is not defined 