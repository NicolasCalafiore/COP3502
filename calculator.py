# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    operandOne = float(input("Enter first operand: "));   # Gathers operand information
    operandTwo = float(input("Enter second operand: "));
    menuSelection = int(input("Calculator Menu\n---------------\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\nWhich operation do you want to perform? "))

    # Executes operator on operand depending on previous selection
    if(menuSelection == 1): print(f"The result of the operation is {operandOne + operandTwo}. Goodbye!");
    elif (menuSelection == 2):print(f"The result of the operation is {operandOne - operandTwo}. Goodbye!");
    elif (menuSelection == 3):print(f"The result of the operation is {operandOne * operandTwo}. Goodbye!");
    elif (menuSelection == 4):print(f"The result of the operation is {operandOne / operandTwo}. Goodbye!");
    else:
        print("Error: Invalid selection! Terminating program.");



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
