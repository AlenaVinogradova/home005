# 0.
# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# Это задача с семинара, у меня более простое решение:
# Числа идут по порядку кроме одного. Значит можем создать список по порядку example,
# используя первый [0] и последний [len()] элемент, и сравнить их

with open('nums.txt','r') as q:
    ran = [int(i) for i in q.readline().split()]
print(ran)
# q = '45 46 47 49 50'
# ran = [int(i) for i in q.split()]
# print(ran)

example = [i for i in range(ran[0], ran[len(ran)-1])]

for i in example:
    if not i in ran:
        print(f'не хватает {i}')


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

Q = 2021      #Количество конфет на столе
m = 28        #Максимальный ход
opponent = False        #True - против человека, False - против компьютера
from random import randint
flag = True
count = 0
while Q > 0:
    if flag == True:
        a = int(input('Первый игрок. Сколько берете конфет? - '))
        flag = False
    else:
        if opponent:
            a = int(input('Второй игрок. Ваш ход: '))
        else:
            if Q > 6:
                # a = randint(1,6)      #бот
                a = Q%(m+1)             #бот с интеллектом
            else:
                a = Q
            print(f'Компьютер взял {a} конфет')
        flag = True
    Q -= a
    print(f'    Осталось {Q} конфет')
    count += 1
if count % 2:
    print('Победа первого игрока!')
else:
    if opponent:
        print('Победа второго игрока!')
    else:
        print('Победа компьютера')


# 3. Создайте программу для игры в ""Крестики-нолики"".

def out(list):
    print(list[0], list[1], list[2])
    print(list[3], list[4], list[5])
    print(list[6], list[7], list[8])

pole = [i for i in range(9)]
out(pole)
flag = True
count = 0
while not(pole[0]==pole[1]==pole[2]
        or pole[3]==pole[4]==pole[5]
        or pole[6]==pole[7]==pole[8]
        or pole[0]==pole[3]==pole[6]
        or pole[1]==pole[4]==pole[7]
        or pole[2]==pole[5]==pole[8]
        or pole[0]==pole[4]==pole[8]
        or pole[2]==pole[4]==pole[6]
        or count >= 9) :
    if flag == True:
        a = int(input('Поставьте крестик: '))
        pole[a] = 'x'
        flag = False
    else:
        a = int(input('Поставьте нолик: '))
        pole[a] = 'o'
        flag = True
    out(pole)
    count += 1
if count < 9:
    print(f'finish!!! winner is "{pole[a]}"')
else:
    print('ну вот, ничья')


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Алгоритм сжатия, заменяющий идущие подряд одинаковые символы парой (повторяющийся символ, количество повторений).
# Например, строчку aaababbcbbb он переводит в (a, 3) (b, 1) (a, 1) (b, 2) (c, 1) (b, 3).

message = 'aaababbcbbb'
print(message)
message += ' '      #можно использовать вместо 117 строчки. Какой вариант лучше?
encoding = []
count = 1
for i in range(1, len(message)):
    if message[i] == message[i-1]:
        count+=1
    else:
        encoding.append((message[i-1],count))
        count = 1
# encoding.append((message[len(message)-1], count))     #можно использовать вместо 108 строчки. Какой вариант лучше?

print(encoding)

str = ''
for i in encoding:
    str += i[0] * i[1]
print(str)
