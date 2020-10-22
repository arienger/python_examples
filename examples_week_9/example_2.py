pet = {
    "Bob": "Cat",
    "Fred": "Dolphin",
    "Dan": "Crocodile",
    "Claire": "Stick insect",
    "Alice": "Dog",
    "Eve": "Elephant",
}

print("All owners")
for name in pet.keys():
    print(name)

print("\n\n\n")

print("All pets")
for animal in pet.values():
    print(animal)

print("\n\n\n")

print("All pairs")
for p in pet.items():
    print(p)

print("\n\n\n")

print("Unpack the pair tuple")
for name, animal in pet.items():
    print(f"{name} has a pet, and it is a {animal}")