# Lab 6 -- Author: Paul Chojecki
# Group 38: Paul Chojecki (owner) and Divya Puthanveetil (partner)
# 10/19/2023

# initialize constants
SELECTION_ENCODE = 1
SELECTION_DECODE = 2
SELECTION_QUIT = 3


def encode(arr):
    '''
    :param arr: integer representing password
    :return: returns encoded password
             encoding is performed by adding the encrpytion key to each digit of the password
             if the digit exceeds 10 then the encoded digit loops around
             i.e. 0 -> 1 -> 2 -> ... -> 8 -> 9 -> 0 -> ....etc.
    '''

    ENCRYPTION_KEY = 3

    arr_str = ''
    arr_encoded = [(int(elem) + ENCRYPTION_KEY) % 10 for elem in str(arr)]
    for i in arr_encoded:
        arr_str += str(i)
    return int(arr_str)


def decode(encoded):
    # creates a list of the digits in the encoded password
    encoded_list = list(str(encoded))
    decoded = []

    # iterates through the encoded digits and subtracts 3
    # adds the new digits to the decoded list
    for item in encoded_list:
        if (int(item) - 3 >= 0):
            decoded.append(str(int(item) - 3))
        else:
            decoded.append(str(int(item) - 3 + 10))

    # makes the decoded list into a string and then casts to an integer
    decoded_str = ''.join(decoded)
    return int(decoded_str)


def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


if __name__ == '__main__':
    print_menu()

    pswd = None
    pswd_encoded = None
    while (True):
        select = int(input('Please enter an option: '))

        if (select == SELECTION_ENCODE):  # option 1 -- encode
            pswd = int(input('Please enter your password to encode: '))
            pswd_encoded = encode(pswd)
            print('Your password has been encoded and stored!')

        elif (select == SELECTION_DECODE):
            print(f'The encoded password is {pswd_encoded}, and the original password is {decode(pswd_encoded)}.')

        else:  # option 3 -- assumes no invalid inputs
            break

        print_menu()
