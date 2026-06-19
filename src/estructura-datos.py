print("Estructuras de datos en Python")
print("======================================\n")
#Listas
print("listas(list)")
# Indice       0      1     2        3           Izquierda-Derecha
# Indice      -4     -3    -2       -1
fullstack = ["Html","JS", "CSS", "Python" ]
#Agregar elemento a la Lista

fullstack.append("base de datos")

print(fullstack)
print("----------------------------------------")

print(  f"El tipo de datos es: {type(fullstack)}")
print("----------------------------------------")



#Acceder a un elemento de una lista
print( fullstack[0], fullstack[-2])

#Lista de Listas (Matriz)
Matriz_simulada= [

    [1,2,3],
    [8,7,5]

]
print(Matriz_simulada)

"""
#Tuplas

Las tuplas no pueden ser agregados datos de ningun tipo, en cambio las listas si se puede.

"""
titulo= "Tuplas(tuples) esto es un ejemplo dinamico"
print(titulo)
print( "-" * len(titulo) )

curso= ("bootcamp", "Fullstack", "python", "2026")
print(curso)
print( f"El tipo de dato es:{type(curso)}")

nombre= "diego"
#sets

titulo1= "Set(set) esto es un ejemplo dinamico"
print(titulo1)
print( "-" * len(titulo1) )

lenguajes= {"Python", "JavaScript", "PHP", "C++", "Elxir"}
print(lenguajes )
print( f"El tipo de dato es:{type(lenguajes)}")

#Valores unicos en el Set, ignora los duplicados
lenguajes1= {"Python", "JavaScript", "PHP", "C++", "Elxir", "Python", "Python", "Python"}
print(lenguajes1 )

#Transforma lista en set.
lista_set= [1, 1, 1, 2, 2, 3, 4, 5, 6, 7,7,7,7]
print(set(lista_set))
#diccionarios