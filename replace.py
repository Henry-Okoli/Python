# Use the replace function to remove ! and replace it with space 
jump = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
jump_replace = jump.replace("!", " ")
# print the replace valuable
print("jump_replace(""!"", " "): {}".format(jump_replace))

# Convert the value to Uppercase charater
jump_upper = jump_replace.upper()
print("jump_replace.upper() : {}".format(jump_upper))

# Convert the value into a lower character 
jump_lower = jump_replace.lower()
print("jump_replace.lower(): {}".format(jump_lower))

# Convert the value into reverse order  
jump_reverse = jump_replace[::-1]
print("jump_replace.__reversed__(): {}".format(jump_reverse))
print("\n ")
current_time = 12 

if current_time <11:
    print("Time for the short jog - let's go!")

else:
    print ("It's after 11 let's go and have lunch")
































