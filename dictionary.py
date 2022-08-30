from multiprocessing.sharedctypes import Value


vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'fiesta': 'Ford fiesta',
}

# add
vehicles["starfigther"] = "Lokhead F-10"

# delete
del vehicles["er5"]

for key, value in vehicles.items():
    print(key, value, sep = ", ")