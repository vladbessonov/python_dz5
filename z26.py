# Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def stepen(a,b):
    if b == 0:
        return 1
    if b < 0:
        return 1/stepen(a, -b)
    if b>0 and b<1:
        return pow(a, b)
    return a * stepen(a, b-1)

a = int(input('Введите число А= '))
b = float(input('Введите число В= '))

a_step_b=stepen(a, b)

print (f"число А в степени В равно {a_step_b}")









