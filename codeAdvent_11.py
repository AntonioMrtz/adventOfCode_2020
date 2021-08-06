'''
Created on 04 August 2021

@author: Antonio Martínez Fernández
'''


#! Importante dejar el input con una línea vacía al final para que todas las lineas acaben en \n y tengan la misma longitud :)

array = []

pasillo = ["."]
libre = ["L"]
l = ["L", "."]
ocupado = ["#"]


def lectura():

    #archivo = open("prueba.txt")
    archivo = open("input10.txt")

    while True:
        linea = archivo.readline()

        if not linea:
            break

        array.append(linea)


def countEmptySeats():

    global array
    contador = 0

    for i in range(0, len(array), 1):  # de 0 a longitud-1

        linea = array[i]

        for j in range(0, len(linea)-1, 1):  # de 0 a (len(linea)-1)-1

            if linea[j] in ocupado:
                contador += 1

    return contador


def checkOcuppied(i, j, linea, copia):

    global array

    total = 0

    if i == 0 and j != 0 and j != len(linea)-1:     # medio superior

        if linea[j-1] in ocupado:
            total += 1
        if linea[j+1] in ocupado:
            total += 1
        if copia[1][j] in ocupado:
            total += 1
        if copia[1][j-1] in ocupado:
            total += 1
        if copia[1][j+1] in ocupado:
            total += 1

    elif i == len(array)-1 and j != 0 and j != len(linea)-2:  # medio inferior

        if linea[j-1] in ocupado:
            total += 1
        if linea[j+1] in ocupado:
            total += 1
        if copia[len(array)-2][j] in ocupado:
            total += 1
        if copia[len(array)-2][j-1] in ocupado:
            total += 1
        if copia[len(array)-2][j+1] in ocupado:
            total += 1

    elif i != 0 and i != len(array)-1 and j == 0:

        if linea[j+1] in ocupado:
            total += 1
        if copia[i-1][j+1] in ocupado:
            total += 1
        if copia[i-1][j] in ocupado:
            total += 1
        if copia[i+1][j+1] in ocupado:
            total += 1
        if copia[i+1][j] in ocupado:
            total += 1

    elif i != 0 and i != len(array)-1 and j == len(linea)-2:

        if linea[j-1] in ocupado:
            total += 1
        if copia[i-1][j-1] in ocupado:
            total += 1
        if copia[i-1][j] in ocupado:
            total += 1
        if copia[i+1][j-1] in ocupado:
            total += 1
        if copia[i+1][j] in ocupado:
            total += 1

    elif i != 0 and i != len(array)-1 and j != 0 and j != len(linea)-2:

        if linea[j-1] in ocupado:
            total += 1
        if linea[j+1] in ocupado:
            total += 1
        if copia[i-1][j-1] in ocupado:
            total += 1
        if copia[i-1][j+1] in ocupado:
            total += 1
        if copia[i-1][j] in ocupado:
            total += 1
        if copia[i+1][j] in ocupado:
            total += 1
        if copia[i+1][j-1] in ocupado:
            total += 1
        if copia[i+1][j+1] in ocupado:
            total += 1

    if total >= 4:
        tmp = list(array[i])
        tmp[j] = 'L'
        array[i] = "".join(tmp)


def checkFree(i, j, linea, copia):

    global array

    contador = 0

    # * SUPERIOR

    if i == 0 and j == 0:

        if(array[1][0] in l and linea[1] in l and array[1][1] in l):

            contador += 1

    elif i == 0 and j == len(linea)-2:

        if(array[1][j] in l and array[1][j-1] in l and linea[j-1] in l):

            contador += 1

    elif i == 0 and j != 0 and j != len(linea)-1:

        if(linea[j-1] in l and linea[j+1] in l and copia[1][j] in l and copia[1][j-1] in l and copia[1][j+1] in l):

            contador += 1

    # * INFERIOR

    elif i == len(array)-1 and j == 0:

        if(copia[len(array)-2][0] in l and linea[1] in l and copia[len(array)-2][1] in l):

            contador += 1

    elif i == len(array)-1 and j == len(linea)-2:

        if(copia[len(array)-2][j] in l and linea[j-1] in l and copia[len(array)-2][j-1] in l):

            contador += 1

    elif i == len(array)-1 and j != 0 and j != len(linea)-2:

        if(linea[j-1] in l and linea[j+1] in l and copia[len(array)-2][j] in l and copia[len(array)-2][j-1] in l and copia[len(array)-2][j+1] in l):

            contador += 1

    # * MEDIO

    elif i != 0 and i != len(array)-1 and j == 0:

        if(linea[j+1] in l and copia[i-1][j+1] in l and copia[i-1][j] in l and copia[i+1][j+1] in l and copia[i+1][j] in l):

            contador += 1

    elif i != 0 and i != len(array)-1 and j == len(linea)-2:

        if(linea[j-1] in l and copia[i-1][j-1] in l and copia[i-1][j] in l and copia[i+1][j-1] in l and copia[i+1][j] in l):

           contador += 1

    elif i != 0 and i != len(array)-1 and j != 0 and j != len(linea)-2:

        if(linea[j-1] in l and linea[j+1] in l and copia[i-1][j-1] in l and copia[i-1][j+1] in l and copia[i-1][j] in l and copia[i+1][j] in l and copia[i+1][j-1] in l and copia[i+1][j+1] in l):

            contador += 1

    if(contador == 1):

        tmp = list(array[i])
        tmp[j] = '#'
        array[i] = "".join(tmp)


def getOcuppiedSeats(copia):

    global array

    for i in range(0, len(array), 1):  # de 0 a longitud-1

        linea = array[i]

        for j in range(0, len(linea)-1, 1):  # de 0 a (len(linea)-1)-1

            if linea[j] == "L":

                checkFree(i, j, linea, copia)

            elif linea[j] == '#':
                checkOcuppied(i, j, linea, copia)


def main_Function():

    lectura()

    copia = array[:]
    getOcuppiedSeats(copia)
    while(array != copia):

        copia = array[:]  # la actualizacion se hace en el main
        getOcuppiedSeats(copia)

    return countEmptySeats()


# 0 arriba ,1 abajo , 2 izq , 3 derecha , 4 izq-arriba , 5 der-arriba , 6 izq-abajo , 7 der-abajo
# devuelve # , L o .
def recorrer(dir, i, j, linea, copia):

    if(dir == 0):

        while(i > 0):

            i -= 1
            if(copia[i][j] in libre or copia[i][j] in ocupado):
                return copia[i][j]

        return "."

    elif(dir == 1):

        while(i < len(copia)-1):

            i += 1
            if(copia[i][j] in libre or copia[i][j] in ocupado):
                return copia[i][j]

        return "."

    elif(dir == 2):

        while(j > 0):
            j -= 1
            if(linea[j] in libre or linea[j] in ocupado):
                return linea[j]

        return "."

    elif(dir == 3):

        while(j < len(linea)-2):
            j += 1
            if(linea[j] in libre or linea[j] in ocupado):
                return linea[j]

        return "."

    elif(dir == 4):

        while(j > 0 and i > 0):
            i -= 1
            j -= 1
            if(copia[i][j] in libre or copia[i][j] in ocupado):
                return copia[i][j]

        return "."

    elif(dir == 5):

        while(j < len(linea)-2 and i > 0):
            i -= 1
            j += 1

            if(copia[i][j] in libre or copia[i][j] in ocupado):
                return copia[i][j]

        return "."

    elif(dir == 6):

        while(i < len(copia)-1 and j > 0):

            i += 1
            j -= 1
            if(copia[i][j] in libre or copia[i][j] in ocupado):
                return copia[i][j]

        return "."

    elif(dir == 7):

        while(i < len(copia)-1 and j < len(linea)-2):

            i += 1
            j += 1
            if(copia[i][j] in libre or copia[i][j] in ocupado):
                return copia[i][j]

        return "."


def checkFree_v2(i, j, linea, copia):

    global array

    contador = 0

    # * SUPERIOR

    if i == 0 and j == 0:

        if(recorrer(1, i, j, linea, copia) in l and recorrer(3, i, j, linea, copia) in l and recorrer(7, i, j, linea, copia) in l):

            contador += 1

    elif i == 0 and j == len(linea)-2:

        if(recorrer(1, i, j, linea, copia) in l and recorrer(2, i, j, linea, copia) in l and recorrer(6, i, j, linea, copia) in l):

            contador += 1

    elif i == 0 and j != 0 and j != len(linea)-1:

        if(recorrer(1, i, j, linea, copia) in l and recorrer(2, i, j, linea, copia) in l and recorrer(3, i, j, linea, copia) in l and recorrer(6, i, j, linea, copia) in l and recorrer(7, i, j, linea, copia) in l):

            contador += 1

    # * INFERIOR

    elif i == len(array)-1 and j == 0:

        if(recorrer(0, i, j, linea, copia) in l and recorrer(3, i, j, linea, copia) in l and recorrer(5, i, j, linea, copia) in l):

            contador += 1

    elif i == len(array)-1 and j == len(linea)-2:

        if(recorrer(0, i, j, linea, copia) in l and recorrer(2, i, j, linea, copia) in l and recorrer(4, i, j, linea, copia) in l):

            contador += 1

    elif i == len(array)-1 and j != 0 and j != len(linea)-2:

        if(recorrer(0, i, j, linea, copia) in l and recorrer(2, i, j, linea, copia) in l and recorrer(3, i, j, linea, copia) in l and recorrer(4, i, j, linea, copia) in l and recorrer(5, i, j, linea, copia) in l):

            contador += 1

    # * MEDIO

    elif i != 0 and i != len(array)-1 and j == 0:

        if(recorrer(0, i, j, linea, copia) in l and recorrer(1, i, j, linea, copia) in l and recorrer(2, i, j, linea, copia) in l and recorrer(4, i, j, linea, copia) in l and recorrer(6, i, j, linea, copia) in l):

            contador += 1

    elif i != 0 and i != len(array)-1 and j == len(linea)-2:

        if(recorrer(0, i, j, linea, copia) in l and recorrer(1, i, j, linea, copia) in l and recorrer(2, i, j, linea, copia) in l and recorrer(4, i, j, linea, copia) in l and recorrer(6, i, j, linea, copia) in l):

           contador += 1

    elif i != 0 and i != len(array)-1 and j != 0 and j != len(linea)-2:

        if(recorrer(0, i, j, linea, copia) in l and recorrer(1, i, j, linea, copia) in l and recorrer(2, i, j, linea, copia) in l and recorrer(3, i, j, linea, copia) in l and recorrer(4, i, j, linea, copia) in l and recorrer(5, i, j, linea, copia) in l and recorrer(6, i, j, linea, copia) in l and recorrer(7, i, j, linea, copia) in l):

            contador += 1

    if(contador == 1):
        tmp = list(array[i])
        tmp[j] = '#'
        array[i] = "".join(tmp)


def checkOcuppied_v2(i, j, linea, copia):
    global array

    total = 0

    # * SUPERIOR

    if i == 0 and j == 0:

        if recorrer(1, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(3, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(7, i, j, linea, copia) in ocupado:
            total += 1

    elif i == 0 and j == len(linea)-2:

        if recorrer(1, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(2, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(6, i, j, linea, copia) in ocupado:
            total += 1

    elif i == 0 and j != 0 and j != len(linea)-1:

        if recorrer(1, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(2, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(3, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(6, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(7, i, j, linea, copia) in ocupado:
            total += 1

    # * INFERIOR

    elif i == len(array)-1 and j == 0:

        if recorrer(0, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(3, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(5, i, j, linea, copia) in ocupado:
            total += 1

    elif i == len(array)-1 and j == len(linea)-2:

        if recorrer(0, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(2, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(4, i, j, linea, copia) in ocupado:
            total += 1

    elif i == len(array)-1 and j != 0 and j != len(linea)-2:

        if recorrer(0, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(2, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(3, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(4, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(5, i, j, linea, copia) in ocupado:
            total += 1

    # * MEDIO

    elif i != 0 and i != len(array)-1 and j == 0:

        if recorrer(0, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(1, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(3, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(5, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(7, i, j, linea, copia) in ocupado:
            total += 1

    elif i != 0 and i != len(array)-1 and j == len(linea)-2:

        if recorrer(0, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(1, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(2, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(4, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(6, i, j, linea, copia) in ocupado:
            total += 1

    elif i != 0 and i != len(array)-1 and j != 0 and j != len(linea)-2:

        if recorrer(0, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(1, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(2, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(3, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(4, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(5, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(6, i, j, linea, copia) in ocupado:
            total += 1
        if recorrer(7, i, j, linea, copia) in ocupado:
            total += 1

    if total >= 5:
        tmp = list(array[i])
        tmp[j] = 'L'
        array[i] = "".join(tmp)


def getOcuppiedSeats_v2(copia):

    global array

    for i in range(0, len(array), 1):  # de 0 a longitud-1

        linea = array[i]

        for j in range(0, len(linea)-1, 1):  # de 0 a (len(linea)-1)-1

            if linea[j] == "L":

               checkFree_v2(i, j, linea, copia)

            elif linea[j] == '#':

                checkOcuppied_v2(i, j, linea, copia)


def main_Function_v2():

    lectura()

    copia = array[:]
    getOcuppiedSeats_v2(copia)
    while(array != copia):

        copia = array[:]
        getOcuppiedSeats_v2(copia)

    return countEmptySeats()


if __name__ == '__main__':

    print("parte 1 = ", main_Function())
    array = []
    print("parte 2 = ", main_Function_v2())
