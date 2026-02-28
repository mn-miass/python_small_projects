def calculate(operator, operand1, operand2):
    if operator == '+':
        return (operand1 + operand2)
    elif operator == '-':
        return (operand1 - operand2)
    elif operator == '*':
        return (operand1 * operand2)
    elif operator == '/':
        return (operand1 / operand2)
    elif operator == '%':
        return (operand1 % operand2)

if __name__ == "__main__":
    operator = input("Enter the operator (+ - *  / %): ")
    if operator not in "+-*/%":
        print(f"{operator} not valid")
        exit()
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = calculate(operator, num1, num2)
    print(f"The result is: {round(result, 3)}")
