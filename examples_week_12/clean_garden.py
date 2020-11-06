import csv


def find_item(garden, item):
    for g in garden:
        if g[0] == item:
            return g
    return


def swap_items(garden1, garden2, pos1, pos2):
    print(garden1[0] + ' is swapped with ' + garden2[0])
    neighbors_garden.remove(garden2)
    return


def clean_garden(my_garden, neighbors_garden):
    for g in my_garden:
        if g[0] in ('rock', 'moss'):
            item = ''
            if g[0] == 'rock':
                item = 'strawberry'
            if g[0] == 'moss':
                item = 'raspberry'
            neighbors_garden_posision = find_item(neighbors_garden, item)
            if neighbors_garden_posision:
                swap_items(g, neighbors_garden_posision, neighbors_garden_posision[1], neighbors_garden_posision[2])
    print('Finish')
    return


my_garden = []
neighbors_garden = []

with open('my_garden.csv', newline='', encoding='iso-8859-1') as csvfile:
    my_gardenreader = csv.reader(csvfile, delimiter=';')
    for row in my_gardenreader:
        try:
            element = row[0]
            pos1 = float(row[1])  # latitude is second last
            pos2 = float(row[2])  # longitude is last
            gardenelement = (element, pos1, pos2)
        except ValueError:
            continue
        my_garden.append(gardenelement)

with open('neighbors_garden.csv', newline='', encoding='iso-8859-1') as csvfile:
    neighbors_gardenreader = csv.reader(csvfile, delimiter=';')
    for row in neighbors_gardenreader:
        try:
            element = row[0]
            pos1 = float(row[1])  # latitude is second last
            pos2 = float(row[2])  # longitude is last
            gardenelement = (element, pos1, pos2)
        except ValueError:
            continue
        neighbors_garden.append(gardenelement)

clean_garden(my_garden, neighbors_garden)
