terra1 = [[1, 1, 5, 10], [11, 2], [1, 1, 1]]
terra2 = []
power = 1




def game(terra, power):
    for block in terra:
        for bon in block:
            if bon <= power:
                power += bon 
            else:
                break
    return power            



print(game(terra2, power))