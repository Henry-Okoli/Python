# take the order of what they want to eat
# output what they have ordered
#1
# item1 = input("Enter the first items/food you want order: ")
# item2 = input("Enter the second items/food you want order: ")
# item3 = input("Enter the last items/food you want order: ")

# items = (item1, item2, item3)
# print ("Order Confirmation! You have ordered:", *items, sep= "\n")

# OR

#2

# iteams = []

# for i in range(3):
#     iteam = input(f'choose three food you want to eat {i+1} Enter the iteam here: ')
#     iteams.append(iteam)

# print("\nOrder conformation!!!, You have ordered:\n")

# for iteam in iteams:
#     print(iteam)


def order_taken(num_iteam):
    iteams = []
    for i in range(num_iteam):
        while True:
            # try:
                iteam = input(f'choose five food you want to eat {i+1} Enter the iteam here: ').strip()
                if iteam.isdigit(): # just to check if the input is empty ot you entered a digit no
                    print("Please enter a food iteam")
                elif iteam:
                     iteams.append(iteam)
                     break
                else:
                    print('You have not selected any iteam')
            # except ValueError:
            #     print("Invalied input, please try again")
    return iteams

def main():
    num_iteam = 5  # you can change it to the number the iteams you want them to enter
    ordered_iteams = order_taken(num_iteam)

    print("\nOrder conformation!!!, You have ordered:\n")

    for iteam in ordered_iteams:
        print(iteam)

if __name__ == "__main__":
    main()


# to pirnt the name of the person taken the order
name ="Peter Parker"
age = 32
sentence = (f"My name is {name} and I'm {age} year sold.")
print (sentence)