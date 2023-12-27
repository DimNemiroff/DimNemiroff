def invite_to_event(username):
    return  f"Dear {username}, we have the honour to invite you to our event"

while True:
    name = input("Name ")
    #invite_to_event(name)
    print(invite_to_event(name))