import csv

lats = []
lons = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            lat = float(row[-2])  # latitude is second last
            lon = float(row[-1])  # longitude is last
        except ValueError:
            continue
        lats.append(lat)
        lons.append(lon)

print(lats, lons)
