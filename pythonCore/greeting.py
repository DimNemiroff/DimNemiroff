def g_n():
    name = input('Write your name ')
    return name


def greet(name):
    print(f'Hello {name}')


def main():
    name = g_n()
    greet(name)

print(f'__name__1 = {__name__}')
if (__name__ == '_main__'):
    print(f'__name__2 = {__name__}')
      
    main()
else: print(f'__name__3 = {__name__}')