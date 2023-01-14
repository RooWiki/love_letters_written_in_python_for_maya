# VARIABLES
# El nombre de la variable = valor 

contenido = "Juguetes"
print (contenido)
result = type(contenido)    
print (result)

#Para sumar tipos de datos deben ser de un mismo timpo
cantidad = 100
x = str(cantidad)
TipoDeX = type (x)
print (TipoDeX)

y = type(contenido)
print (y)

print  (x + contenido + "Hola mundo")
#Python: Tipado dinamico 


#Las variables SOLO son nombres que apuntan a objetos
#Estos objetos cumplen con tres parametros: IDENTITY, TYPE, VALUE
#Ejemplo:
a = "Pablo"
print (id (a))#IDENTITY ES: id (a), TYPE ES: STRING Y VALUE ES: Pablo

##PARA ELIMIAR UNA VARIABLE
del (a)


##APUNTADORES
Nombre_1 = "Roo Wiki"
Nombre_2 = "Roo Wiki"
print (id (Nombre1))
print (id (Nombre2))
#los dos apuntadores tienen el mismo ID
del(Nombre1) #Si se borra el apuntador Nombre1 el objeto sigue existiendo porque existe el apuntador Nombre2 
del(Nombre2)#Para borrar el objeto definitivamente se deben de eliminar todos los apuntadores


# Tipo de escritura de Python: PEP 8

