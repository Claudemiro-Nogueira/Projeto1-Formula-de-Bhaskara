import math
a1, b1, c1 = map(float, input().split(' '))
a = a1
b = b1
c = c1

delta = (b*b) - 4*a*c
print(delta)
if delta < 0:
    print("Impossivel calcular")
elif(a == 0):
    print("Impossivel calcular")
else:
    x1 = (-b + math.pow(delta, 0.5)) / (2*a)
    x2 = (-b - math.pow(delta, 0.5)) / (2*a)
    #x1 = (-b + delta**1/2) / 2*a
    #x2 = (-b + delta**1/2) / 2*a
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')


