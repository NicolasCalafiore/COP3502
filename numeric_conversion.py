# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_menu(): # Prints Menu
    print("Decoding Menu\n-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit\n")


def reverse_list(list): # Reverse the order of a list
    size = len(list) - 1
    increment = 0
    newList = []
    while increment <= size:
        newList.append(list[size - increment])
        increment += 1
    return newList

def hex_string_decode(string):
    # Convert each character in the string to its decimal equivalent
    elements = []
    for letter in string:
        letter = letter.upper()
        element = hex_char_decode(letter)
        elements.append(element)

    # Reverse the list of decimal values
    elements = reverse_list(elements)

    # Remove the '0x' prefix if it exists
    if(elements[len(elements) - 1] == 0 and elements[len(elements) - 2] == "X"):
        elements.pop(len(elements) - 2)
        elements.pop(len(elements) - 1)

    # Sums the list of decimal values to a single integer
    increment = 0
    sum = 0
    while increment < len(elements):
        sum += int(elements[increment]) * 16**increment
        increment += 1

    return sum




def binary_string_decode(binary):
    # Convert each character in the string to its decimal equivalent
    elements = []
    for letter in binary:
        letter = letter.upper()
        elements.append(letter)

    # Reverse the list of binary digits
    elements = reverse_list(elements)

    # Remove the '0b' prefix if it exists
    if(elements[len(elements) - 1] == "0" and elements[len(elements) - 2] == "B"):
        elements.pop(len(elements) - 2)
        elements.pop(len(elements) - 1)

    # Sums the list of binary digits to a single integer
    increment = 0
    sum = 0
    while increment < len(elements):
        if int(elements[increment]) == 1:
            sum += 2**increment
        increment += 1

    return sum



def binary_to_hex(binary):
    decimal = 0
    power = 0
    # Iterate over each digit in the binary string in reverse order
    for digit in reverse_list(binary):
        # Convert the digit to an integer and add it to the decimal value
        decimal += int(digit) * 2 ** power
        # Increment the power of 2 for the next digit
        power += 1

    # Define a string of hexadecimal characters
    hex_chars = "0123456789ABCDEF"
    hex_string = ""
    # Convert the decimal value to a hexadecimal string
    while decimal > 0:
        remainder = decimal % 16
        hex_string = hex_chars[remainder] + hex_string
        decimal //= 16

    return hex_string


def hex_char_decode(hex): # Receives a hex value. If integer returns same value. If char returns equivalent integer.
    hex = hex.upper()
    if hex == "A":
        return 10
    elif hex == "B":
        return 11
    elif hex == "C":
        return 12
    elif hex == "D":
        return 13
    elif hex == "E":
        return 14
    elif hex == "F":
        return 15
    elif hex == "0":
        return 0
    else:
        return hex


if __name__ == '__main__':
    # Loop until the user chooses to exit
    while True:
        # Display the menu options
        print_menu()
        # Get the user's menu selection
        menuSelection = int(input("Please enter an option: "))
        # Exit if the user chooses option 4
        if menuSelection == 4:
            print("Goodbye!")
            break
        # Get the numeric string to convert from the user
        numericString = input("Please enter the numeric string to convert: ")
        # Convert the numeric string based on the user's menu selection
        if menuSelection == 1:
            print(f'Result: {hex_string_decode(numericString)}')
        if menuSelection == 2:
            print(f'Result: {binary_string_decode(numericString)}')
        if menuSelection == 3:
            print(f'Result: {binary_to_hex(numericString)}')
        print("\n")
