import math

result = 0.0;
results = []
## Global Variables

while(1==1):
    isAcceptable = False;
    ## Displays Calculator Selection
    print(f"Current Result: {result}")
    print("Calculator Menu\n---------------")
    print("0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n")


    while not (isAcceptable): ##Loops until an acceptable selection is made OR for functions that do not require menu selection to be redisplayed
        menuSelection = int(input("Enter Menu Selection: "))
        if (menuSelection == 7 and len(results) == 0):
            print("Error: No calculations yet to average!\n")
        elif (menuSelection == 7):
            sum = 0;
            for i in results:  ## Variable Collection
                sum += i
            num = len(results);
            avg = sum / num

            ## Variable Display
            print(f"Sum of calculations: {sum}")
            print(f"Number of calculations: {num}")
            print(f"Average of calculations: {round(avg, 2)}")
        elif (menuSelection < 0 or menuSelection > 7):
            print("Error: Invalid selection!\n")
        else:
            isAcceptable = True




    ## If a normal operation is requested
    if(menuSelection != 0 and menuSelection != 7):

        operandOne = input("Enter first operand: ")
        operandTwo = input("Enter second operand: ")

        ## Lines 44-51 operand verification for any RESULT inputs.
        if(operandTwo == "RESULT"):
            if(len(results) != 0):
                operandTwo = float(results[len(results) - 1])
            else:
                operandTwo = 0.0
        if (operandOne == "RESULT"):
            if (len(results) != 0):
                operandOne = float(results[len(results) - 1])
            else:
                operandOne = 0.0

        operandOne = float(operandOne)
        operandTwo = float(operandTwo)

        if(menuSelection == 1): result = operandOne + operandTwo;
        if (menuSelection == 2): result = operandOne - operandTwo;
        if (menuSelection == 3): result = operandOne * operandTwo;
        if (menuSelection == 4): result = operandOne / operandTwo;
        if (menuSelection == 5): result = operandOne ** operandTwo;
        if (menuSelection == 6): result = math.log(operandTwo, operandOne);
        results.append(result);

    ## If exit is requested
    if(menuSelection == 0):
        print("Thanks for using this calculator. Goodbye!")
        break

