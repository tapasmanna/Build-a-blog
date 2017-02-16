from sys import argv, exit
from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    position = 0
    output_string = ""
    while(position < len(text)):
        newchar = rotate_character(text[position],rot)
        output_string = output_string + newchar
        position = position + 1
    return output_string


def user_input_is_valid(cl_args):
    if len(cl_args) == 1 or cl_args[1].isdigit() == False or len(cl_args) > 2:
        #print("usage: python3 caesar.py n")
        #exit()
        return False
    else:
        return True

def main():
    user_input_is_valid(argv)
    exit()
    rotation = int(argv[1])
    message = input("Type a message: \n")
    print(encrypt(message,rotation))
if __name__ == '__main__':
    main()
