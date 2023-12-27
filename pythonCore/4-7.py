points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
rout = [0, 1, 3, 2, 1, 3, 2, 0]
rout1 = []


def calculate_distance(coordinates):
    distance = 0.0
    for l in range(len(coordinates)-1):
        hop_key = [coordinates[l], coordinates[l+1]]
        hop_key.sort()
        hop_tuple = (hop_key[0], hop_key[1])
        #distance += points.get(hop_tuple) 
        distance += points[hop_tuple]
    return distance




print(calculate_distance(rout))
