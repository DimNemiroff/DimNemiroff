
login = None
pass1 = None
pass2 = None

if __name__ == '__main__':

    while True:
        login = str(input ("Для реєстрації введіть бажаний логін: "))
        if login == "0":
            break
        elif len(login)<6: 
            print("Введений логін занадто короткий, введіть не менш 6 символів або натисніть '0' для виходу")
        else: 
            break
        
    while login != "0" and pass2 != "0" :
        pass1 = str(input ("Введіть бажаний пароль: "))
        if pass1 =="0": break
        elif len(pass1)<8:    
            print("Введений пароль занадто короткий, введіть не менш 8 символів або натисніть '0' для виходу") #Превіряємо належну довжину  
            continue
        pass2 = str(input ("Підтвердить пароль, або натисніть 0 для виходу: "))
        if pass1 != pass2:
            print("Введені паролі не співпадають")  #Перевірка на ідентичність
            continue
        else: break
    if pass1 == pass2 and login != "0" and pass2 != '0':    
        print(f"Вітаю, {login} Вас зареєстровано в системі! Не забудьте змінити пароль через 30 днів.")
    else: print("Нажаль, реєстрація не вдалася.Спробуйте іншим разом.")