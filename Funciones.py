'''
en python a diferencia de los demas lenguajes

Las funciones ya no son public static etc...

Lo basico de las funciones en python son 

1: como se crean
    Para crear una funcion se crea con def, hay dos formas de crearlas

    publicas def funcion():

    privadas def __funcion();
'''
def student(firstname, lastname):   
     print(firstname, lastname) 

student(firstname ='Geeks', lastname ='Practice')      

'''
Algo muy importante de las funciones en python

1: el constructor

si hablamos de POO el contructor es muy ultil puesto que esto al crear instancias facilita las cosas

para crear el constructor se crea una nueva funcion:

def __init__(self,atrib,atrib2):
    self.atrib = atrib
    self.atrib2 = atrib


2: self

self es la instancia de la clase, usando self podemos acceder a los atributos de las clases

'''

class car(): 
      
    # init method or constructor 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 
          
    def show(self): 
        print("Model is", self.model ) 
        print("color is", self.color ) 
          
# both objects have different self which  
# contain their attributes 
audi = car("audi a4", "blue") 
ferrari = car("ferrari 488", "green") 
  
audi.show()     # same output as car.show(audi) 
ferrari.show()  # same output as car.show(ferrari) 

'''
Clases

Para crear clases en python se utiliza el metodo class nombre():

cuando son clases, metodos, condiciones, ciclos, etc se le agrega al final :
'''

'''

En java cuando uno instanciaba otra clase de otro archivo.java uno llamaba el meotod desde 

Metodo1 = new Metodo(atribs)

en el caso de python se realiza de la siguiente forma

import Metodo as mt

y para buscar sus clases en java era

Metodo1.Pruebas()

en python es

mt.Pruebas()

si no se hace lo de mt toca como 

Metodo.Pruebas()
'''