import os
import math
def convertions():
    print("PERFORMING CONVERTIONS")
    def hexa_binary_system():
        return '123456789ABCDEF'

    def to_decimal(from_, base):
        result = 0
        int_part = from_[0]
        n = len(int_part) - 1
        for i in range(len(int_part)):
            if int_part[i].isalpha():
                val = hexa_binary_system().find(int_part[i]) + 1
            else:
                val = int(int_part[i])
            result += val * (base ** n)
            n -= 1

        if len(from_) > 1:
            res = 0.0
            decimal_part = from_[1]
            n = -1
            for i in range(len(decimal_part)):
                if decimal_part[i].isalpha():
                    val = int(hexa_binary_system().find(decimal_part[i]) + 1)
                else:
                    val = int(decimal_part[i])
                res += (val * (base ** n))
                n += -1
            return float(result) + res
        return result

    def from_decimal(from_, base):
        result = ''
        dividend = int(from_[0])
        precision = 4
        while dividend >= 1:
            quoient, remainder = divmod(dividend, base)
            dividend = quoient
            if remainder >= 10:
                remainder = hexa_binary_system()[remainder - 1]
            result = str(remainder) + result

        if len(from_) > 1:
            multiplicand = float('.' + from_[1])
            decimal = '.'
            for _ in range(precision):
                k = str((multiplicand * base)).split('.')
                multiplicand = float('.' + (k[1]))
                if int(k[0]) > 9:
                    k[0] = hexa_binary_system()[int(k[0]) - 1]
                decimal += k[0]

            return result + decimal
        return result

    def binarytooctal(binarynum):
        octaldigit = 0
        octalnum = []
        i = 0
        mul = 1
        chk = 1
        while binarynum != 0:
            rem = binarynum % 10
            octaldigit = octaldigit + (rem * mul)
            if chk % 3 == 0:
                octalnum.insert(i, octaldigit)
                mul = 1
                octaldigit = 0
                chk = 1
                i = i + 1
            else:
                mul = mul * 2
                chk = chk + 1
            binarynum = int(binarynum / 10)

        if chk != 1:
            octalnum.insert(i, octaldigit)

        print("\nEquivalent Octal Value = ", end="")
        while i >= 0:
            print(str(octalnum[i]), end="")
            i = i - 1
        print()

    def to_binary(val, base):
        result = ''
        i = 0
        j = 0
        while i < base - 1:
            i += 2 ** j
            j += 1

        for i in range(len(val) - 1, -1, -1):
            convertdecimal = to_decimal(val[i].split('.'), base)
            convertdecimal = str(convertdecimal).split('.')
            tobinary = from_decimal(convertdecimal, 2)
            l = j - len(tobinary)
            for _ in range(l):
                tobinary = '0' + tobinary
            result += tobinary + result
        return result[j: len(result)]

    def octaltohexadecimal(n):
        chk = 0
        i = 0
        decnum = 0
        while octnum != 0:
            rem = octnum % 10
            if rem > 7:
                chk = 1
                break
            decnum = decnum + (rem * (8 ** i))
            i = i + 1
            octnum = int(octnum / 10)

        if chk == 0:
            i = 0
            hexdecnum = []
            while decnum != 0:
                rem = decnum % 16
                if rem < 10:
                    rem = rem + 48
                else:
                    rem = rem + 55
                rem = chr(rem)
                hexdecnum.insert(i, rem)
                i = i + 1
                decnum = int(decnum / 16)

            print("\nEquivalent Hexadecimal Value is: ")
            i = i - 1
            while i >= 0:
                print(end=hexdecnum[i])
                i = i - 1
            print()

        else:
            print("\nInvalid Input!")

    def hexadecimaltooctal(hex):
        oct = ""
        dec = i = 0
        c = len(hex) - 1

        # loop to extract each digit of number
        while i < len(hex):

            # digit extracted
            d = hex[i]
            if d == '0' or d == '1' or d == '2' or \
                    d == '3' or d == '4' or d == '5':
                dec = dec + int(d) * int(math.pow(16, c))
            elif d == '6' or d == '7' or d == '8' or d == '9':
                dec = dec + int(d) * int(math.pow(16, c))
            elif (d == 'A') or (d == 'a'):
                dec = dec + 10 * int(math.pow(16, c))
            elif (d == 'B') or (d == 'b'):
                dec = dec + 11 * int(math.pow(16, c))
            elif (d == 'C') or (d == 'c'):
                dec = dec + 12 * int(math.pow(16, c))
            elif (d == 'D') or (d == 'd'):
                dec = dec + 13 * int(math.pow(16, c))
            elif (d == 'E') or (d == 'e'):
                dec = dec + 14 * int(math.pow(16, c))
            elif (d == 'F') or (d == 'f'):
                dec = dec + 15 * int(math.pow(16, c))
            else:
                print("invalid input")
                break
            i += 1
            c -= 1

    def bin_to_hexadecimal(n):
        bnum = int(n)
        temp = 0
        mul = 1

        count = 1
        # char array to store hexadecimal number
        hexaDeciNum = ['0'] * 100

        # counter for hexadecimal number array
        i = 0
        while bnum != 0:
            rem = bnum % 10
            temp = temp + (rem * mul)

            # check if group of 4 completed
            if count % 4 == 0:

                # check if temp < 10
                if temp < 10:
                    hexaDeciNum[i] = chr(temp + 48)
                else:
                    hexaDeciNum[i] = chr(temp + 55)
                mul = 1
                temp = 0
                count = 1
                i = i + 1

            # group of 4 is not completed
            else:
                mul = mul * 2
                count = count + 1
            bnum = int(bnum / 10)

        # check if at end the group of 4 is not
        # completed
        if count != 1:
            hexaDeciNum[i] = chr(temp + 48)

        # check at end the group of 4 is completed
        if count == 1:
            i = i - 1

        # printing hexadecimal number
        # array in reverse order
        print("\n Hexadecimal equivalent of {}:  ".format(n), end="")
        while i >= 0:
            print(end=hexaDeciNum[i])
            i = i - 1

    def from_binary(binarynum):
        octaldigit = 0
        octalnum = []
        i = 0
        mul = 1
        chk = 1
        while binarynum != 0:
            rem = binarynum % 10
            octaldigit = octaldigit + (rem * mul)
            if chk % 3 == 0:
                octalnum.insert(i, octaldigit)
                mul = 1
                octaldigit = 0
                chk = 1
                i = i + 1
            else:
                mul = mul * 2
                chk = chk + 1
            binarynum = int(binarynum / 10)

        if chk != 1:
            octalnum.insert(i, octaldigit)

        print("\nEquivalent Octal Value = ", end="")
        while i >= 0:
            print(str(octalnum[i]), end="")
            i = i - 1
        print()

        # loop to find octal equivalent
        # stored in dec i.e.
        # conversion of decimal to octal.
        while (dec > 0):
            oct = "".join([str(int(dec % 8)), oct])
            dec = int(dec / 8)

        # printing the final result
        print("Equivalent Octal Value =", oct)

    def octal_to_hexadecimal(octal_number):
        # Split integer and fractional parts
        integer_part, _, fractional_part = str(octal_number).partition('.')

        # Convert integer part to decimal
        decimal_integer = int(integer_part, 8)

        # Convert fractional part to decimal
        decimal_fractional = 0.0
        if fractional_part:
            decimal_fractional = sum(int(digit) * 8 ** (-i - 1) for i, digit in enumerate(fractional_part))

        # Combine integer and fractional parts in decimal
        decimal_number = decimal_integer + decimal_fractional

        # Convert decimal to hexadecimal
        hexadecimal_integer = hex(int(decimal_integer)).replace("0x", "").upper()
        fractional_hexadecimal = ""

        if decimal_fractional > 0:
            fractional_hexadecimal = "."
            precision = 8  # You can adjust the precision as needed

            for _ in range(len(fractional_part)):
                decimal_fractional *= 16
                digit = int(decimal_fractional)
                fractional_hexadecimal += hex(digit).replace("0x", "").upper()
                decimal_fractional -= digit

        # Combine integer and fractional parts in hexadecimal
        hexadecimal_number = hexadecimal_integer + fractional_hexadecimal

        return hexadecimal_number

    def hexadecimal_to_octal(hexadecimal_number):
        # Split integer and fractional parts
        integer_part, _, fractional_part = str(hexadecimal_number).partition('.')

        # Convert integer part to decimal
        decimal_integer = int(integer_part, 16)

        # Convert fractional part to decimal
        decimal_fractional = 0.0
        if fractional_part:
            decimal_fractional = sum(int(digit, 16) * 16 ** (-i - 1) for i, digit in enumerate(fractional_part))

        # Combine integer and fractional parts in decimal
        decimal_number = decimal_integer + decimal_fractional

        # Convert decimal to octal
        octal_integer = oct(int(decimal_integer)).replace("0o", "")
        fractional_octal = ""

        if decimal_fractional > 0:
            fractional_octal = "."

            for _ in range(len(fractional_part)):
                decimal_fractional *= 8
                digit = int(decimal_fractional)
                fractional_octal += str(digit)
                decimal_fractional -= digit

        # Combine integer and fractional parts in octal
        octal_number = octal_integer + fractional_octal

        return octal_number

    def hexadecimal_to_binary(hexadecimal_number):
        # Split integer and fractional parts
        integer_part, _, fractional_part = str(hexadecimal_number).partition('.')

        # Convert integer part to decimal
        decimal_integer = int(integer_part, 16)

        # Convert fractional part to decimal
        decimal_fractional = 0.0
        if fractional_part:
            decimal_fractional = sum(int(digit, 16) * 16 ** (-i - 1) for i, digit in enumerate(fractional_part))

        # Combine integer and fractional parts in decimal
        decimal_number = decimal_integer + decimal_fractional

        # Convert decimal to binary for the integer part
        binary_integer = bin(int(decimal_integer)).replace("0b", "")

        # Convert decimal to binary for the fractional part
        fractional_binary = ""
        if decimal_fractional > 0:
            fractional_binary = "."
            precision = 8  # You can adjust the precision as needed

            for _ in range(len(fractional_part) * 4):
                decimal_fractional *= 2
                digit = int(decimal_fractional)
                fractional_binary += str(digit)
                decimal_fractional -= digit

        # Combine integer and fractional parts in binary
        binary_number = binary_integer + fractional_binary

        return binary_number

    def binary_to_hexadecimal(binary_number):
        # Split integer and fractional parts
        integer_part, _, fractional_part = str(binary_number).partition('.')

        # Convert integer part to decimal
        decimal_integer = int(integer_part, 2)

        # Convert fractional part to decimal
        decimal_fractional = 0.0
        if fractional_part:
            decimal_fractional = sum(int(digit) * 2 ** (-i - 1) for i, digit in enumerate(fractional_part))

        # Combine integer and fractional parts in decimal
        decimal_number = decimal_integer + decimal_fractional

        # Convert decimal to hexadecimal for the integer part
        hexadecimal_integer = hex(int(decimal_integer)).replace("0x", "").upper()

        # Convert decimal to hexadecimal for the fractional part
        fractional_hexadecimal = ""
        if decimal_fractional > 0:
            fractional_hexadecimal = "."
            precision = 8  # You can adjust the precision as needed

            for _ in range(math.ceil(int(len(fractional_part) / 4))):
                decimal_fractional *= 16
                digit = int(decimal_fractional)
                fractional_hexadecimal += hex(digit).replace("0x", "").upper()
                decimal_fractional -= digit

        # Combine integer and fractional parts in hexadecimal
        hexadecimal_number = hexadecimal_integer + fractional_hexadecimal

        return hexadecimal_number

    def binary_to_octal(binary_number):
        # Split integer and fractional parts
        integer_part, _, fractional_part = str(binary_number).partition('.')

        # Convert integer part to decimal
        decimal_integer = int(integer_part, 2)

        # Convert fractional part to decimal
        decimal_fractional = 0.0
        if fractional_part:
            decimal_fractional = sum(int(digit) * 2 ** (-i - 1) for i, digit in enumerate(fractional_part))

        # Combine integer and fractional parts in decimal
        decimal_number = decimal_integer + decimal_fractional

        # Convert decimal to octal for the integer part
        octal_integer = oct(int(decimal_integer)).replace("0o", "")

        # Convert decimal to octal for the fractional part
        fractional_octal = ""
        if decimal_fractional > 0:
            fractional_octal = "."
            precision = 8  # You can adjust the precision as needed

            for _ in range(int(len(fractional_part) / 3)):
                decimal_fractional *= 8
                digit = int(decimal_fractional)
                fractional_octal += str(digit)
                decimal_fractional -= digit

        # Combine integer and fractional parts in octal
        octal_number = octal_integer + fractional_octal

        return octal_number
    number_systems = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']

    while True:
        print('From:')
        [print(i + 1, number_systems[i]) for i in range(len(number_systems))]
        from_ = int(input('==> '))
        print('To:')
        [print(i + 1, number_systems[i]) for i in range(len(number_systems))]
        to_ = int(input('==> '))
        option = {1: 10, 2: 2, 3: 8, 4: 16}

        print(f'\n{number_systems[from_ - 1]} to {number_systems[to_ - 1]} Convertion')
        number_ = str(input(f'Enter {number_systems[from_ - 1]} Number: '))

        print(f'{number_systems[to_ - 1]}', end='')
        if from_ == 2:
            if to_ == 1:
                print(' Number:', to_decimal(number_.split('.'), from_))
            if to_ == 3:
                print(' Number:', binary_to_octal(number_))
            if to_ == 4:
                print(' Number:', binary_to_hexadecimal(number_))
        if from_ == 1:
            print(' Number:', from_decimal(number_.split('.'), option[to_]))
        if from_ == 3:
            if to_ == 1:
                print(' Number:', to_binary(number_.split('.'), option[from_]))
            if to_ == 2:
                print(' Number:', to_decimal(number_.split('.'), option[from_]))
            if to_ == 4:
                print(' Number:', octal_to_hexadecimal(number_))
        if from_ == 4:
            if to_ == 1:
                print(' Number:', to_decimal(number_.split('.'), option[to_]))
            if to_ == 2:
                print(' Number:', hexadecimal_to_binary(number_))
            if to_ == 3:
                print(' Number:', hexadecimal_to_octal(number_))
        input("Press Enter to clear the console.")
        os.system('cls')
def operations():
    print('PERFORMING OPERATIONS')
    def process(op1, op2, op, l):
        len_max = max(len(op1), len(op2))
        print(' ', op1.rjust(l))
        print(op, op2.rjust(l))
        print(' ', ('-' * len_max).rjust((l)))

    def DecimalOperation(op1, op2, op):
        len_max = max(len(op1), len(op2))
        calc = eval(op1 + op + op2)
        process(op1, op2, op, len(str(calc)))
        print('   ', str(calc).rjust(len_max))

    def BinaryAddition(op1, op2, op):
        result = ''
        len_max = max(len(op1), len(op2))
        a = [op1.zfill(len_max), op2.zfill(len_max)]
        carry = 0

        for i in range(len_max - 1, -1, -1):
            k = carry
            for j in range(len(a)):
                calc = k + int(a[j][i])
                if calc == 2:
                    carry = 1
                    k = 0
                else:
                    k = calc
                if j == len(a) - 1:
                    result = str(k) + result
        if carry == 1:
            result = str(carry) + result
        process(op1, op2, op, len(result))
        print(' ', result.rjust(len(result)))

    def BinarySubtraction(op1, op2, op):
        result = ''
        len_max = max(len(op1), len(op2))
        op1 = op1.zfill(len_max)
        op2 = op2.zfill(len_max)
        borrow = 0

        for i in range(len_max - 1, -1, -1):
            bit1 = int(op1[i])
            bit2 = int(op2[i])
            diff = bit1 - bit2 - borrow

            if diff < 0:
                diff += 2
                borrow = 1
            else:
                borrow = 0

            result = str(diff) + result
        process(op1, op2, op, len_max)
        print(' ', result.lstrip('0').rjust(len_max))  # Remove leading zeros from the result

    def BinaryMultiplication(op1, op2, op):
        a = []
        len_max = max(len(op1), len(op2))
        for i in range(len(op2) - 1, -1, -1):
            l = ''
            for j in range(len(op1) - 1, -1, -1):
                l = str(int(op2[i]) * int(op1[j])) + l
            a.append(l + (' ' * ((len(op2) - 1) - i)))
        max_len = max(a)
        process(op1, op2, op, len(max_len))

        for i in a:
            print(' ', i.rjust(len(max_len)))
        if len(a) > 1:
            print(' ', '-' * (len(max_len)))
            print('', bin(int(op1, 2) * int(op2, 2))[2:].rjust(len(max_len)))

    def BinaryDivision(op1, op2):
        operand1 = int(op1, 2)
        operand2 = int(op2, 2)
        res = (eval(f'{operand1} / {operand2}'))
        res = bin(res)[2:]
        print(res)

    def OctalAddition(octal1, octal2):
        # Function to add two octal numbers
        carry = 0
        result = []

        # Pad the shorter number with leading zeros to make them of equal length
        max_length = max(len(octal1), len(octal2))
        octal1 = octal1.zfill(max_length)
        octal2 = octal2.zfill(max_length)

        for digit1, digit2 in zip(reversed(octal1), reversed(octal2)):
            digit1 = int(digit1, 8)  # Convert octal digit to decimal
            digit2 = int(digit2, 8)  # Convert octal digit to decimal
            sum_digit = (digit1 + digit2 + carry) % 8
            carry = (digit1 + digit2 + carry) // 8
            result.append(oct(sum_digit).lstrip('0o'))

        if carry:
            result.append(oct(carry).lstrip('0o'))

        print("".join(reversed(result)))

    def OctalSubtraction(octal1, octal2):
        # Function to subtract two octal numbers
        borrow = 0
        result = []

        # Pad the shorter number with leading zeros to make them of equal length
        max_length = max(len(octal1), len(octal2))
        octal1 = octal1.zfill(max_length)
        octal2 = octal2.zfill(max_length)

        for digit1, digit2 in zip(reversed(octal1), reversed(octal2)):
            digit1 = int(digit1, 8)  # Convert octal digit to decimal
            digit2 = int(digit2, 8)  # Convert octal digit to decimal

            if digit1 < digit2 + borrow:
                sum_digit = 8 + digit1 - digit2 - borrow
                borrow = 1
            else:
                sum_digit = digit1 - digit2 - borrow
                borrow = 0

            result.append(oct(sum_digit).lstrip('0o'))

        print("".join(reversed(result)))

    def OctalDivision(dividend, divisor):
        dividend = int(dividend, 8)
        divisor = int(divisor, 8)

        quotient = dividend // divisor
        remainder = dividend % divisor

        quotient_octal = oct(quotient).lstrip('0o')
        remainder_octal = oct(remainder).lstrip('0o')

        print(quotient_octal, remainder_octal)

    def HexadecimalAddition(hex1, hex2):
        # Function to add two hexadecimal numbers
        carry = 0
        result = []

        # Pad the shorter number with leading zeros to make them of equal length
        max_length = max(len(hex1), len(hex2))
        hex1 = hex1.zfill(max_length)
        hex2 = hex2.zfill(max_length)

        for digit1, digit2 in zip(reversed(hex1), reversed(hex2)):
            sum_digit = int(digit1, 16) + int(digit2, 16) + carry
            carry = sum_digit // 16
            result.append(hex(sum_digit % 16)[2:])

        if carry:
            result.append(hex(carry)[2:])

        print("".join(reversed(result)))

    def HexadecimalSubtraction(hex1, hex2):
        # Function to subtract two hexadecimal numbers
        borrow = 0
        result = []

        # Pad the shorter number with leading zeros to make them of equal length
        max_length = max(len(hex1), len(hex2))
        hex1 = hex1.zfill(max_length)
        hex2 = hex2.zfill(max_length)

        for digit1, digit2 in zip(reversed(hex1), reversed(hex2)):
            digit1 = int(digit1, 16)  # Convert hexadecimal digit to decimal
            digit2 = int(digit2, 16)  # Convert hexadecimal digit to decimal

            if digit1 < digit2 + borrow:
                sum_digit = 16 + digit1 - digit2 - borrow
                borrow = 1
            else:
                sum_digit = digit1 - digit2 - borrow
                borrow = 0

            result.append(hex(sum_digit)[2:])

        print("".join(reversed(result)))

    def HexadecimalMultiplication(hex1, hex2):
        hex1 = int(hex1, 16)
        hex2 = int(hex2, 16)

        product = hex1 * hex2

        product_hex = hex(product)[2:]

        print(product_hex)

    def HexadecimalDivision(dividend, divisor):
        dividend = int(dividend, 16)
        divisor = int(divisor, 16)

        quotient = dividend // divisor
        remainder = dividend % divisor

        quotient_hex = hex(quotient)[2:]
        remainder_hex = hex(remainder)[2:]

        print(quotient_hex, remainder_hex)

    print('Number System Operations')
    number_system = {'Binary': {'Addition': BinaryAddition,
                                'Subtraction': BinarySubtraction,
                                'Multiplication': BinaryMultiplication,
                                'Division': BinaryDivision},
                     'Decimal': DecimalOperation,
                     'Octal': {'Addition': OctalAddition,
                               'Subtraction': OctalSubtraction,
                               'Multiplication': '',
                               'Division': OctalDivision},
                     'Hexadecimal': {'Addition': HexadecimalAddition,
                                     'Subtraction': HexadecimalSubtraction,
                                     'Multiplication': HexadecimalMultiplication,
                                     'Division': HexadecimalDivision
                                     }
                     }

    print(f'Please Input Operation to Perform ')
    print('Sample Input: Binary Addition')
    activity = input('--> ').split(' ')
    op1 = str(input('First Operand: '))
    op2 = str(input('Second Operand: '))
    d = {'Addition': '+', 'Subtraction': '-', 'Multiplication': 'x', 'Division': '/'}
    number_system[activity[0]][activity[1]](op1, op2, d[activity[1]])

def main():
    print('NUMBER SYSTEM')
    opt = {1: [convertions, 'Convertions'], 2: [operations, 'Operations']}
    for key, val in opt.items():
        print(f'{key}. {val[1]}')
    user_choice = int(input('Select Activity: '))
    opt[user_choice][0]()

if __name__ == '__main__':
    main()

