#N1
str_number=map(int,["10","25","50","15"])

print(list(str_number))

#N2
prices =[100,150,75,420]
discount = 0.20
dictionary =[]

for price in prices:
    dictionary.append(price * (1 - discount))

print(dictionary)

#N3
first_names = ["Іван", "Марія", "Олександр"]
last_names = ["Петров", "Іванова", "Коваль"]

def make_full_name(first, last):
    return f"{first} {last}"

full_names = list(map(make_full_name, first_names, last_names))

print(full_names)