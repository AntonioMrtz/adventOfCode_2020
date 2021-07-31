'''
Created on 31 july 2021

@author: Antonio Martínez Fernández
'''

array = []
lista = []


def lectura():
    archivo = open("input8.txt")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        array.append(int(linea))


def comprobar_suma(n):

    k1 = 0
    k2 = 0

    for i in lista:

        for j in lista:

            if i+j == n and k1 != k2:
                return True
            k2 += 1
        k2 = 0
        k1 += 1

    return False


def main_function():

    i = 0

    for n in array:

        if(i >= 25):
            if(comprobar_suma(array[i]) == False):
                print(array[i])
                return(array[i])
            lista.append(array[i])
            lista.pop(0)
            i += 1

        else:
            lista.append(array[i])
            i += 1


def clasificar_solucion():

    global lista
    menor = 999999999999999999999
    mayor = 0

    for actual in lista:
        if(actual < menor):
            menor = actual
        if(actual > mayor):
            mayor = actual

    return menor, mayor


def sumatorio():

    global lista
    total = 0

    for actual in lista:
        total += actual

    return total


def main_function_v2(n):

    global lista

    for i in range(0, len(array)-1, 1):

        lista.append(array[i])

        for j in range(i+1, len(array)-1, 1):

            lista.append(array[j])
            if(sumatorio() == n):

                print(clasificar_solucion())
                return 0

            elif(sumatorio() > n):
                lista = []

                break


if __name__ == '__main__':

    lectura()
    aux = main_function()
    lista = []
    print()
    main_function_v2(aux)
