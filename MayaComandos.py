import maya.cmds as cmds

#Create
#Crear con propiedades
cmds.polyCube(name = "myCube", width = 10)

#Edit
#editar flag
cmds.polyCube("myCube", edit = True, width = 5 )

#Query
#Consultar flag
cmds.polyCube("myCube", query = True, width = True)