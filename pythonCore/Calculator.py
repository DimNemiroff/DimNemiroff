result = None
operand = None
operator = None
wait_for_number = True
while True:
    if result == None : result = 0
    #print ('begin', operand,operator, wait_for_number, result)
    try :
        if wait_for_number == False :
            operator = input('enter operator ')
            if operator in ('+' , '-' , '*' , '/') : 
                wait_for_number = True
            elif operator not in ( '+' , '-' , '*' , '/' , '=' ) :
                raise Exception 
            #print( operator )
        elif wait_for_number == True :
            operand = input('enter number ')
            operand = float (operand)
            if operator == None : result = result + operand
            if operator == '+' : result = result + operand
            if operator == '-' : result = result - operand
            if operator == '*' : result = result * operand
            if operator == '/' : result = result / operand 
            wait_for_number = False
            #print(operand, result)
    except ValueError :
        print ( operand, ' - is not a number. Try again.')
        operand = None          # debug
    except ZeroDivisionError :
        print ( operator, 'cannot be divided by zero. Try again.')
        operand = None
    except Exception :
        print ( operator, ' - is not a operator. Try again.')
        operator = None
    if operator == "=":               # debug
        print (result)
        break    
    print ( "end cycle" ,operand,operator, wait_for_number, result)        