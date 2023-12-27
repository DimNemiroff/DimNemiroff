def check_password(user):
    user = 'jkhzjh'
    user = 'Intruder'
    print(user)  
    #return user

user = None
check_password(user)



#Authentication user - siml prog
# Все перебрав - не можу уявити випадку, коли по пасворду тре знайти юзера... а якщо в мене декілька облікових
#записів, логіни різні, а паролі однакові, чи може бути в різних юзерів паролі співпадають (теоретично - це можливо, якщо немає
#генератора поролей)
''' 
credentials = {"Alice" :'C00peR', "Bob" : 'uNc1e' , "Carl" :'ClariNet'}
trys = 3
User = None
while trys > 0:
    passw = input("Enter your password, please:")
    if passw  in credentials.values():
        i = list(credentials.values()).index(passw)
        User = list(credentials.keys())[i]
        trys = -1
        print(User)
        break
    else:
        trys -= 1
        print(f"Sorry, password is invalid. Try again!\n{trys} attempt(s) left")
if User not in credentials:
    User = 'Intruder'
print(User)
print(f"Welcome, {User}! It's nice to see you again") if User in credentials else print("Sorry, I don't know you") 

''' 