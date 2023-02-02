# parametros por defecto

x = "global x"

def  any():
    #x = "local x"
    print (x)
    
    def inner():
        #x = "inner x"
        print x
    inner()
    
any()

###


def suma(a=0 , b=0):
    print (a+b)
suma (3,8)

