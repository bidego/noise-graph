from html.entities import name2codepoint
from termios import NL1
import time
import random


Width = 240
C = 18
Intervalo = 0.01

def calcularNro(offset):
  return random.random() * C - C/2 + offset # (-2, 2)

nro = int(calcularNro(0))
nro2 = int(calcularNro(0))
nro3 = int(calcularNro(0))
nro4 = int(calcularNro(0))

def imprimirPunto(punto, color):
    print(int(punto+Width/2+C/2)*" ",color + "▀" )#, (Width - punto)*2*" ", "▀")
    time.sleep(Intervalo)

count = 1

while(count < 100*100*999):
    print('\33[40m')
    count = count + 1
    nro = int(calcularNro(nro))
    nro2 = int(calcularNro(nro2))
    nro3 = int(calcularNro(nro3))
    nro4 = int(calcularNro(nro4))
    imprimirPunto(nro, '\33[31m')
    imprimirPunto(nro2, '\33[32m')
    imprimirPunto(nro3, '\33[35m')
    imprimirPunto(nro4, '\33[90m')


