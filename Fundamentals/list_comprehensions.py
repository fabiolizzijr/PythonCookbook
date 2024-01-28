# List comprehension example
# Examples WITHOUT, then WITH List Comprehension
# It has 3 common uses:
# -> 1. To alter multiple items
# -> 2. To extract data
# -> 3. To filter data

#================================================================
# 1. Alter multiple items to uppercase WITHOUT List comprehension
fruits = ['apples', 'bananas', 'strawberries'] # simple list
new_fruits = []
for fruit in fruits:
    new_fruits.append(fruit.upper())

print("------------WITHOUT List comprehension-----------------------------")
print(new_fruits)
#================================================================
# 1. Alter multiple items to uppercase WITH List comprehension
comprehension_fruits = [fruit.upper() for fruit in fruits]
print("\n------------WITH List comprehension-----------------------------")
print(comprehension_fruits)
# How it works: new_list = [action conditions/for]
#================================================================
# 2. Extract data WITHOUT list comprehension
# list of dictionaries
squad =         [{'name': 'Eric',   'age': 23, 'trained': True},
                 {'name': 'Alex',   'age': 49, 'trained': True},
                 {'name': 'Fabio',  'age': 35, 'trained': True},
                 {'name': 'Henry',  'age': 25, 'trained': False},
                 {'name': 'Helena', 'age': 23, 'trained': True},
                 {'name': 'Anderson', 'age': 25, 'trained': False},]
not_trained = [] # Extract list of soldier with trained: False
age_23 = [] # Extract list of soldier with age: 23
for soldier in squad:
    if soldier['trained'] == False:
        not_trained.append(soldier)
    elif soldier['age'] == 23:
        age_23.append(soldier)

print("\n------------WITHOUT List comprehension-----------------------------")
print(not_trained)
print(age_23)
#=========================================================================
# 2. Extract data WITH list comprehension
list_comp_not_trained = [soldier for soldier in squad if soldier['trained'] == False]
list_comp_age_23 = [soldier for soldier in squad if soldier['age'] == 23]
print("\n------------WITH List comprehension-----------------------------")
print(list_comp_not_trained)
print(list_comp_age_23)
#=========================================================================
# 3. Filter data to be done...