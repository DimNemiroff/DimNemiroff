def power (a,b):
    if b >= 1 :    
        return a * power(a,b-1)
    return 1 
#if __name__ == '__main__':

    while True:
        x = int( input('Input Base, 0 - if you want to exit '))
        if x == 0 :
            if input("You really exit? - y/n ") == ('y' or 'Y') :
                break
            else : 
                continue
        n = int( input('Input Exponent '))
        s = power(x,n)

        print (s)

