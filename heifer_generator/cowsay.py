import sys
from heifer_generator import HeiferGenerator
from file_cow import FileCow

def list_cows(cows):    # Prints out all cow names
    print("Cows available:", end=" ")
    for cow in cows:
        print(cow.name, end = " ")
    print("File cows available: turkey moose turtle tux ")

def find_cow(name, cows):   # Finds cow with given name
    for cow in cows:
        if cow.name == name:
            return cow
    return None

def main(): # Main function
    cows = HeiferGenerator.get_cows()
    cow_files = [FileCow("moose", "moose"), FileCow("turkey", "turkey"), FileCow("turtle", "turtle"), FileCow("tux", "tux")]


    if(sys.argv[1] == "-l"):  # If -l is passed, list cows
        list_cows(cows)
    elif(sys.argv[1] == "-n"): # If -n is passed, find cow with given name
        print()
        cow = find_cow(sys.argv[2], cows)  # Find cow with given name
        if(cow != None):
            print(' '.join(sys.argv[3:])) # Print out the rest of the arguments
            print(cow.image)
            if(cow.can_breathe_fire): 
                print("This dragon can breathe fire.")
            else:
                print("This dragon cannot breathe fire.")
        else:
            print(f'Could not find {sys.argv[2]} cow!') 
    elif(sys.argv[1] == "-f"):
        cow_file_name_a = sys.argv[2]
        isFound = False
        for cow_file in cow_files:
            if(cow_file.name == cow_file_name_a):
                isFound = True
                message = ' '.join(sys.argv[3:])
                print(message)
                print(cow_file.image)
                break

        if not isFound:
            print(f'Could not find {sys.argv[2]} cow!')
        


    else:
        print()
        print(' '.join(sys.argv[1:]))
        print(cows[0].image)
        


if __name__ == '__main__':
    main()
