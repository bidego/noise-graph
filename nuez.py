from html.entities import name2codepoint
from termios import NL1
import time
import random
from math import remainder

o = "▀"
l = "|"

def obj(n):
    if n % 2 > 0:
        return o;
    else:
        return  l;

# Ruido func
    # recibe n1 
    # generaba n2 
    # generaba n1bis numeroDelMedio(n1,n2)
    #### imprime n1 este no ve
    # imprime n1bis
    # imprime n2 
    # genera n1 
    # generar n2bis numeroDelMedio(n2,n1) 
    # imprimir n2bis
    # imprimir n1
    
# bucle Ruido(random)

count = 0
indiceRandom = 20
n1 = random.random()
n1 = int(n1*indiceRandom)
intervalo = 0.04
diff = 0

def imprimirPunto(punto):
    print(punto*" ","▀", (indiceRandom - punto)*2*" ", "▀")
    time.sleep(intervalo)

def diferencia(n1, n2):
    mayor = n1 if n1 > n2 else n2
    menor = n1 if n1 < n2 else n2
    d = mayor - menor
    return d

def ruido():
    global n1
    global indiceRandom
    global diff

    # generaba n2
    seed = random.random() * indiceRandom
    n2 = int(seed)
    # generaba n1bis numeroDelMedio(n1,n2)
    diff = diferencia(n1, n2)
        
    mayor = n1 if n1 > n2 else n2
    n1bis = int(mayor - diff / 2)
    # imprime n1bis
    # print(n1)
    imprimirPunto(n1bis)

    # imprime n2 

    imprimirPunto(n2)
    
    # genera n1
    n1 = int(random.random() * indiceRandom)
    # generar n2bis numeroDelMedio(n2,n1) 
    
    mayor = n1 if n1 > n2 else n2
    
    diff = diferencia(n1, n2)
    n1bis =  int(mayor - diff / 2)
    
    imprimirPunto(n1bis)

    imprimirPunto(n1)

    #indiceRandom -= 1

    # imprimir n1bis
    # imprimir n1
    #print(n1bis)
    #print(n1)

#generate noise
count = 1

while(count < 100*100*999):
    ruido()
    count = count + 1
    
