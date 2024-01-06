"""def some_function(fc, file=''):
    line = None
    fc.write('first line\nsecond line\nthird line')
    fc.close()
    fc.open(file, 'r')
    line = fc.readlines()
    line = "".join(line)
    print(line)
    return line


with open('text.txt', 'w+') as fh:
    # res = some_function(fh, 'text.txt')
    d = fh.write('first line\nsecond line\nthird line')
    print(d)
    line = fh.readlines()
    print(line)
    line = "".join(line)
    print(line)
"""

'''
print(res)
with open('text2.txt', 'w+') as fj:
    res = some_function(fj, 'text2.txt')

print(res)
'''
fh = open('test.txt', 'w+')
fh.write('first line\nsecond line\nthird line\n')
fh = open('test.txt', 'r')
line = fh.readlines()
print(fh, line)
fh.write('fourth line\nfifth line\nsixth line')
fh = open('test.txt', 'r')
line = fh.readlines()
print(line)
line = "".join(line)
print(line)

fh.close()