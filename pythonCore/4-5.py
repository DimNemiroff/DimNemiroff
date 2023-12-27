data1 = {1:'odin', 2: 'dwa', 3: 'tri', 4: 'odin'}
data2 = {}
#mylist = ['dwa']



def lookup_key(data, value):
    my_list = []
    for key in data:
        if data[key] == value:
            my_list.append(key)
    return my_list

print(lookup_key(data1, 'odin'))
