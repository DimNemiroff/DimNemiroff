def check_password(credentials):
    global user
    attempts = 3
    while attempts >= 1:
        passw = input("Enter your password, please:")
        if passw in credentials.values():
            i = list(credentials.values()).index(passw)
            user = list(credentials.keys())[i]
            break
        else:
            if attempts > 1:
                attempts -= 1
                print(f"Sorry, password is invalid. Try again!\n{attempts} attempt(s) left")
            else: break
    if user not in credentials:
        user = 'Intruder'
    return user



def check_auth_code(expected_auth_code):
    auth_code = input("Enter authentication code, please: ")
    return  auth_code == expected_auth_code 



credentials = {"Alice" :'C00peR', "Bob" : 'uNc1e' , "Carl" :'ClariNet'}
expected_auth_code = '1111'
user = None

user = check_password(credentials)
if user in credentials and check_auth_code(expected_auth_code):
    print(f"Welcome, {user}! It's nice to see you again")
else:
    print("Sorry, I don't know you")            
