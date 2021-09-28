##Denisova Ekaterina katia_kos@mail.ru

#1.2. Пользователь вводит время в секундах. Пер
time = int(input("Сколько секунд?"))
h = time // 3600
m = (time - h*3600) // 60
s = time - (h * 3600 + m * 60 )

print(f"Время   {h}  чч : {m} мм : {s} сс")



#тут мой мозг вышел