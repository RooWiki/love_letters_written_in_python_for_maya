# FUNTIONS

# Son bloques de codigo, que tiene un nombre, que acepta parametros, y regresa un resultado
# Estas funciones nos permiten programar funcinalidades, las cuales podemos utilizar y reutilizar
# en nuestros promgramas(scripts), adapatando su resultados de acuerdo a parametros(argumentos)
def saludar():
    print("Hola Mundo")

saludar()
#####################    
   
def sumar(a, b):
    return a + b
   
a = sumar (10,10)
print (a)


######Ejemplo de funcion
# Funcion de distancia entre obejtos


import maya.cmds as cmds
import math

def distancia(objeto1, objeto2):
    punto1 = cmds.xform(objeto1, query = True, translation=True, worldSpace=True)
    punto2 = cmds.xform(objeto2, query = True, translation=True, worldSpace=True)
   
    vector = [punto1[0] - punto2[0], punto1[1] - punto2[1], punto1[2] - punto2[2]]
    
    hipotenusa = math.sqrt(vector[0]**2 + vector[2]**2)
    distancia = math.sqrt(hipotenusa**2 + vector[1]**2)
    
    return distancia







print(distancia("pCube1","pCube2")) #recibe dos obejtos