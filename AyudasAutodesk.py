import maya.cmds as cmds
import sys

print(sys.version)
#MEL
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;

#Python
cmds.polySphere(r=1, sx=20, sy=20, ax=(0,1,0), cuv=2, ch=1)

#Comando help
cmds.help("polySphere")

##Generar esfera sin cambiar todos sus parametros
cmds.polySphere(radius = 10)

"""Tambien se pude aprender comandos en la pestaña
Script Editor / Help / Python Command Reference"""