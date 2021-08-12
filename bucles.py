'''
borrar en terminal cls
'''

'''

Existen dos tipos de ciclos

for -> ejecuta una fraccion de codigo durante una cantidad definida

while -> ejecuta una fraccion de codigo durante una cantidad indefinida

'''

'''
for x in range(0, 3):
for x in range(3):
'''


for ñ in range(13):
    #print("2 x",ñ,"=", 2*ñ)
    x = ñ

lista = ["Maria_Arteaga", "Maria_Alvarez","Estefania","Susana","Esteban","Mateo","Montes", "Juan", "Simon", "Carlos", "David"]

for elemento in lista:
    #print(elemento)
    y = elemento 

for elemento2 in range(len(lista)):
    #print(lista[elemento2])
    z = elemento2 

tamano = range(len(lista))

for elemento3 in tamano:
    #print(lista[elemento3])
    c = elemento3

for numero in range(1, 10):
    if(numero % 2 != 0):
        #print(numero)
        s = numero

i = 0
while i < 10:
    #print(i)
    #i = i + 1
    i += 1 

cond = True
numero1 = 1
while cond:
    if(numero1 % 5 == 0):
        cond = False
    else:
        #print(numero1)
        numero1 += 1

numero2 = 1
while numero2 % 5 != 0:
    print(numero2)
    numero2 += 1

for i in range(10):
    if i % 2 == 0:
        print(i,"Par")
    elif i % 5 == 0:
        print(i,"Multiplo 5")
        break

for x in range(11):
    for y in range(11):
        print(x,"x",y,"=",x*y)

'''

import csv
 
with open('example.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)

'''
