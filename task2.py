#2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

a = int(input("Введите время в секундах:"))
b_h = a // 3600
b_m = (a % 3600) // 60
b_s = ((a % 3600) % 60)

if b_h > 0:
    h = b_h
else:
    h = 0
if b_m > 0:
    m = b_m
else:
    m = 0
if b_s > 0:
    s = b_s
else:
    s = 0
print (f"{h:02d}:{m:02d}:{s:02d}")

