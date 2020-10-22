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
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
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
    1000: 'one thousand',
}


def number_name(N):
    if N < 20 and N in number_name_dict:
        return number_name_dict[N]
    elif N < 100:
        singular = N % 10
        # print(singular)
        tens = int(((N % 100) - singular))
        # print(tens)
        if singular > 0:
            return number_name_dict[tens] + '-' + number_name_dict[singular]
        else:
            return number_name_dict[tens]
    elif N < 1001:
        if N == 1000:
            return number_name_dict[N]
        singular = N % 10
        # print(singular)
        tens = int(((N % 100) - singular))
        # print(tens)
        hundreds = int(((N % 1000) - tens - singular))
        # print(hundreds)
        if singular > 0:
            if tens > 0:
                if tens < 11:
                    return number_name_dict[hundreds] + ' and ' + number_name_dict[(tens + singular)]
                else:
                    return number_name_dict[hundreds] + ' and ' + number_name_dict[tens] + '-' + number_name_dict[
                        singular]
            else:
                return number_name_dict[hundreds] + ' and ' + number_name_dict[singular]
        else:
            if tens > 0:
                if tens < 11:
                    return number_name_dict[hundreds] + ' and ' + number_name_dict[(tens + singular)]
                else:
                    return number_name_dict[hundreds] + ' and ' + number_name_dict[tens]
            else:
                return number_name_dict[hundreds]

    return 'invalid {N}'


# print(number_name(735))
# return ""
def all_numbernames(N):
    lengde = 0
    name = ""
    for i in range(1, N + 1):
        name = name + " " + number_name(i)
    ny_string = ""
    for k in name:
        if k != " " and k != "-":
            ny_string += k

    return (len(ny_string))

def solve_euler_17():
    return all_numbernames(1000)

# for i in range(1, 1001):
#     print(number_name(i))

# koden nedover er ikke en del av løsning og
# brukes ikke i automatisk vurdering. Du kan endre eksemplene eller
# legge til input() / print() her om du vil, under if __name__...
if __name__ == "__main__":
    if number_name(12) == "twelve":
        print('Yay!')
else:
    print('Oh! I thought it was twelve')

if number_name(115) == 'one hundred and fifteen':
    print('115 works')
else:
    print('115 is broken')

if number_name(342) == 'three hundred and forty-two':
    print('342 works')
else:
    print('342 is broken')

if all_numbernames(5) == len("one" + "two" + "three" + "four" + "five"):
    print('up to 5 works')
else:
    print('up to 5 is broken')

if all_numbernames(115) == 1133:
    print('up to 115 works')
else:
    print('up to 115 is broken')

if all_numbernames(342) == 6117:
    print('up to 342 works')
else:
    print('up to 342 is broken')

if solve_euler_17() == 21124:
   print('Good! You solved Euler 17')
else:
   print('Try some more')
