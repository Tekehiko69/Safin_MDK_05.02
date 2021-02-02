# 1 Задание
a = int(input('a = '))
b = int(input('b = '))
a, b = b, a
print('a =', a)
print('b =', b)
# 2 Задание
a = int(input())
sum = 0
while a > 0:
    last_digit = a % 10
    sum += last_digit
    a = a // 10
print(sum)
# 3 Задание
a, b, c = float(input()), float(input()), float(input())
d = (b**2) - 4*a*c
if d > 0:
    x1 = (-b - d ** 0.5) / (2*a)
    x2 = (-b + d ** 0.5) / (2*a)
    print(min(x1, x2), max(x1, x2))
elif d == 0:
    print(-b / (2*a))
else:
    print('Нет корней')