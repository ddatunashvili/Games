import random
cda=1 # პირველი კრუგი ცდად ითვლება
rnd=random.randint(0,100) # რენდომ ირჩევს რიცხვს
# ციკლი იწყება
while True:
    ricxvi=input("Chawere savaraudo ricxvi (0/100) ")
    # შეგყავს ვერსია
    try: # ამოწმებს რიცხვი ჩაწერე თუ სხვა სიმბოლო
        ricxvi=int(ricxvi)
    except:
        print("shecdoma, tavidan sheiyvane. ")
        continue # თუ შეცდომაა პროცესი,ციკლი იწყება თავიდან
    if rnd==ricxvi: # თუ რიცხვი დაემთხვა
        print(f'yochag shen gamoicani {cda} cdashi')
        # გთხოვს უპასუხო
        pasuxi=input("kidev ginda tamashi? (ki/ara)")
        if pasuxi=="ki":
            continue # კი მაშინ პროცესი იწყება თავიდან
        else :
            print("warmatebebs gisurveb")
            break # სხვა პასუხზე პროცესი წყდება
    elif rnd > ricxvi: # თუ ჩაფიქრებული მაღალი რიცხვია
        print("magalia")
        cda=cda+1 # ცდად ითვლება და პროცესი თავიდან იწყება
    elif rnd<ricxvi: # თუ ჩაფიქრებული დაბალი რიცხვია
        print('dabalia')
        cda +=1 # ცდად ითვლება და პროცესი თავიდან იწყება
