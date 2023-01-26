#ejercicio cuadricula de cubos
rango = range(13)
rango1 = range(13)
print (rango)
x=0
y=0
for objeto in rango:
    
    for objeto2 in rango1:
        #el cuerpo del bucle
        cube = cmds.polyCube(w=0.9, h=0.9, d=0.9)
        cmds.move(b,0,a, cube[0])
        b = b+1
    a = a + 1
    b=0
a=0;