import maya.cmds as cmds

cube = cmds.polyCube()# Crea un cubo de nombre cube con ['pCube1', 'polyCube1']
cube_width = cmds.polyCube(cube[1], query = True, width = True)# Extrae width de polyCube1

esfera = cmds.polySphere(r = cube_width/2)# Crea una esfera del tamaño del width

#cube = cmds.polyCube(cube[1],edit = True, width = 3)# incremetna el tamaño de width del cubo

# Transformar Objetos
# Move, Rotate, Scale
# Move
cmds.move(1,0,0, cube[0])#Traslada cube/pCube1/TraslateX a 1 en cordenadas absolutas 
cmds.move(1,0,0, cube[0], r = True)#Traslada cube/pCube1/TraslateX a 1 en cordenadas realtivas
cmds.move(1,2,0, esfera[0], ls = True)#Traslada esfera/pSphere1/TraslateX a 1 TraslateY a 2 en LocalSpace (Con respecto al cubo)

# Rotate
cmds.rotate(0,45,0, cube[0])# rotacion cordenadas absolutas
cmds.rotate(0,45,0, cube[0], r = True)# rotacion cordenadas relativas
cmds.rotate(0,45,0, cube[0], ls = True)# rotacion LocalSpace


# Scale
cmds.scale(0,2,0, cube[0])# Escalado cordenadas absolutas
cmds.scale(3,1,0, cube[0], r = True)# Escalado cordenadas relativas
cmds.scale(3,3,3, cube[0], ls = True)# Escalado LocalSpace


#Comando Xform
cube_t = cmds.xform(cube[0], query=True, t=True)# Captura las coordenadas
cmds.xform(esfera[0], t=cube_t)# Traslada la esfera a la posicion del cubo
print (cube_t)

