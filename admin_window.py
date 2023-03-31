import pyodbc
import random
import os

cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-DNTIAC2\CAT;Database=Carry;Trusted_Connection=yes;')
cursor = cnxn.cursor() 
def admin():
    choice = int(input("1 - Закупка продуктов\n2 - Посмотреть историю покупок пользователей\n3 - Посмотреть баланс\n4 - Изменить цены продуктов\n5 - Посмотреть карты пользователей "))
    if(choice == 1):
         cursor.execute("select [ID_Product], [Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type]")
         for i in cursor:
             print(i)
         buy = int(input("Выберете продукт для закупки:\n"))
         count_admin = int(input("Введите количество:\n"))
         cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] + {count_admin} WHERE [ID_Product] = {buy}")

         cursor.execute(f"select [Price] from [dbo].[Product] WHERE [ID_Product] = {buy}")
         test = cursor.fetchall()
         for i in test[0]:
              price_product = i
         print(f"Закупка успешна! С баланса списано {price_product*count_admin*0.5}")
                            
         cursor.execute(f"UPDATE [dbo].[User] SET [Balance] = [Balance] - {price_product*count_admin*0.5} WHERE [Email] = 'admin@gmail.ru'") 
    elif(choice ==  2):
         mail_user = input("Введите email пользователя:\n")
         cursor.execute(f"select [ID_User] from [dbo].[User] WHERE [Email] = '{mail_user}'")
         test = cursor.fetchall()
         for i in test[0]:
            id_user = i
         cursor.execute(f"select [Number_Cheque], [Date], [Foreign_Object], [Amount] from [Cheque] WHERE [User_ID] = '{id_user}'")
         for i in cursor:
            print(i)
    elif(choice == 3):
        print("Ваш баланс: \n")
        cursor.execute(f"select [Balance] from [dbo].[User] WHERE [Email] = 'admin@gmail.ru'")
        for i in cursor:
            print(i)                
        print("рубля")
    elif(choice == 4):
         cursor.execute("select [ID_Product], [Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type]")
         for i in cursor:
             print(i)
         buy = int(input("Выберете продукт для изменения цены:\n"))
         price_change = int(input("Введите новую цену:\n"))
         cursor.execute(f"UPDATE [dbo].[Product] SET [Price] = {price_change} WHERE [ID_Product] = {buy}")
         print(f"Цена изменена на {price_change} рублей")

    elif(choice == 5):
        mail_user = input("Введите email пользователя:\n")
        cursor.execute(f"select [ID_User] from [dbo].[User] WHERE [Email] = '{mail_user}'")
        test = cursor.fetchall()
        for i in test[0]:
            id_user = i
        print("Карта лояльности пользователя: \n")
        cursor.execute(f"select [Name_Card],[Percent] from [User] inner join [dbo].[Card] on [Card_ID] = [ID_Card] WHERE [Email] = '{mail_user}'")
        for i in cursor: 
            print(i)    
    cnxn.commit()
    cnxn.close()  
              
               