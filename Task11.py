# dictionary to perform mathematical operation 
def calculate(num1, num2, operator):
    # perform the apporpriate mathematical operation based on the operator 
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        try:
            result =  num1 / num2
        except ZeroDivisionError:
            print ("Division by zero\n")
    else:
        result = 'Invalid operator'

    return result
# write to file operation
# file = open("output.txt", 'a')

# write to a file 
def write_to_file(Arithmatics):
    # Open the file in 'append' mode and write the arithmetic expression
    with open ("Arithmatics.txt", "a") as file:
        file.write(Arithmatics + '\n')

#read to file operation 
def read_from_file(file_name):
    try:
        # Open the file in 'read' mode and read all lines
        with open (file_name, 'r') as file:
            maths_Arithmatics = file.readlines()
            return [Arithmatics.strip() for Arithmatics in maths_Arithmatics]
    except FileNotFoundError:
        print("Error: File not found")
        return None
    
# print the result of the read file 
def print_the_result(maths_Arithmatics):
    if maths_Arithmatics is not None:
        for Arithmatics in maths_Arithmatics:
            print(Arithmatics)
            # part = Arithmatics.split(' ')
            # num1 = float(part[0])
            # operator = part[1]
            # num2 = float(part[2])
            # print(num2)
            # result = calculate(num1 , num2, operator)
            # if  result is not None:
            #     Arithmatics += f' = {result}'
            # print(Arithmatics)

# accept and compute the input values 
def main():
    while True:
        select = input("\nCHOOSE EITHER 1 OR 2\nIf you choose '1' you will enter the numbers and operators before you can get your out put \nIF you choose '2' it will read equation from the file:  \n")
        
        if select == '1':
    # read number and operation from the input side
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
            except ValueError:
                print("Error: Invalid entry, Please enter a valide number. ")
                continue

            operator = input("Enter the operator (+, -, *, /): ")
            
            Arithmatics = f'{num1} {operator} {num2}'

            result = calculate (num1, num2, operator)
            if result is not None:
                Arithmatics += f' = {result}'
            print("Result: ", Arithmatics)

            write_to_file(Arithmatics)

        elif select == '2':
            file_name = input("Enter the the name of the text file: ")
            maths_Arithmatics = read_from_file(file_name)
            if maths_Arithmatics is not None:
                print_the_result(maths_Arithmatics)

        else:
            print("Error: invalid choose, choose either 1 or 2")
            
        final = input("Do you want to do another calculation (yes/no): ")
        if final != 'yes':
            break

if __name__ == '__main__':
    main()