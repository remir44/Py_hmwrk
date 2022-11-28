# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
day = int(input("Введите номер дня недели: "))
if day == 6 or day == 7:
    print("Выходной :)")
else:
    print("Не выходной :(")

# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
for x in range(2):
    for y in range(2):
        for z in range(2):
            left = not (x or y or z)
            right = not x and not y and not z
            result = left == right
            print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {result}")

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка.
x = int(input('Введите число x≠0: '))
y = int(input('Введите число y≠0: '))
if x == 0 or y == 0:
    print('Одна из точек равна нулю >:(')
elif x > 0 and y > 0:
    print(f'При координатах ({x}, {y}) точка находится в плоскости 1 ')
elif x < 0 and y > 0:
    print(f'При координатах ({x}, {y}) точка находится в плоскости 2 ')
elif x < 0 and y < 0:
    print(f'При координатах ({x}, {y}) точка находится в плоскости 3 ')
elif x > 0 and y < 0:
    print(f'При координатах ({x}, {y}) точка находится в плоскости 4 ')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('x > 0, y > 0')
elif quarter == 2:
    print('x < 0, y > 0')
elif quarter == 3:
    print('x < 0, y < 0')
elif quarter == 4:
    print('x > 0, y < 0')
else:
    print('На координатной плоскости только 4 четверти')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
ax = float(input('Введите координаты точки a по оси x:'))
ay = float(input('Введите координаты точки a по оси y:'))
bx = float(input('Введите координаты точки b по оси x:'))
by = float(input('Введите координаты точки b по оси y:'))
distance = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
print(f'Растояние между точкой A до точки B = {"%.2f" % distance}')

