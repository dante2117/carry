import pyodbc
import random
import os
import email_carry 
import coll_dishes 
import admin_window 
import time


cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-DNTIAC2\CAT;Database=Carry;Trusted_Connection=yes;')
cursor = cnxn.cursor() 
while(True):
   try:
     aut = int(input("Добро пожаловать в 🔥 Хот Карри 🔥 \n1 - Войти \n2 - Зарегистрироваться\n"))
   except BaseException:
     print("Введены некорректные значения! Исправьтесь!")
     time.sleep(3)
     os.system("cls")
     continue

   if (aut == 1):
        os.system('cls')
        recipient = input("Введите почту:\n")
                    
            
        if(recipient == "admin@gmail.ru"):
                admin_window.admin()
                break 
            
        else: 
                code_rand = random.randint(1000,9999)
                message = f"Ваш код подтверждения для регистрации {code_rand}. Спасибо, что выбрали нас!\n"
                print(email_carry.send_mail(message=message, recipient=recipient))
        
        while(True):
                try:
                    code_chek = int(input("Введите код из сообщения: \n"))
                except BaseException:
                    print("Введены некорректные значения! Исправьтесь!")
                    time.sleep(3)
                    os.system("cls")
                    continue
            
                print("Вы вошли как пользователь")
                if(code_chek == code_rand):
                    choice = int(input("1 - Собрать Карри \n2 - Посмотреть баланс \n3 - Посмотреть чеки \n4 - Карта лояльности\n"))
                    os.system("cls")
                    if(choice == 1):
                        coll_dishes.dishes(recipient)
                            
                    elif(choice == 2):
                        print("Ваш баланс: \n")
                        cursor.execute(f"select [Balance] from [dbo].[User] WHERE [Email] = '{recipient}'")
                        for i in cursor:
                            print(i)
                        print("рубля")

                    elif(choice == 3):
                        print("Ваши чеки: \n")
                        cursor.execute(f"select [ID_User] from [dbo].[User] WHERE [Email] = '{recipient}'")
                        test = cursor.fetchall()
                        for i in test[0]:
                            id_user = i
                        cursor.execute(f"select [Number_Cheque], [Date], [Foreign_Object], [Amount] from [Cheque] WHERE [User_ID] = '{id_user}'")
                        for i in cursor:
                            print(i)
                    elif(choice == 4):
                        print("Ваша карта лояльности: \n")
                        cursor.execute(f"select [Name_Card],[Percent] from [User] inner join [dbo].[Card] on [Card_ID] = [ID_Card] WHERE [Email] = '{recipient}'")
                        for i in cursor:
                            print(i)

                    cnxn.commit()
                    break
   
                else:
                    print("Код введён неверно! Попробуйте ещё")  

            

   elif(aut == 2):
        os.system('cls')
        recipient = input("Введите почту:\n")  
        code_rand = random.randint(1000,9999)
        message = f"Ваш код подтверждения для регистрации {code_rand}. Спасибо, что выбрали нас!\n"
        print(email_carry.send_mail(message=message, recipient=recipient))
        while(True):
            code_chek = int(input("Введите код из сообщения: \n"))
            if(code_chek == code_rand):
                cursor.execute(f"insert into [dbo].[User] ([Email],[Balance], [Card_ID]) values ('{recipient}','0', 4)")
                print("Вы успешно зарегистрированы!")
                time.sleep(3)
                os.system('cls')
                break
            else:
                print("Код введён неверно! Попробуйте ещё")  
        

        cnxn.commit()

   else:
       print("Такой операции не существует")
 

cnxn.close()