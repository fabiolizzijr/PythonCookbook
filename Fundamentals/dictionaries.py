# Dictionaries Examples and training
#=========================================
# import pretty print
#=========================================
import pprint

# Creating a dictionary
fruits_in_basket = {"Banana": 3, "Apple": 2, "Strawberry": 12,
                    "Orange": 5, "Pineapple":3, "Watermelon":2}

# Pretty printing it
pprint.pprint(fruits_in_basket)
print("-----------------------------------------------------------")
# Printing key value pars with for loop
for key, value in fruits_in_basket.items():
    print(key + ": " + str(value))

print("------------------------------------------------------------")

# Testing get method
print("I have " + str(fruits_in_basket.get('Orange', 0)) + " oranges")
print("I have " + str(fruits_in_basket.get('Apple', 0)) + " apples")
print("I have " + str(fruits_in_basket.get('Melon', 0)) + " melons")
print("-------------------------------------------------------------")

# Testing setdefault
fruits_in_basket.setdefault('Orange', 10) # This don't work, 'Orange' already exist
fruits_in_basket.setdefault('Apples', 10) # This don't work, 'Orange' already exist
fruits_in_basket.setdefault('Kiwis', 10)# This create Kiwis and set 10
print("NOW I have " + str(fruits_in_basket.get('Orange', 0)) + " oranges")
print("NOW I have " + str(fruits_in_basket.get('Apple', 0)) + " apples")
print("NOW I have " + str(fruits_in_basket.get('Kiwis', 0)) + " kiwis")
print("-------------------------------------------------------------")

favorite_fruit = 'Banana'
# Does this item is in the dictionary ?
if favorite_fruit in fruits_in_basket:
    print(" The fruit that I love is in the basket!")
else:
    pprint.pprint(favorite_fruits)

# This also create a dictionary
empty_dic = {}

# This too create a dictionary
my_fav_game = dict()

if empty_dic == my_fav_game:
    print("They are empty!")
