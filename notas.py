#operadores racionales

resultado = 10 < 20

print(resultado)

#para python si se desea imprimir de manera concatenada como java o c++ 
#en python se hace usando "," en java usando + y en c++ usando <<

#forma 2

nombre ="Esteban"
edad = 18
print("Hola {} tienes {} años ".format(nombre,edad))

#forma 2 

print(f"Hola {nombre} tienes {edad} años ")

#lector o scanner en python
#        tipo de dato(input("txt que aparecera en consola"))
#numero = int(input("Digite un numero-> "))

numero = int(input("Digite un numero -> "))

#Si es string

txt = input("Digite una palabra -> ")

print(f"El numero es {numero}")
print(f"La palabra es {txt}")


#conversiones

n = int("23")

x = float("123.2")

y = str(10)#el 10 se convierte a una cadena

b = bin(2126)

hexa = hex(10) 
hexa = int("0xa", 16)
#hexa = int("0xa", base)

binaro = int("0b1010", 2)
#binaro = int("0b1010", base)

redondear = round(42.99999)

tamaño = len("Esteban")

#op logicos
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#https://www.w3schools.com/python/python_conditions.asp

#intercambio

a , b = b , a

#es lo mismo que

temp = a 

a = b 
b = temp

#condicionales 

if a > b:
    print(True)
elif a < b:
    print(False) 
else:
    print("Ninguna condicion se cumplio")

'''
Estructura de las condiciones

if condicion: 
    que se debe hacer
elif condicion:
    que de debe hacer
else: 
    que se debe hacer

    para las condiciones si se usa if, elif(else if) o else despues de la condicion siempre va :
    sin los : no funciona y tener en cuenta la tabulacion

    los if se pueden anidar o los elif pero al final siempre tiene que haber un else 
'''

#Arreglos -> https://www.w3schools.com/python/python_arrays.asp

'''
Los arreglos en python utilizan la forma [] y como este lenguaje es
los tipos de datos son identificados auto entonces se hace como el sig ejm
'''

Array = [1,2,3,4,5]
Array2 = ["a","b","c","d"]

print(Array[0:4])#imprime los elementos de la lista desde la pos 0 hasta la pos 4-1
print(Array[0:])#imprime los elementos de la lista desde la pos 0 hasta el ultimo
print(Array,Array2)

#Funciones utiles

Array.append(6) #Agrega un elemento a la ultima posicion de la lista
print(Array)

Array.insert(0,777)#inserta en una posicion deseada un elemento 
#Array.insert(Posicion, valor)
print(Array)

Array.extend([1,2,3,4])#agregar mas de un elemento a la lista (al final)
print(Array)

print(Array + [1,2,3,3]) #otra forma

#Encontrar un elemento en la lista

test = 6 in Array # valordeseado in(en que parte) Arreglo o donde se desee buscar
print(test)
test2 = Array.index(5) #retorna la ubicacion-1 donde se encuentre el elemento

#Elementos repetidos 

test3 = Array.count(3)
print(f"Elementos repetidos {test3}")

#Eliminar elementos
print(Array)
test4 = Array.pop() #Array.pop() elimina el ultimo Array.pop(pos determinada)
print(Array)

#Eliminar elemento especifico
print(Array)
test4 = Array.remove(777) 
print(Array)

#invertir Arreglo
print(Array)
test5 = Array.reverse()
print(Array)

#Duplicar lista
#invertir Arreglo
test6 = [1,2,3,4]*2
print(test6)

#Ordenar lista
print(Array)
test7 = Array.sort()
print(Array)
test8 = Array.sort(reverse=True)#Ordenar de + -> - 
print(Array)

#Tupla -> valor fijo no se le puede agregar mas valores, no se puede añadir o quitar

tupla = ()
tupla =(1,3,43,343,23.12,234,"Hola",[1,2,3])

#Entoces que se puede hacer 1) Buscar 2) buscar elemento especifico 

test9 = tupla.count(1)

# tuplas a lista

lista = list(tupla)
Tupla2 = tuple(Array2)

#Conjunto -> https://www.youtube.com/watch?v=rmRrvol4XcM&list=RDCMUC7QoKU6bj1QbXQuNIjan82Q&index=5
# https://www.youtube.com/watch?v=UKD3CMINxik&list=RDCMUC7QoKU6bj1QbXQuNIjan82Q&index=24


#Diccionarios -> https://www.youtube.com/watch?v=vAy4IM7NLIQ&list=RDCMUC7QoKU6bj1QbXQuNIjan82Q&index=2


#Ciclos 

Array3 = [1,2,3,4,5,6]
tota =0
for x in Array3:
    print(Array3[x-1])
    tota+=Array3[x-1]
    print("total",tota)
else:
    print("No break")

cont=0
total1=0

while cont<len(Array3):
    total1+=Array3[cont]
    cont+=1


print(tota)
print(total1)


# Python program to demonstrate 
# range() function 
	

for i in range(5): 
	print(i, end =" ") # ciclo de rango 0-4
print() 

for i in range(2, 9): #Ciclo con rango del 2 - 9 que es rango 2 - 8
	print(i, end =" ") 
print() 

# loop with range 15 - 25 incremented by 3 
for i in range(15, 25, 3): 
	print(i, end =" ") 

#Ciclos controlados

s = 'geeksforgeeks'
  
for letter in s:  
    if letter == 'e' or letter == 's':  
        break
    print(letter, end = " ") 
print() 
  
for letter in s:  
    if letter == 'e' or letter == 's':  
        continue
    print(letter, end = " ") 
print()     
  
for letter in s:  
    if letter == 'e' or letter == 's':  
        pass
    print(letter, end = " ") 