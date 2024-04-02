def calculate(num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)

    if operator == "+" or operator == "1":
        return num1 + num2
    elif operator == "-" or operator == "2":
        return num1 - num2
    elif operator == "*" or operator == "3":
        return num1 * num2
    elif operator == "/" or operator == "4":
        if num2 == 0:
            print("Error: Division by zero")
            return None
        else:
            return num1 / num2
    else:
        print("Invalid operator")
        return None

num1 = input("The First Number: ")
num2 = input("The Second Number: ")
operator = input("Operator to use (1 or +, 2 or -, 3 or *, 4 or /): ")

result = calculate(num1, operator, num2)
if result is not None:
    print(f"{num1} {operator} {num2} = {result}")