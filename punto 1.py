def main():
    #Tamaño maximo del vector
    tamaño= 13
    numero=input('ingrese el codigo:') #Ingreso de los valores del codigo de barras
    codigo=[int(x) for x in numero]
    cero(codigo)
    codigoEAN(codigo)
    impares(codigo)
    pares(codigo)

    #Codigo de control
    p = impares(codigo) + pares(codigo)
    print(p)
    print(codigoControl(p))
    
#definicion de EAN-8 o EAN-13
def codigoEAN(codigo):
    if(len(codigo)==8):
        print("El codigo es EAN-8")
    else:
        print("El codigo es EAN-13")
        #definicion del pais
        if(codigo[0]==0):
            print("El codigo del pais es de EEUU")
        elif(codigo[0]==3 and codigo[1]==8 and codigo[2]==0):
                print("El codigo del pais es de Bulgaria")
        elif(codigo[0]==5 and codigo[1]==0):
                print("El codigo del pais es de Inglaterra")
        elif(codigo[0]==5 and codigo[1]==3 and codigo[2]==9):
                print("El codigo del pais es de Irlanda")
        elif(codigo[0]==5 and codigo[1]==6 and codigo[2]==0):
                print("El codigo del pais es de Portugal")
        elif(codigo[0]==7 and codigo[1]==0):
                print("El codigo del pais es de Noruega")
        elif(codigo[0]==7 and codigo[1]==5 and codigo[2]==9):
                print("El codigo del pais es de Venezuela")
        elif(codigo[0]==8 and codigo[1]==5 and codigo[2]==0):
                print("El codigo del pais es de Cuba")
        elif(codigo[0]==8 and codigo[1]==9 and codigo[2]==0):
                print("El codigo del pais es de India")
        else:
            print("DESCONOCIDO")
#rellenar los 0                
def cero(codigo):
    x=len(codigo)
    while x < 8:
        codigo.append(0); 
        x=len(codigo)         
    print(codigo)
        
#multiplicar las casillas impares
def impares(codigo):
    mult=0
    for x in range(0,8):
        if (x %2) != 0:
            mult +=  codigo[x] * 3
    return mult

#multiplicar casillas pares        
def pares(codigo):
    suma=0
    for x in range(0,8):
        if (x %2) == 0:
            suma += codigo[x]
    return suma

#Validacion del codigo de control
def codigoControl(p):
    if(p %10 == 0):
        return "SI"
    else:
        return "NO"


main()
                    
    
    
    

    