def find_item(garden, item):
    for g in garden:
        if item == 'moss' and g[1] == 'raspberry':
            return g[1]
        if item == 'rock' and g[1] == 'strawberry':
            return g[1]
    return None


def swap_items(garden1, garden2, pos1, pos2):
    # print('Found, swap ' + pos1 + ' with ' + pos2)
    for my_item in garden1:
        if my_item[1] == pos1:
            for other_item in garden2:
                if other_item[1] == pos2:
                    my_item[1] = pos2
                    other_item[1] = pos1

    return


def clean_garden(my_garden, other_garden):
    for g in my_garden:
        if g[1] in ('rock', 'moss'):
            foundItem = find_item(other_garden, g[1])
            if foundItem:
                # print('Found, swap ' + g[1] + ' with ' + foundItem)
                swap_items(my_garden, other_garden, g[1], foundItem)

    return

if __name__ == "__main__":

    my_garden = [
        ["grass", "moss"],
        ["moss", "strawberry"],
        ["moss", "rock"]
    ]

    other_garden = [
        ["grass", "raspberry"],
        ["grass", "strawberry"],
        ["strawberry", "rock"]
    ]

    clean_garden(my_garden, other_garden)

    my_after = [
        ['grass', 'raspberry'],
        ['moss', 'strawberry'],
        ['moss', 'strawberry']
    ]

    other_after = [
        ['grass', 'moss'],
        ['grass', 'rock'],
        ['strawberry', 'rock']
    ]

    if my_after == my_garden and other_after == other_garden:
        print('OK!')

