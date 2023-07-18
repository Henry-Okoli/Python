# Enter your full name here 
full_name = input("Please enter your full name ")
full_name_split = full_name.split()
# Run a validation check to make sure the valide name is entered
if len(full_name) == 0:
    print ("You have't entered anything, Please enter your full name")
elif len(full_name) < 4:
    print ("You have entered less the 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name) > 25:
    print ("You have entered more than 25 characters, Please make sure you only entered your name ")
elif len(full_name_split) == 2:
    print("Thank you for entering your full name")
else:
    print("Please make sure you only entered your name")
