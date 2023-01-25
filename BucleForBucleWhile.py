
# Bucle for 
# Este programa genera una fila de cubos con el bucle for
b=0
for objeto in [1,2,3,4,5,6,7]:
     #el cuerpo del bucle
     cube = cmds.polyCube(w=0.9)
     cmds.move(b,0,0, cube[0])
     b = b+1



## 
# Este programa genera una fila de cubos con un rango de 0 a 100
rango = range(100)
print (rango)

b=0
for objeto in rango:
     #el cuerpo del bucle
     cube = cmds.polyCube(w=0.9)
     cmds.move(b,0,0, cube[0])
     b = b+1
     
## 
# Bucle while 
##

b = 0
while b<10:
    print (b)
    b=b+1