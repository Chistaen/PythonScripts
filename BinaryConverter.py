def convertToDecimals(binary):
    if len(binary) != 8:
        return 0

    calculations = (1, 2, 4, 8, 16, 32, 64, 128)
    result = 0
    calculation_number = 7;

    for i in binary:
        if i == '1':
            result += calculations[calculation_number]

        calculation_number -= 1;

    return result

def convertToBinary(decimals):
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

    return result

print (convertToDecimals('00010110'))
print (convertToBinary(22))
