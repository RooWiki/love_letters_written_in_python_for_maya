
#getAttr
#Maya utiliza este comando para settear cualquier tipo de nodo
cmds.getAttr("pCube1.translateX")#primero va le nombre del obejto y el atributo
tx = cmds.getAttr(cube[0]+".translateX")#Tambien se puede de esta forma
print (tx)

#setAttr 
#Comando para colocar atributos
cmds.setAttr("pSphere1.translateX", tx)# Translada la esfera en X al valor de tx
########################################################
#getAttr
get_translate = cmds.getAttr(cube[0]+".translate")#toma los atributo de XYZ
print (get_translate)

# La diferencia entre capturar datos con xform y getAttr 
#xform = Lista con los atributos: [-0.49507152588286063, 0.0, 0.0]
#getAttr = Lista con una dupla con los atributos: [(-0.49507152588286063, 0.0, 0.0)]



#Cambio de posicion con getAttr y setAttr

get_translate1 = cmds.getAttr(cube[0]+".translate")#Captura coordendas
cmds.setAttr(esfera[0]+".translate", get_translate1[0][0],
                                     get_translate1[0][1],
                                     get_translate1[0][2],)#Envia a las coordenadas a la esfera
print (get_translate1)

# Ejemplo Cambio de color #######################################################
color_attr = cmds.getAttr("material_test.color")
cmds.setAttr("lambert1.color",color_attr[0][0],
                              color_attr[0][1],
                              color_attr[0][2],)
print (color_attr)

#######################################################
#######################################################
#Conectar nodos
cmds.connectAttr(esfera[0] +".translateX", cube[0]+".rotateX") #El cubo rota cuando la esfera se desplaza
#Desonectar nodos
cmds.disconnectAttr(esfera[0] +".translateX", cube[0]+".rotateX") #Los nodos se desconectan