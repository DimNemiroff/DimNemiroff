items = ['2 eggs' , '1 liter sugar', '1 tsp salt', 'vinegar']


def format_ingredients(items):
    line = ""
    if len(items) >= 2:
        new_list = items[0:-2]
        #new_list.extend(['and', items[-1]])
        print(new_list)
        for i in new_list:
            line = line + str(i) + ', '
        line = line + items[-2] + ' and ' + items[-1]
    elif len(items) == 1:
        line = items[0]
    else: line =""
    print(line)
    return line

format_ingredients(items)   