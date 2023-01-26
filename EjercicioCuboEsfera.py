##### Ejercicio cubo esfera
rango = range(10)
rango1 = range(10)
RadioCubo = 1


RadioEsfera = RadioCubo/2
for x in rango:
    for y in rango1:
        if  x % 2 == 0 and y % 2 == 0:
            cube = cmds.polyCube(d = RadioCubo, h = RadioCubo, w = RadioCubo)
            cmds.move(x*RadioCubo,0,y*RadioCubo, cube[0])
        elif x % 2 == 1 and  y % 2 == 0:
            esfera = cmds.sphere(r = RadioEsfera)
            cmds.move(x*RadioCubo,0,y*RadioCubo, esfera[0])
        
        if  x % 2 == 1 and y % 2 == 1:
            cube = cmds.polyCube(d = RadioCubo, h = RadioCubo, w = RadioCubo)
            cmds.move(x*RadioCubo,0,y*RadioCubo, cube[0])
        elif x % 2 == 0 and  y % 2 == 1:
            esfera = cmds.sphere(r = RadioEsfera)
            cmds.move(x*RadioCubo,0,y*RadioCubo, esfera[0])