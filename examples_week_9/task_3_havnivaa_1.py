def read_file(filename):
    with open(filename, encoding="utf8") as f:
        thislist = []
        for line in f:
            words = line.split()
            thistuple = (words[0], words[1], words[2], words[3], words[4])
            thislist.append(thistuple)

    return thislist


def average(data, month=None):
    cm = 0
    counter = 0
    for t in data:
        if month is None:
            cm += int(t[4])
            counter += 1
        else:
            if month == int(t[1]):
                cm += int(t[4])
                counter += 1

    return cm / counter


def add_weekday(data):
    weekdays = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    thislist = []
    for t in data:
        yearvar = int(t[0])
        monthvar = int(t[1])
        dayvar = int(t[2])
        import datetime
        x = datetime.datetime(yearvar, monthvar, dayvar)
        dayvar = weekdays[x.weekday()]
        thistuple = (t[0], t[1], t[2], t[3], t[4], dayvar)
        thislist.append(thistuple)

    return thislist


def average_weekday(data, wkd):
    cm = 0
    counter = 0
    for t in data:
        if wkd == t[5]:
            cm += int(t[4])
            counter += 1

    return cm / counter


if __name__ == "__main__":
    data = read_file("VIK_sealevel_2000.txt")
    print(data[:5])
    annual_avg = average(data)
    print('Annual average:', annual_avg, 'cm')

    july_average = average(data, 7)
    print('July average:', july_average, 'cm')

    for month in range(1, 13):
        print(f'{month:2} average is {average(data, month):5.1f} cm')

    data_2 = add_weekday(data)
    print(data_2[:25])

    for wd in ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
        avg = average_weekday(data_2, wd)
        print(f'{wd}: {avg:5.1f} cm.')
