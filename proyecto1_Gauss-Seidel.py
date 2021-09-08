import math
import os
def Imprimir():
    print("\t\t\t ____________________________________________")
    print("\t\t\t||\t\t\t\t\t\t||")
    print("\t\t\t||\t\t\tECUACIONES:\t\t||")
    print("\t\t\t||\t\t\t\t\t\t||")
    print("\t\t\t ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯\n")
    for i in range (Grado):
        n= 0
        print("\t\t\t\t", end = "") 
        for j in range (Grado):
            print(str(matriz[i][j]) + "X" + str(n + 1) + "    ", end = "")
            n = n +1
        print("|    " + str(ConstanteMatriz[i]))
   
    print("\n")

def Procedimiento():
    Diag = []
    ValAct = []
    ValAnt = []
    Eaproximado = []

    for i in range (Grado):
        Diag.append(matriz[i][i])
        ValAct.append(0)
        ValAnt.append(0)
        Eaproximado.append(100)
    ErrorIn = 100

    NumIt = 0
    while ErrorIn > errordefinido:
        for i in range (Grado):
            aux = 0
            for j in range (Grado):
                if (i != j):
                    aux -= ValAct[j]*matriz[i][j]
            ValAct[i] = (ConstanteMatriz[i] + aux)/Diag[i]

        if (NumIt > 0):
            for i in range (Grado):
                Eaproximado[i] = abs( (ValAct[i] - ValAnt[i])/ValAct[i] ) * 100

        ValAnt = ValAct[:]
        NumIt = NumIt + 1
        ErrorIn = max(Eaproximado)
    print ("\tIteraciones para la solución: " + str(NumIt))
    for i in range(Grado):
        print("\tX" + str(i + 1) + " = " + "{:.5f}".format(ValAct[i]) + "\t\tError: " + "{:.5f}".format(Eaproximado[i]) + " %")
    print ("\n")
    if(math.isnan(Eaproximado[1])):
        print("Ocurrió un error con el programa.")

matriz = []
ConstanteMatriz = []
Grado = 0
errordefinido = 0
validador = False

print("\n\n\t\t\t\t\tMÉTODO DE GAUSS SEIDEL.\n\n")
print("\t\tEste programa resuelve ecuaciones por el método de Gauss Seidel, en el cual")
print("\t\tse puede resolver hasta n ecuaciones y además poder ejecutarse mediante un")
print("\t\terror deseado.\n")
print("\tRegla: \n\tPara llevar a cabo la ejecución del programa, se debe tener en cuenta lo siguiente:")
print("\t\t1. Ingresar ecuaciones cuya diagonal sea mayormente dominante y no contenga ceros.\n\t\t2. A la hora de escribir la matriz, tener cuidado en no teclear alguna letra.")
try:
        while(not validador):
            try:    
                Validador = Grado = int(input("\n\tIngrese la dimensión de la matriz cuadrada: "))
                if(Grado < 2):
                    print("\n\tIngrese un número mayor o igual que 2")
                else:#   Grado de la matriz
                    break
            except:
                print("No es un número.")
        validador = False
        while(not validador):
            try:
                Validador = errordefinido = float(input("Ingrese el margen de error deseado: [.5 a 100]: "))
                if(errordefinido < .5 or errordefinido > 100):
                    print("Ingrese una cantidad válida.")
                else:
                    break
            except:
                print("Ingrese una cantidad numérica.")

        for i in range(Grado):    #   Coeficiente de las ecuaciones
            auxiliar = []
            for j in range(Grado):
                auxiliar.append(float(input(f"[{i}][{j}]: ")))
            matriz.append(auxiliar)

        for i in range(Grado):
            aux = 0
            for j in range(Grado):
                if(i == j):
                    aux = matriz[i][j]
                    if(aux == 0):
                        print("Hay un cero en la diagonal.")
                        validador = True
                        quit()

        for i in range (Grado):   #Término independiente de las ecuaciones
            ConstanteMatriz.append(float(input(f"Término Independiente {i}: ")))
except:
        if(validador):
            quit()
        else:
            print("Hubo un error.")
        
Imprimir()
Procedimiento()
os.system('pause')
