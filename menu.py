# Ask the user to enter three favourite food they want to order
item1 = input("Enter the first items/food you want order: ")
item2 = input("Enter the second items/food you want order: ")
item3 = input("Enter the last items/food you want order: ")

# print the items he has ordered
items = (item1, item2, item3)
print ("Order Confirmation! You have ordered:", *items, sep= "\n")




name ="Peter Parker"
age = 32
sentence = f"My name is{name}and I'm{age}year sold."
print (sentence)