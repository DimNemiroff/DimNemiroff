def factorial(n):
    n = abs(n)
    if n < 2:
        return 1
    return n * factorial(n-1)
 

if __name__ == '__main__':

    k = int(input("Input the password's length "))
    n = int(input("Input the number of possible elements "))
    v = int(input("Input speed of combing through combinations, words/s "))
    need_time = n**k/v 
    #need_time = factorial(n)/factorial(n-k)
    print(need_time)

    years = int(need_time//31536000)
    month = int((need_time%31536000)//2628000)
    days = int((need_time%31536000%2628000)//86400)
    hours = int((need_time%86400%86400)//3600)
    minut = int(need_time%3600)
    sec = int(need_time%60)

    ''' 
    years = int(need_time//31536000)
    month = int(need_time//2592000)
    days = int(need_time//86400)
    hours = int(need_time//3600)
    minut = int(need_time//60-hours*60)
    sec = int(need_time%60)
    '''
    print(f"{years} років",f"{month} місяців",f"{days} днів",f"{hours} годин",f"{minut} хвилин",f"{sec} секунд")