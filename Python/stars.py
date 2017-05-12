x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(arr):
    for items in x:
        print "*" * items

draw_stars(x)

def draw_stars2(arr):
    for items in arr:
        if isinstance(items, int):
            print "*" * items
        elif isinstance(items, str):
            length = len(items)
            letter = items[0].lower()
            print letter * length
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print draw_stars2(x)
