pet = {
    'Alice' : 'Dog',
    'Bob' : 'Cat',
    'Claire' : 'Stick insect',
    'Dan' : 'Crocodile',
    'Eve' : 'Elephant',
    'Fred' : 'Dolphin'
}

print('All pets',pet)

print(pet['Alice'])
print(pet['Eve'])

pet['Xavier'] = 'Alien'

print(pet)

print(pet['Karl']) # KeyError
