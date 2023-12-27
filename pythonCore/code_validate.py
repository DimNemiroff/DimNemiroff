#Checkin the pin validity

def is_valid_pin_codes(pin_codes):
    status = False
    
    if pin_codes != []:
        try:
            for i in pin_codes:
                if i.isdigit() and type(i) is str and len(i) == 4 and pin_codes.count(i) == 1:  #check length and list type and check numeric
                    status = True
                else:
                    raise
        except: status = False
    return status

code_list = [[],['1101', '9034', '0011'],['1101', '9034', '0011', '9034'],['1101', 0.254, '0011', '9034'],['1101', '79034', '0011'],['11F1', '9034', '0011'],[]]

for i in code_list:
    print(is_valid_pin_codes(i))

 