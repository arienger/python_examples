def find_item(garden, item):
    # din kode her
    return None


def swap_items(garden1, garden2, pos1, pos2):
    # din kode her
pass


def clean_garden(my_garden, neighbors_garden):


    """
    Bytt ut all "rock" med "strawberry", og "moss" med "raspberry" fra naboen sin hage
    så lenge det finnes muligheter for bytte.

    Args:
    my_garden - din hage
    neighbors_garden - naboen sin hage
    """
# din kode her
pass

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
