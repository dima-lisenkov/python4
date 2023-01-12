k = int(input('Введите степень уравнения:'))
import random


coef_list = []
for i in range(k+1):
    coef = random.randint(0,101)
    coef_list.append(coef)


x_list = [str(f'x**{i}') if i!=1 else str(f'x') for i in range(k,0,-1)]


result_string = ''
for i in range(k):
    if (coef_list[i] != 0):
        result_string += f'{coef_list[i]}*{x_list[i]}'
        if coef_list[i+1] > 0:
            result_string += ' + '
if (coef_list[i] != 0):            
    result_string += f'{coef_list[k]} = 0'
else:
    result_string += f' = 0'


with open('3zadacha.txt', 'w') as f:
    f.write(result_string)

print(result_string)

