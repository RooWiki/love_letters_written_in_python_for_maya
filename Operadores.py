# OPERADORES BOOLEANOS (operadores logicos, puertas logicas)

# AND : devuelve True cuando x AND y sean verdaderos
# OR : devuelve True cuando x o y sean verdaderos
# NOT : niega un valor booleano

# OPERADORES DE COMPARACION
# > : devuelve True cuando x sea mayor a y
# < : devuelve True cuando x sea menor a y
# >= : devuelve True cuando x sea mayo o igual a y
# <= : devuelve True cuando x sea menor o igual a y
# == : devuelve True cuando x sea igual a y
# != : devuelve True cuando x sea diferente de y

# OPEROADORES CON ITERABLES(LISTAS,TUPLAS,STRINGS)

# in                            ejemplo:    Busca elemento
5 in [1,2,3]

# not in                        ejemplo:    No busca elemento
5 not in [1,2,3]
"j" not in "Phyton"

# + : concatenacion             ejemplo:    suma elementos
[1,2,3]+[4+5+6]
"hola " + "como estas"

lista = [1,2,3]
lista + [4,5,6]

print (id (lista))
print (id (lista + [4,5,6]))

# * :                           ejemplo:    multiplica elementos
[1,2,3] + 4
"phyton " * 3

# index : indice negativos      ejemplo:    Ultimo elemento de la lista
lista[-1]

# slicing                       ejemplo:    Selecion de elementos de la lista
lista = [1,2,3,4,5,6,7]
lista[0:3]
lista[:3]
lista[2:]
lista[::2]

# len                           ejemplo:    nuemro de elementos
len(lista)
len("python")

# min                           ejemplo:    Menor elementos
min(lista)
min("python")

# max                           ejemplo:    Mayor elementos
max(lista)
max("python")

# count                         ejemplo:    veces que se repite el elemento de la lista
lista.count(8)

# append                        ejemplo:    Agregar elemento a la lista
lista.append(4)
lista .append("jaja")
print(lista)


# remove                        ejemplo:    Quitar elemento a la lista
lista.remove(4)
print(lista)

# DANDO FORMATO A STRINGS
contendido = "juguetes"
cantidad = 10

print ("En la caja hay " + contendido + str(cantidad))

# %s, %f, %i                    ejemplo:    Cambio de formato
print ("En la caja hay %s %s" %(contendido, cantidad))
print ("En la caja hay %s %f" %(contendido, cantidad))
print ("En la caja hay %s %i" %(contendido, cantidad))

# \n                            ejemplo:    Salto de linea
print ("En la caja \nhay %s %s" %(contendido, cantidad))