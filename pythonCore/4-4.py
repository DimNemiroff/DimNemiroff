rate_num = {'A': 5, 'B': 5, 'C': 4, 'D': 3, 'E': 3, 'FX':2, 'F':1 }
rate_desc = {'A': 'Perfectly', 'B': 'Very good', 'C': 'Good', 'D': 'Satisfactorily', 'E': 'Enough', 'FX':'Unsatisfactorily', 'F':'Unsatisfactorily'}
key = None

def get_grade(key):
    return rate_num.get(key)

    


def get_description(key):
    return rate_desc.get(key)


key = input ()

print (f'Buh {get_grade(key)} level {get_description(key)}')

