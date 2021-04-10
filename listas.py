def lista():
    #Una lista puede aumentar lo que se quiera y puede tener todo tipo de datos
    #una tupla no puede alterarse
    lista = ["Hola",1,1.2,[1,2,2,3,4],{1,2,3,4,"Hola"}]
    #print(lista)
    #print(lista[0])
    #print("Tamaño de la lista",len(lista))
    lista2 = list(range(12,21))
    lista3 = list(range(21))
    lista3.insert(1,12)
    lista3.remove(4)
    lista3.reverse()
    #print(lista3)
    lista3.sort()
    #print(lista3)

    lista4 = ["Maria_Arteaga", "Maria_Alvarez","Estefania","Susana","Esteban","Mateo","Montes", "Juan", "Simon", "Carlos", "David"]
    lista4.sort()
    #print(lista4)

    '''
    Pilas

    append -> insertar al inicio.
    pop -> elimina el primer elemenento

    Colas

    append -> insertar
    popleft -> elimina el primer elemento

   *PENDIENTE*

    lista4 = ["Maria_Arteaga","Estefania","Susana","Esteban","Mateo","Montes", "Juan", "Simon", "Carlos", "David"]
    lista4.append("Maria_Alvarez")
    print(lista4)    
    print(lista4.pop())
    print(lista4.popleft())
    '''

lista()