import os
from console_gfx import ConsoleGfx

# Displays main menu
def Menu_Display():  
    print("\nRLE Menu\n--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")

# Returns list of Gfx loaded file
def Load_File():  
    fileName = input("Enter name of file to load:")
    script_dir = os.path.dirname(os.path.abspath(__file__)) # Credit: https://www.tutorialspoint.com/How-to-open-a-file-in-the-same-directory-as-a-Python-script
    file_path = os.path.join(script_dir, fileName)
    return ConsoleGfx.load_file(file_path)

# Converts list of integers to a string of hex digits
def to_hex_string(data): 
    hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
    list = []
    for i in data:
        list.append(str(hex_list[i]))
    return ''.join(list)

# Returns number of unique elements in flat_data
def encode_rle(flat_data): 
    compressed_list = []
    counter = 1
    index = 0
    while index < len(flat_data):
        for j in range(index + 1, len(flat_data)): # Evaluates all elements after the current element
            if(flat_data[index] == flat_data[j]):
                counter += 1
                if counter == 15:
                    break
            else:
                break
        compressed_list.extend([counter, flat_data[index]])
        index += counter
        counter = 1
    return compressed_list

# Returns the number of runs in flat_data
def count_runs(flat_data):
    runs = 0
    index = 0
    while index < len(flat_data):
        counter = 1
        for j in range(index + 1, len(flat_data)): # Evaluates all elements after the current element
            if int(flat_data[index]) == int(flat_data[j]):
                counter += 1
                if counter == 15:
                    break
            else:
                break
        index += counter 
        runs += 1
    return runs

# Returns the length of the decoded RLE data
def get_decoded_length(rle_data):
    return sum(rle_data[::2])

# Decodes RLE data
def decode_rle(rle_data):
    flat_data = []
    counters = rle_data[::2]
    values = rle_data[1::2]
    for i in range(len(counters)):
        flat_data.extend([values[i]] * counters[i])
    return flat_data

# Converts a string of hex digits to a list of integers
def string_to_data(data_string):
    index = 0
    hex_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    string_list = []
    while index < len(data_string):
        string_list.append(hex_list.index(data_string[index])) # Adds value that corresponds to the index of the hex digit in the hex_list
        index += 1
    return string_list





######

# Translates RLE data into a human-readable representation
def to_rle_string(rle_data):
    rle_string = ""
    for i in range(0, len(rle_data), 2):
        rle_string += str(rle_data[i]) + hex(rle_data[i+1])[2:] + ":"
    return rle_string[:-1]

# Translates a string in human-readable RLE format (with delimiters) into RLE byte data
def string_to_rle(rle_string):
    rle_data = []
    rle_list = rle_string.split(":")
    for i in range(len(rle_list)):
        rle_data.append(int(rle_list[i][:-1]))
        rle_data.append(int(rle_list[i][-1], 16))
    return rle_data

# Main function that runs the program
def main():
    imageData = None
    RLE_STRING_STORAGE = None
    RLE_HEX_STRING_STORAGE = None


    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image: ")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print("\n")
    while True:  # Program loop
        Menu_Display()  # Displays main menu
        menuSelect = int(input("\nSelect a Menu Option: "))


        if menuSelect == 0:  # Exit
            break
        elif menuSelect == 1:  # Load file
            imageData = Load_File()
        elif menuSelect == 2:  # Load test file
            print("Test image data loaded. ")
            imageData = ConsoleGfx.test_image
        elif menuSelect == 3:  # Read RLE String
            RLE_STRING_STORAGE = input("Enter an RLE string to be decoded: ")

        elif menuSelect == 4:  # Load RLE Hex String
            RLE_HEX_STRING_STORAGE = input("Enter the hex string holding RLE data: ")
    
        elif menuSelect == 5:  # Load Data Hex String
            hex_string = input("Enter the hex string holding flat data: ")
            flat_data = string_to_data(hex_string)
            RLE_Data_Hex = flat_data
    
        elif menuSelect == 6:  # Display Image
            print("Displaying image...")
            if imageData == None:
                print("(no data)")
            else: 
                ConsoleGfx.display_image(imageData)
        elif menuSelect == 7:  # Display RLE String
            if RLE_HEX_STRING_STORAGE == None:
                print("(no data)")
            else:
                data = string_to_data(RLE_HEX_STRING_STORAGE)
                rle_string= to_rle_string(data)
                print(f'RLE representation: {rle_string}')

        elif menuSelect == 8:  # Display Hex RLE Data    
            if RLE_STRING_STORAGE == None:
                print("(no data)")
            else:
                rle_data = string_to_rle(RLE_STRING_STORAGE)
                hex_string = to_hex_string(rle_data)
                print(f'RLE hex values: {hex_string}')

        elif menuSelect == 9:  # Display Hex Flat Data
            if RLE_STRING_STORAGE == None:
                print("(no data)")
            else: 
                rle_data = string_to_rle(RLE_STRING_STORAGE)
                flat_data = decode_rle(rle_data)
                result = ''.join(str(x) for x in flat_data)
                print(f'Flat hex values: {result}')

        else:
            print("Error! Invalid input.")

if __name__ == '__main__':
    main()
