import pathlib

p = pathlib.Path('C:\\')

for i in p.iterdir():
    print(i.name)
print(p.parent, p.name, p.suffix)
