import os
os.system('cls')
import time

numero = int(input('Informe o número: '))

for i in range(numero, 0, -1):
    print(i)
    time.sleep(1)

print('FIM.')