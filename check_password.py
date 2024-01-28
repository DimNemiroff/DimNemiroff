

def check_password(credentials):
    global user
    trys = 3
    while trys >= 1:
        passw = input("Enter your password, please:")
        if passw  in credentials.values():
            i = list(credentials.values()).index(passw)
            user = list(credentials.keys())[i]
            break
        else:
            if trys > 1:
                trys -= 1
                print(f"Sorry, password is invalid. Try again!\n{trys} attempt(s) left")
            else: break
    if user not in credentials:
        user = 'Intruder'
    return user



credentials = {"Alice" :'C00peR', "Bob" : 'uNc1e' , "Carl" :'ClariNet'}
user = None
   
user = check_password(credentials)
print(f"Welcome, {user}! It's nice to see you again") if user in credentials else print("Sorry, I don't know you")      
