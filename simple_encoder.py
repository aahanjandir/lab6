# Aahan Jandir

def menu():
    print('MENU')
    print(13* '-')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(num):
    num_list = list(num)
    for i in range(len(num_list)):
        num_list[i] = str(int(num[i]) + 3)
    return ''.join(num_list)
def decode(num):
    num_list = list(num)
    for i in range(len(num_list)):
        num_list[i] = str(int(num[i]) - 3)
    return ''.join(num_list)

def main(): 
    x = True
    while x == True:
        menu()
        user_option = input('Please enter an option: ')
        if user_option == '1':
            user_num = (input('Please enter your password to encode: '))
            encoded_password = encode(user_num)
            print('Your password has been encoded and stored!')

        if user_option == '2':
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')

        if user_option == '3':
            x = False


main()
