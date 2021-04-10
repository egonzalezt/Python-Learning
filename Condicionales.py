#condicionales 

a = 2
b = 3

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
    que se debe hacer
else: 
    que se debe hacer

    para las condiciones si se usa if, elif(else if) o else despues de la condicion siempre va :
    sin los : no funciona y tener en cuenta la tabulacion

    los if se pueden anidar o los elif pero al final siempre tiene que haber un else 
'''
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile or not a_smile and not b_smile :
    return True
  else: return False

'''
booleanos

0 - 1

0 no hay energia -> False
1 hay energia -> True

'''
cond = False
if(not cond):
    print("Hola")
else:
    print("Negado")


numero = 12

if numero % 2 == 0:

    print("Es multiplo de 2")
    
    if numero % 4 == 0:
        print("Es multiplo de 4")

        if numero % 16 == 0:
            print("Es multiplo de 16")  
        elif numero % 8 == 0:
            print("Es multiplo de 8")     
        else:
            print("Efe")
else:
    print("No es multiplo de 2")


edad = 5
ti = 1000205682
fnacimiento="11/27/2001"
nombre="Juan David Montes Pulgarin"

if edad > 18:
    print("La persona: {} De edad: {} y fecha de nacimiento {} Es mayor de edad".format(nombre,edad,fnacimiento))
elif edad > 10 and edad < 18:
    print("La persona: {} De edad: {} y fecha de nacimiento {} Es menor de edad por puto".format(nombre,edad,fnacimiento))
else:
    print("La persona: {} De edad: {} y fecha de nacimiento {} es demaciado pequeño".format(nombre,edad,fnacimiento))


agua_con_leche = 12
leche_en_polvo = 11

if agua_con_leche > leche_en_polvo:
    print("su mama hombre")
elif agua_con_leche < leche_en_polvo:
    print("your dad is your mom")

agua_con_leche1 ="Sumamahombre"
leche_en_polvo1 ="Supapamujer"

if agua_con_leche1 is not leche_en_polvo1:
    print("No tenes papas pibe")
if agua_con_leche1 is leche_en_polvo1:
    print("lo que sea")

'''
usar is not es para negar montes no es hombre -> montes is not hombre

usar is es para afirmar -> montes es hombre -> montes is hombre
'''

montes = True
hombre = True

if montes is hombre:
    print("Pos si montes es un hombre")

elif montes is not hombre:
    print("Sos mujer")

'''

true -> verdad -> 1
false -> falso -> 0 

0 no hay energia
1 hay energia

if True is not True -> False:
    print(is not hombre)
    
'''