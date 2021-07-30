
'''
Created on 29 july 2021

@author: Antonio Martínez Fernández
'''

array = []
visitados = []


def lectura():
    archivo = open("input7.txt")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        array.append(linea)


def infiniteLoop_search():

    global visitados
    i = 0
    accumulator = 0

    while(i not in visitados):

        actual = array[i]
        visitados.append(i)

        actual = actual.split()  # separamos en operacion y numero
        instruccion = actual[0]
        numero = actual[1]

        if(instruccion == "acc"):
            accumulator += int(numero)
            i += 1

        elif(instruccion == "nop"):
            i += 1

        else:
            i += int(numero)

    visitados = []
    return accumulator


def infiniteLoop_searchAndReplace():

    global array
    acc = 0
    i = 0

    '''
         Lo que buscamos es un tronco principal que se ejecuta sin cambiar ninguna instrucción y en cada lugar
         donde se pueda elegir ( jmp || nop ) se siguen 2 ramas , la del principal que no cambia nada y la auxiliar que toma la inversa

         En las ramas donde se toma el camino inverso se finaliza la ejecucción cuando se encuentra un repetido ( gracias a las copias de arrays solucionamos el 
         problema al llamar recursivamente del paso por referencia en python , lo que nos machaca os datos ) o cuando la linea actual es la última o más que la última,
         es decir que finaliza correctamente

         La solución o soluciones se escriben por pantalla siendo "ACC=" las del tronco principal( sin modificar ) o "ACC 2=" las de las ramas
        
    '''

    while i not in visitados:

        if(i >= len(array)):
            print("accumulator  =", acc)
            break

        else:
            actual = array[i]

            visitados.append(i)

            actual = actual.split()
            instruccion = actual[0]
            numero = actual[1]

            if(instruccion == "jmp"):
                altern_case(visitados[:], i+1, acc)
                i += int(numero)
            elif(instruccion == "nop"):
                altern_case(visitados[:], i+int(numero), acc)
                i += 1
            else:
                acc += int(numero)
                i += 1


def altern_case(arr, i, ac):

    global array
    while i not in arr:

        if(i >= len(array)):
            print("accumulator 2= ", ac)
            break

        else:

            actual = array[i]

            arr.append(i)

            actual = actual.split()
            instruccion = actual[0]
            numero = actual[1]

            if(instruccion == "jmp"):

                i += int(numero)
            elif(instruccion == "nop"):

                i += 1
            else:
                ac += int(numero)
                i += 1


if __name__ == '__main__':

    lectura()

    print("part 1 =", infiniteLoop_search())

    print("\nparte 2 ")
    infiniteLoop_searchAndReplace()
