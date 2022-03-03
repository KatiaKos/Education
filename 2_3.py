#Denisova Ekaterina katia_kos@mail.ru
#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.
n_month = input('Введите месяц в числовом формате: ')
a, b, c, d = 'winter', 'spring', 'summer', 'autumn'
my_dict = {
    "1" : a,
    "2" : a,
    "3" : b,
    "4" : b,
    "5" : b,
    "6" : c,
    "7" : c,
    "8" : c,
    "9" : d,
    "10" : d,
    "11" : d,
    "12" : a
}
print (my_dict.get(n_month))





