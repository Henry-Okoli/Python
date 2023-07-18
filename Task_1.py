def calculate(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = 'Invalid operator'
    
    return result

def write_to_file(equation):
    with open('equations.txt', 'a') as file:
        file.write(equation + '\n')

def main():
    while True:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        operator = input('Enter the operator (+, -, *, /): ')
        
        equation = f'{num1} {operator} {num2} = {calculate(num1, num2, operator)}'
        print('Result:', equation)
        
        write_to_file(equation)
        
        choice = input('Do you want to perform another calculation? (yes/no): ')
        if choice.lower() != 'yes':
            break

if __name__ == '__main__':
    main()