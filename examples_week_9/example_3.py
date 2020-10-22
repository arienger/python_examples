number_name = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
}



def print_name(n):
    if n in number_name:
        print(f'{n} is called {number_name[n]}')
    else:
        print(f"I don't know what {n} is called.")
        name = input("Please tell me: ")
        number_name[n] = name

print_name(3)
print_name(56)

print_name(2)
print_name(56)