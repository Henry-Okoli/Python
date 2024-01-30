# # Enter your full name here 
# full_name = input("Please enter your full name ")
# full_name_split = full_name.split()
# # Run a validation check to make sure the valide name is entered
# if len(full_name) == 0:
#     print ("You have't entered anything, Please enter your full name")
# elif len(full_name) < 4:
#     print ("You have entered less the 4 characters. Please make sure that you have entered your name and surname.")
# elif len(full_name) > 25:
#     print ("You have entered more than 25 characters, Please make sure you only entered your name ")
# elif len(full_name_split) == 2:
#     print("Thank you for entering your full name")
# else:
#  print("Please make sure you only entered your name")


def validate_full_name(full_name):
    min_length, max_length = 4, 25

    if not full_name:
        return 'You did not enter a name please enter your fullname'
    elif len(full_name) < min_length:
        return f'The name you enter is too small please enter you full name'
    elif len(full_name) > max_length:
        return f'The name you entered is too much reduce it to 25 characters'

    name_part = full_name.split()
    if len(name_part) != 2:
        return 'Enter your first name and your surname'
    return 'Thank you for returning your full name'
    

def get_full_name():
    """
    prompt the user to enter their full name
    str:
    The full name has been entered
    """
    try:
        return input("Enter your full name here:").strip()
    except Exception as e:
        print(f'An error has occured: {e}')
        return ""

def main():
    full_name = get_full_name()
    validate_message = validate_full_name(full_name)
    print(validate_message)

if __name__ ==" __main__":
    main()

    