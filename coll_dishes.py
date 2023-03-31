import pyodbc
import random
import os
import datetime

import time

now = datetime.datetime.now() 
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-DNTIAC2\CAT;Database=Carry;Trusted_Connection=yes;')
cursor = cnxn.cursor() 

def dishes(recipient):
              
              cursor.execute(f"select [Balance] from [dbo].[User] WHERE [Email] = '{recipient}'")
              test = cursor.fetchall()
              for i in test[0]:
                    balance = i

              balance = balance + 1900 + 1900 * random.uniform(0.2,0.4)  
              cursor.execute(f"UPDATE [dbo].[User] SET [Balance] = [Balance] + {balance} WHERE [Email] = '{recipient}'") 
              
              while(1 == 1):
                amount = 0
                cursor.execute("select [ID_Product], [Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type] WHERE [Name_Product_Type] = 'Мясо' and [Quantity_Stock] > 0")
                for i in cursor:
                     print(i)

                meat = int(input("Выберете мясо: \n"))
                cursor.execute(f"select [Price] from [dbo].[Product]  WHERE [ID_Product] = {meat}")
                test = cursor.fetchall()
                for i in test[0]:
                     price = i
                amount = amount + price

                cursor.execute("select [ID_Product],[Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type] WHERE [Name_Product_Type] = 'Рис' and [Quantity_Stock] > 0")
                for i in cursor:
                     print(i)
                rice = int(input("Выберете рис: \n"))
                cursor.execute(f"select [Price] from [dbo].[Product]  WHERE [ID_Product] = {rice}")
                test = cursor.fetchall()
                for i in test[0]:
                     price = i
                amount = amount + price

                cursor.execute("select [ID_Product],[Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type] WHERE [Name_Product_Type] = 'Картофель' and [Quantity_Stock] > 0")
                for i in cursor:
                     print(i)
                potato = int(input("Выберете картофель: \n"))
                cursor.execute(f"select [Price] from [dbo].[Product]  WHERE [ID_Product] = {potato}")
                test = cursor.fetchall()
                for i in test[0]:
                     price = i
                amount = amount + price

                cursor.execute("select [ID_Product],[Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type] WHERE [Name_Product_Type] = 'Морковь' and [Quantity_Stock] > 0")
                for i in cursor:
                     print(i)
                carrot = int(input("Выберете морковь: \n"))
                
                cursor.execute(f"select [Price] from [dbo].[Product]  WHERE [ID_Product] = {carrot}")
                test = cursor.fetchall()
                for i in test[0]:
                     price = i
                amount = amount + price

                cursor.execute("select [ID_Product],[Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type] WHERE [Name_Product_Type] = 'Паста Карри' and [Quantity_Stock] > 0")
                for i in cursor:
                     print(i)
                carry = int(input("Выберете пасту: \n"))

                cursor.execute(f"select [Price] from [dbo].[Product]  WHERE [ID_Product] = {carry}")
                test = cursor.fetchall()
                for i in test[0]:
                     price = i
                amount = amount + price

                cursor.execute("select [ID_Product],[Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type] WHERE [Name_Product_Type] = 'Мёд' and [Quantity_Stock] > 0")
                for i in cursor:
                     print(i)
                honey = int(input("Выберете мёд: \n"))
                
                cursor.execute(f"select [Price] from [dbo].[Product]  WHERE [ID_Product] = {honey}")
                test = cursor.fetchall()
                for i in test[0]:
                     price = i
                amount = amount + price

                cursor.execute("select [ID_Product],[Name_Product], [Price] , [Name_Product_Type] from [dbo].[Product] inner join [dbo].[Product_Type] on [Product_Type_ID] = [ID_Product_Type] WHERE [Name_Product_Type] = 'Лук' and [Quantity_Stock] > 0")
                for i in cursor:
                     print(i)
                onion = int(input("Выберете лук: \n"))
                
                cursor.execute(f"select [Price] from [dbo].[Product]  WHERE [ID_Product] = {onion}")
                test = cursor.fetchall()
                for i in test[0]:
                     price = i
                amount = amount + price

                count = int(input("Введите количество таких блюд: \n"))
                number_rand = random.randint(100,999)
                cursor.execute(f"insert [dbo].[Dish] ([Number_Dish], [Quantity]) values ('{number_rand}','{count}')")
                amount = amount * count
                cursor.execute(f"select [ID_Dish] from [dbo].[Dish] WHERE [Number_Dish] = {number_rand}")
                test = cursor.fetchall()
                for i in test[0]:
                     id_dish = i 

                cursor.execute(f"select [ID_User] from [dbo].[User] WHERE [Email] = '{recipient}'")
                test = cursor.fetchall()
                for i in test[0]:
                     id_user = i
                
                cursor.execute(f"insert into [dbo].[Product_Dish] ([Product_ID], [Dish_ID]) values ('{meat}','{id_dish}')")
                cursor.execute(f"insert into [dbo].[Product_Dish] ([Product_ID], [Dish_ID]) values ('{rice}','{id_dish}')")
                cursor.execute(f"insert into [dbo].[Product_Dish] ([Product_ID], [Dish_ID]) values ('{potato}','{id_dish}')")
                cursor.execute(f"insert into [dbo].[Product_Dish] ([Product_ID], [Dish_ID]) values ('{carrot}','{id_dish}')")
                cursor.execute(f"insert into [dbo].[Product_Dish] ([Product_ID], [Dish_ID]) values ('{carry}','{id_dish}')")
                cursor.execute(f"insert into [dbo].[Product_Dish] ([Product_ID], [Dish_ID]) values ('{honey}','{id_dish}')")
                cursor.execute(f"insert into [dbo].[Product_Dish] ([Product_ID], [Dish_ID]) values ('{onion}','{id_dish}')")

                cursor.execute(f"select [ID_Product_Dish] from [dbo].[Product_Dish] WHERE [Dish_ID] = '{id_dish}'")
                test = cursor.fetchall()
                for i in test[0]:
                     id_product_dish = i

                cheque_rand = random.randint(1000,9999)
                current_time = now.strftime("%d-%m-%Y %H:%M")
                foreign = random.randint(0,1)
                foreign_found = random.randint(0,1)
                cursor.execute(f"insert into [dbo].[Cheque] ([Number_Cheque], [Date], [Amount], [User_ID], [Product_Dish_ID]) values ('{cheque_rand}','{current_time}','{amount}', '{id_user}', '{id_product_dish}')")

                cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] - 1 WHERE [ID_Product] = {meat}") 
                cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] - 1 WHERE [ID_Product] = {rice}")
                cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] - 1 WHERE [ID_Product] = {potato}")
                cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] - 1 WHERE [ID_Product] = {carrot}") 
                cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] - 1 WHERE [ID_Product] = {carry}")                     
                cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] - 1 WHERE [ID_Product] = {honey}")
                cursor.execute(f"UPDATE [dbo].[Product] SET [Quantity_Stock] = [Quantity_Stock] - 1 WHERE [ID_Product] = {onion}")
                os.system('cls')
                resume = int(input("1 - Сбор следующего блюда\n2 - Перейти к оплате\n"))
                if(resume == 1):
                     cnxn.commit()
                     print(f"Переход на сбор следующего блюда через.. ")
                     for i in range(3, 0, -1):
                           print(f"{i} с")
                           time.sleep(1)
                     os.system('cls')
                     continue
                if(resume == 2):
                     cursor.execute(f"select [Percent] from [User] inner join [dbo].[Card] on [Card_ID] = [ID_Card] WHERE [Email] ='{recipient}'")
                     test = cursor.fetchall()

                     for i in test[0]:
                              card_persent = i

                     if(card_persent == 5):
                                amount_final = amount*0,95
                                final_balance = balance - amount_final
                                final_balance_foreign = balance - amount*0,65
                     elif(card_persent == 10):
                                amount_final = amount*0,9
                                final_balance = balance - amount_final
                                final_balance_foreign = balance - amount*0,6
                     elif(card_persent == 20):
                                amount_final = amount*0,8
                                final_balance = balance - amount_final
                                final_balance_foreign = balance - amount*0,5
                     elif(card_persent == 0):
                                amount_final = amount
                                final_balance = balance - amount_final
                                final_balance_foreign = balance - amount*0,7

                     if(amount_final > 10000):
                              amount_final = amount_final*0,9

                     if(balance >= amount):
                      if(foreign == 0):

                           cursor.execute(f"UPDATE [dbo].[User] SET [Balance] = {final_balance} WHERE [Email] = '{recipient}'")
                           print(f"Ваше блюдо собрано! С баланса списано {amount_final} рублей.\nС чеком и текущим балансом можете ознакомиться в главном меню")  
                           
                           cursor.execute(f"UPDATE [dbo].[User] SET [Balance] = [Balance] +{amount_final} WHERE [Email] = 'admin@gmail.ru'")
                           if(amount_final >= 5000):     
                            cursor.execute(f"UPDATE [dbo].[User] SET [Card_ID] = 1 WHERE [Email] = '{recipient}'")
                            print("Вам предоставлена скидка 5%. Карту лояльности можете посмотреть в главном меню")
                           elif(amount_final >= 15000):
                                  cursor.execute(f"UPDATE [dbo].[User] SET [Card_ID] = 2 WHERE [Email] = '{recipient}'")
                                  print("Вам предоставлена скидка 10%. Карту лояльности можете посмотреть в главном меню")
                           elif(amount_final >= 25000):
                                  cursor.execute(f"UPDATE [dbo].[User] SET [Card_ID] = 3 WHERE [Email] = '{recipient}'")
                                  print("Вам предоставлена скидка 20%. Карту лояльности можете посмотреть в главном меню")
                           cnxn.commit()
                           cnxn.close()
                           break
                      elif(foreign == 1 and foreign_found == 1):
                           print(balance)
                           print(amount)
                           print(final_balance_foreign)
                           cursor.execute(f"UPDATE [dbo].[User] SET [Balance] = {final_balance_foreign} WHERE [Email] = '{recipient}'")
                           os.system('cls')
                           print(f"Ваше блюдо собрано! Но в него попал глаз кентавра 👁\nПриносим свои извинения и предоставляем скидку в 30%. С баланса списано {amount_final} рублей.\nС чеком и текущим балансом можете ознакомиться в главном меню")  
                           cursor.execute(f"UPDATE [dbo].[Cheque] SET [Foreign_Object] = 'Глаз кентавра' WHERE [Number_Cheque] = {cheque_rand}")
                           
                           cursor.execute(f"UPDATE [dbo].[User] SET [Balance] = [Balance] +{amount_final} WHERE [Email] = 'admin@gmail.ru'")

                           cnxn.commit()
                           cnxn.close()
                           break
                      
                     else:
                      amount = 0
                      print(f"На вашем балансе недостаточно средств для данной покупки!\nБаланс составляет {balance}\nВыберете другие ингредиенты")
                      print(f"Переход на пересбор блюда через.. ")
                      for i in range(3, 0, -1):
                           print(f"{i} с")
                           time.sleep(1)
                      os.system('cls')
                      continue
                      



                
                