#x = int(input('Здравствуйте хотите записать числа лично? 1 - да , 2 - нет'))
#y = [1,2,3,4,5,6,7,8,9]
def GetMatrix(n,m,value):
    matrix =[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
#if x == 1:
n = int(input('Задайте количество строк :'))
m = int(input('задайте количество столбцов :'))
value = input('Значение матрицы: ')
print('---' * m)
matrix = GetMatrix(n,m,value)
#elif x == 2:
#n = random.choice(y)
#m = random.choice(y)
#value = random.choice(y)
if n <= 0:
    print('Невозможно вывести нулевое значие')
elif m <= 0:
    print('невозможно вывести нулевые значения')
else:
    print('-----------')
# в комментариях попытка сделать программу отчасти рандомной, но попытка провальная
# отступы в комментариях убраны специально*
# нужна ли особая библиотека функций для random.choice или она уже вшита в программу ?
