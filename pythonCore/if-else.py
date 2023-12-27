is_active = str( input("Is the user active? "))
is_admin = str(input("Is the user administrator? "))
is_permission = str( input("Does the user have access? "))

print (is_active,is_admin,is_permission)
if is_admin == ( '1' or 'y' or 'Y' ):
    admin = True
else :
    admin = False
if is_active == ( '1' or 'y' or 'Y' ):
    active = True
else :
    active = False
if is_permission == ( '1' or 'y' or 'Y' ):
    permission = True
else :
    permission = False
print (active, admin, permission)
# access = 