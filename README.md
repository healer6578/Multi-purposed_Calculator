# Multi-purposed Math Calculator

This Calculator can help new coders understand basic math operators in python.

Also help new-programmers to get a easier understanding of basic math in coding.

## Inputs (1, 2, 3, 4, 5, 6) and its following Operation/function.

---

### Importing nessesary libraries
```
import math
```

### Define function
```
def calculate(num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)
```
### Addition:
```
if operator == "1":
        return num1 + num2
```
### Subtraction:
```
    elif operator == "2":
        return num1 - num2
```
### Multiplication:
```
    elif operator == "3":
        return num1 * num2
```
### Division:
```
    elif operator == "4":
        if num2 != 0:  # To Check if the division is by zero
            return num1 / num2
        else:
            print("Not defined: Division is by zero")
            return None
```
### Square root:
```
    elif operator == "5":
        if num1 >= 0: 
            return math.sqrt(num1)
        else:
            print("Error: Cannot calculate square root of a negative number")
            return None
```
### Exponentiation:
```
    elif operator == "6": 
        return num1 ** num2 
```
### If the all the operators are not recognized:
```
    else:
        print("Invalid operator")
        return None
```
---
### Looping and If user wants to quit calculation
```
while True:
    operator = input("Operator to use (1 for +, 2 for -, 3 for *, 4 for /, 5 for √, 6 for **, q to quit): ")
    if operator.lower() == 'q':
        print("Exiting calculator.")
        break  # Exit the loop if 'q' is entered
```
---
## For Operators that need two numbers
    if operator in ["1", "2", "3", "4", "6"]: 
        num1 = input("The First Number: ")
        num2 = input("The Second Number: ")
        
        result = calculate(num1, operator, num2)
        if result is not None:
            print(f"{num1} {operator} {num2} = {result}")
    elif operator == "5":  # Square root operator, only needs one number
        num1 = input("Number to take the square root of: ")
        result = calculate(num1, operator, None)
        if result is not None:
            print(f"√{num1} = {result}")
    else:
        print("Invalid operator")
