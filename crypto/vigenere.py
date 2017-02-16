from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    new_string=""
    key_index=-1
    for idx in range(len(text)):
        if text[idx].isalpha():
            key_index=(key_index +1)%len(key)
            rot=alphabet_position(key[key_index])
            new_string=new_string + rotate_character(text[idx],rot)
        else:
            new_string=new_string + text[idx]
    return new_string


def main():
    print(encrypt(input("Type a message:"), input("Encryption key:")))
if __name__ == '__main__':
    main()
