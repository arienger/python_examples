number_name_dict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'elleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eightteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred',
    200: 'two hundred',
    300: 'three hundred',
    400: 'four hundred',
    500: 'five hundred',
    600: 'six hundred',
    700: 'seven hundred',
    800: 'eight hundred',
    900: 'nine hundred',
    1000: 'thousand',
}


def number_name(N):
    if N < 20 and N in number_name_dict:
        return number_name_dict[N]

    if N < 100:
        singular = N % 10
        tens = int(((N % 100) - singular))
        if singular > 0:
            return number_name_dict[tens] + ' ' + number_name_dict[singular]
        else:
            return number_name_dict[tens]

    if N < 1001:
        singular = N % 10
        tens = int(((N % 100) - singular))
        hundreds = int(((N % 1000) - (tens * 10) - singular))
        if singular > 0:
            if tens > 0:
                return number_name_dict[hundreds] + ' ' + number_name_dict[tens] + ' ' + number_name_dict[singular]
            else:
                return number_name_dict[hundreds] + ' ' + number_name_dict[singular]
        else:
            if tens > 0:
                return number_name_dict[hundreds] + ' ' + number_name_dict[tens]
            return number_name_dict[hundreds]

    return 'invalid {N}'

    #
    #
    # houndreds = int(((N % 1000) - (tens * 10) - singular) / 100)
    # print(houndreds, tens, singular)
    # if (houndreds > 0) and (houndreds in number_name_dict):
    #     print(number_name_dict[houndreds])
    # if (tens > 0) and (((tens*10)+singular) in number_name_dict):
    #     print(number_name_dict[((tens*10)+singular)])
    # if (singular > 0) and (singular in number_name_dict):
    #     print(number_name_dict[singular])

    # if N in number_name_dict:
    #     return number_name_dict[N]


for i in range(100, 1001):
    print(number_name(i))
