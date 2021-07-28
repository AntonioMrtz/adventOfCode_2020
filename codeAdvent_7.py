'''
Created on 27 july 2021

@author: Antonio Martínez Fernández
'''
import re

array = []
validas = []
total = 0
global_v2 = 0
control = 0


def tratar(s):
    global validas
    corte = s.split(" contain ")
    bolsa = corte[0].split(" bags")[0]
    aux = corte[1].split(', ')

    for c in aux:

        c = c.split(" bag")
        aux2 = re.sub(r'[0-9]+ ', '', c[0])

        if((aux2 == "shiny gold" or aux2 in validas) and bolsa not in validas):
            validas.append(bolsa)
            return 1

    return 0


def lectura():

    global total
    archivo = open("input6.txt")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        array.append(linea)
        total += tratar(linea.rstrip())


def lectura_sin_tratar():

    global total
    archivo = open("prueba.txt")     # ! CUIDADO QUE TIENE PUESTO PRUEBA
    while True:
        linea = archivo.readline()
        if not linea:
            break
        array.append(linea)


def tratar_array():
    global total
    for linea in array:
        total += tratar(linea)


def busqueda_recursiva(s):  # string s

    # buscar la linea del estilo s-> bolsas

    # si contain no bag -> return 0

    # else return numero_bolsa1*busqueda_recursvia(bolsa1+1) +
    #   numero_bolsan*busuqueda_recursiva(bolsan+1)

    global global_v2
    global array
    global control
    aux4 = 0

    for linea in array:

        corte = linea.split(" contain ")  # corte[1]  -> y
        bolsa = corte[0].split(" bags")[0]  # x ->

        if bolsa == s and re.match("no other bags.", str(corte[1])) != None:

            return 0

        elif bolsa == s:

            aux = corte[1].split(', ')
            for c in aux:

                c = c.split(" bag")

                aux2 = re.sub(r'[0-9]+ ', '', c[0])
                aux3 = re.search(r"^[0-9]+", c[0]).group()

                aux4 += int(aux3)*(busqueda_recursiva(aux2)+1)
                # numero de bolsas del color * (recursividad + bolsa actual(1))

            return aux4


if __name__ == '__main__':

    lectura()

    for i in range(6):
        tratar_array()
    print(total)
    print()

    lectura_sin_tratar()
    print(busqueda_recursiva("shiny gold"))
