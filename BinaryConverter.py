# *** Binary Converter ***
# Convert integers to binary and back
#
# Usage:
# Binary to decimals: convert_to_decimals(string)
# Decimals to binary: convert_to_binary(integer)
#
# Notes:
# - You can't convert numbers above 255 and below 0
# - Binary numbers must be passed as a string (due to a Python limitation)
#
# License: BSD

def convert_to_decimals(binary):
    if len(binary) != 8 and len (binary) != 9:
        return 0

    if len(binary) == 9:
        binary = binary[:4] + binary[4:]

    calculations = (1, 2, 4, 8, 16, 32, 64, 128)
    result = 0
    calculation_number = 7;

    for i in binary:
        if i == '1':
            result += calculations[calculation_number]

        calculation_number -= 1;

    return result

def convert_to_binary(decimals):
    binary = [0, 0, 0, 0, 0, 0, 0, 0]

    current_number = decimals
    binary_no = 7

    while binary_no >= 0:
        binary[binary_no] = current_number % 2
        current_number = int(current_number / 2)
        binary_no -= 1

    result = ''
    for i in binary:
        result += str(i)

    result = result[:4] + ' ' + result[4:]

    return result

def request_input():
    print ('Enter [decimals] to convert from binary to decimals. Enter [binary] to convert from decimals to binary. Press [quit] to cancel')

    type_input = input()
    if type_input == 'quit':
        return -1
    elif type_input == 'decimals':
        print ('Please enter a binary number (no spaces), with leading zeros:')

        binary_input = input()
        return convert_to_decimals(str(binary_input))
    else:
        print ('Please enter a decimal number:')

        decimal_input = input()
        return convert_to_binary(int(decimal_input))

if __name__ == '__main__':
    while True:
        result = request_input()

        if result == -1:
            print ('Goodbye!')
            break
        else:
            print ('Result:', result)
