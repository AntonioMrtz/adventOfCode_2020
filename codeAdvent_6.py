'''
Created on 26 july 2021

@author: Antonio Martínez Fernández
'''


array = []
array_v2 = []
contador = 0
contador_v2 = 0


def comprobar():
    global array
    aux = 0
    for i in range(26):
        if(array[i] == 1):
            aux += 1
    return aux


def lectura():
    global array
    global contador
    archivo = open("input5.txt")
    while True:
        linea = archivo.readline()

        if (linea.rstrip() == "" or not linea):
            contador += comprobar()  
            for i in range(26):
                array[i] = 0
            if(not linea):
                break
        else:
            for i in range(len(linea)-1):
                aux = ord(linea[i])-97
                array[aux] = 1
        


def comprobar_v2(m):
    global array_v2
    aux = 0

    for i in range(26):
        if(array[i] == m):
            aux += 1
    return aux


def lectura_v2():
    global array_v2
    global contador_v2

    miembros = 0
    archivo = open("input5.txt")
    while True:
        linea = archivo.readline()

        if (linea.rstrip() == "" or not linea):
            contador_v2 += comprobar_v2(miembros)
            miembros = 0
            for i in range(26):
                array[i] = 0
            if(not linea):
                break
        else:
            for i in range(len(linea)-1):
                aux = ord(linea[i])-97
                array[aux] += 1
            miembros += 1


if __name__ == '__main__':
    for i in range(26):
        array.append(0)

    for i in range(26):
        array_v2.append(0)

    lectura()
    lectura_v2()
    print(contador)
    print(contador_v2)
