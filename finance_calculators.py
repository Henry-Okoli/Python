import math

# decied the nature of the investment you prefered 
print ("investment - to calculate the amount of interest you'll earn on your investment" 
       "\n bond      - to calculate the amount you'll have to pay on a home loan")

# select the the type of investment you will prefer either investment or bond
investment_bond = input(str("\n Enter either 'investment' or 'bond' from the menu above to proceed\n ")).lower()

# if investment is selected 
if investment_bond == "investment":
   # if True:
        principle = float (input("\n Enter the amount you want to deposite "))
        rate = float(input("\n Enter the interest rate (Do Not Incluced %) "))
        rate = float(rate /100) 
        year = float(input("\n Enter the number of years you want to invest "))
        interest = str(input("\n Do you want 'Simple' or 'Compound' interest ")).lower()

        if interest == "simple":
            #"simple" == interest
           #if True:
                interest = principle * (1 + rate * year)
                total = interest
                print (f"\n The total interest rate for {year} years is {total:.2f}".format ())
        elif interest == "compound":
            #"compound" == interest
        #if True:
                interest = principle*math.pow((1 + rate), year)
                total = interest
                print (f"\n The total compound interest for {year} years is {total:.2f}". format())
        else:
            breakpoint

# if bond is selected 
elif investment_bond =="bond":
    #if True:
        value = float(input("\n Enter the present value of the house "))
        rate = float(input("\n Enter the interest rate ")) 
        rate = (rate /100 *(1/12))   
        months = int(input("\n Enter the number of months they plan to take to repay the bond "))
        repayment = (rate * value)/(1-(1 + rate)**(-months)) 
        print(f"\n Your monthly repayment of the bond is {repayment:.2f}".format())

else:
    print("\n You have intered wrong words, Please enter the value")

        