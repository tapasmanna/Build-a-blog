def get_initials(fullname):
    """Given a person's name, return the person's initials(uppercase)"""
    #fullname = input('Type your name: ')
    name=fullname.split()

    initials = ''.join(name[0].upper() for name in fullname.split())
    return initials


def main():
    print(get_initials(input('Type your name: ')))
if __name__ == '__main__':
    main()
