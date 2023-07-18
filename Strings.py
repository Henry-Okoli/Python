# Strip the word off the $ sign and print out the word only
##hero = "$$$Superman$$$"
#hero_strip = hero.strip("$")
#print ("hero_strip(""): {}".format(hero_strip))


#And while loop:
import math

# Print the what optios the user can choose "investment" or "bond".
print("investment - to calculate the amount of interest you'll earn on your investment\n"
      "bond - to calculate the amount you'll have to pay on a home loan")

# Print empty line.
print()

# User input to choose calculation type
choice = input(
    "Enter either 'investment' or 'bond' from the menu above to proceed: ")


# Check user input and execute relevant calculation
while choice.lower() not in ['investment', 'bond']:
    print('Invalid choice, please try again')
    choice = input(
        "Enter either 'investment' or 'bond' from the menu above to proceed: ")

if choice.lower() == "investment":
    # Get input from user for investment calculation
    while True:
        try:
            deposit_amount = float(
                input("Enter the amount of money for depositing: "))
            break
        except ValueError:
            print("Invalid input, the amount of money for depositing ")
    while True:
        try:
            interest_rate = float(
                input("Enter the interest rate (as a percentage): "))
            break
        except ValueError:
            print("Invalid input, the interest rate (as a percentage): ")
    while True:
        try:
            years = int(
                input("Enter the number of years you plan on investing: "))
            break
        except ValueError:
            print("Invalid input, the number of years you plan on investing: ")
    while True:
        interest = input(
            "Do you want 'simple' or 'compound' interest: ").lower()
        if interest in ['simple', 'compound']:
            break
        else:
            print("Invalid input, please enter 'simple' or compound' interest ")

    # Calculate the total amount
    r = interest_rate / 100
    if interest == "simple":
        total_amount = deposit_amount * (1 + r * years)
    elif interest == "compound":
        total_amount = deposit_amount * math.pow((1 + r), years)
    else:
        print("Invalid input. Please try again. ")
        exit()

    # Print the total amount
    print("Total amount after {} years is: {:.2f}".format(years, total_amount))

elif choice.lower() == "bond":
    # Get input from user for bond calculation
    while True:
        try:
            present_value = float(
                input("Enter the present value of the house: "))
            break
        except ValueError:
            print("Invalid input, the present value of the house: ")
    while True:
        try:
            interest_rate = float(input("Enter the interest rate: "))
            break
        except ValueError:
            print("Invalid input, the interest rate: ")
    while True:
        try:
            months = int(
                input("Enter the number of months to repay the bond: "))
            break
        except ValueError:
            print("Invalid input, please the number of months to repay the bond: ")

    # Calculate the bond repayment
    r = (interest_rate / 100) / 12
    bond_repayment = (r * present_value) / (1 - math.pow((1 + r), -months))

    # Print the bond repayment
    print("Monthly bond repayment is: {:.2f}".format(bond_repayment))

else:
    # Invalid input
    print("Invalid input. Please try again.")



#If statement code:
# simple financial calculator
import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
   
user_choice = input("Either enter 'investment' or 'bond' from the menu above.\n").lower()

# investment choice at initial input
if user_choice == "investment".lower():
    deposit = float(input("How much money are you depositing?\n"))
    interest_rate = float(input("what is the percentage rate as a figure only?\n"))
    interest_rate_float = float(interest_rate / 100)
    years = float(input("How many years do you want to invest for?\n"))
    interest_type = input("Will it be simple or compound interest?\n").lower()
    
# simple interest choice
    if interest_type == "simple":
        money_back = deposit * (1 + (interest_rate_float * years))
        print(f"Money returned to you would be {money_back}")
    
# compound interest choice
    elif interest_type == "compound":
         money_back_compound = deposit * math.pow((1 + interest_rate_float), years)
         money_back_compound_2dec = float("{:.2f}".format(money_back_compound))
         print(f"Money returned to you would be £{money_back_compound_2dec}")
    else:
        breakpoint

# bond choice at initial input
elif user_choice == "bond".lower():
     house_value = float(input("what is the house value?\n"))
     bond_interest = float(input("whats is the current interest rate?\n"))
     bond_interest_monthly = float((bond_interest /12) / 100)
     time_to_repay = float(input("How many months do you need to pay bond back?\n"))
     repayment = (bond_interest_monthly * house_value) / (1 - (1 + bond_interest_monthly)**(- time_to_repay))
     repayment_2decimals = float("{:.2f}".format(repayment))
     print(f"Monthly repyament would be £{repayment_2decimals}")

else:
    print("Wrong choice entered")