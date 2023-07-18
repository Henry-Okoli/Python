# Usuing a while loop to sum integer values up to a certain rang
sum1 = 0
i = 0
while sum1 <= 250:
    sum1 += i
    i += 2
print(sum1)

# printing numbers from 1 - 10
y = 0
while y < 10:
    y += 1
    print(y)

# Appling a BREAKE statement within a while loop 
Breake_statement = 0

while Breake_statement < 100:
    Breake_statement += 1
    if Breake_statement == 23:
        break
print(Breake_statement)

# appling continous statement that will  continue if a certain condition is met
continue_statement = 0

while continue_statement < 100:
    continue_statement += 1
    if continue_statement >23:
        continue
print(continue_statement)    

# this will only print one output which is 10 
i = 9
while i < 10:
    i = i + 1
print(i)



# To guest a random values from a rang of values 1 to 50 

import random
num = random.randint(1,50)
num_guess = int(input("Guess a number from 1 to 50: "))

while num_guess != num:
    if num_guess < num:
        num_guess = int(input("To small! Guess another number from 1 to 50: "))
    else:  num_guess = int(input("To big! Guess another number from 1 to 50: "))
    
print("You guessed correctly!")


# 
number = int(input("Enter number less than 100: "))
while number > 100:
    print("Please try again")
    number = int(input("Enter number less than 100: "))
if number % 2 == 0:
    print(number * 2)
else:
    print(number * 3)




