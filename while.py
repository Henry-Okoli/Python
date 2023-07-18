# ask the user to enter a number 
# the code will exist the program if the user enter -1
# the code will calculate the avarage of the total value entered and print it out 
# if the code get anything less than zero it should triger it to calculate the average 
Total = 0
count = 0

while True:
    try:
        number = int(input("Enter a valied number: "))
        if number == -1:
           break
        Total += number
        count += 1
    except ValueError:
        print("Invalid input, Enter a valid number: ")

if count > 0:
    average = Total/count
    print("Average: ", average)
else:
    print ("You did not enter any number")  


start = 5
while start % 2 != 0:
    print(start)
    start += start
#loop will only execute once before condition is no longer true
