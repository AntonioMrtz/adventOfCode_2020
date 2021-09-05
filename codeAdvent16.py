'''
Created on 1 September 2021

@author: Antonio Martínez Fernández
'''

import re


lista_condiciones = []
my_ticket = []
lista_tickets = []   # all valid tickets


def procesLine(linea):

    lista_aux = re.findall(r"\d+-\d+ or \d+-\d+", linea)

    for aux in lista_aux:

        lista_condiciones.append(aux)


def check_requirements(i):

    for aux in lista_condiciones:

        aux = aux.strip()
        aux = aux.split("or")

        aux1 = aux[0]
        aux2 = aux[1]

        aux1 = aux1.split("-")
        a = int(aux1[0])
        b = int(aux1[1])

        aux2 = aux2.split("-")
        c = int(aux2[0])
        d = int(aux2[1])

        if (i >= a and i <= b) or (i >= c and i <= d):
            return True

    return False


def check_possible(values_per_field):

    global lista_condiciones

    check = 0
    actual_cond = 0  # numero de campo/condicion

    ans = []  # options for each column

    for aux in lista_condiciones:  # para cada condicion - para cada columna

        check = 0

        aux = aux.strip()
        aux = aux.split("or")

        aux1 = aux[0]
        aux2 = aux[1]

        aux1 = aux1.split("-")
        a = int(aux1[0])
        b = int(aux1[1])

        aux2 = aux2.split("-")
        c = int(aux2[0])
        d = int(aux2[1])

        for i in values_per_field:

            if not ((i >= a and i <= b) or (i >= c and i <= d)):
                check = 1

        if check == 0:
            ans.append(actual_cond)

        actual_cond += 1

    return ans


def main_function():

    ans = 0

    archivo = open("input14.txt", "r")
    linea = archivo.readline()

    while not linea in '\n':

        procesLine(linea)
        linea = archivo.readline()

    for i in range(4):
        archivo.readline()

    while True:

        contador = 0
        cont_aux = 0

        linea = archivo.readline()
        linea = linea.replace("\n", "")

        if not linea:
            break

        aux = linea.split(",")

        long = len(aux)

        for i in aux:

            if check_requirements(int(i)):

                contador += 1
            else:
                cont_aux += int(i)

        if long != contador:
            ans += cont_aux

    return ans


def main_function_v2():

    archivo = open("input14.txt")

    linea = archivo.readline()

    while not linea in '\n':

        procesLine(linea)
        linea = archivo.readline()

    archivo.readline()  # linea your ticket
    linea = archivo.readline()

    linea = linea.split(",")

    for i in linea:
        my_ticket.append(i)

    archivo.readline()  # linea nearby tickets
    archivo.readline()

    while True:

        aux = 0

        linea = archivo.readline()

        if linea:

            linea = linea.replace("\n", "")
            linea = linea.split(",")

        if not linea:
            break

        # guardamos los tickets válidos

        for i in linea:

            if not check_requirements(int(i)):
                aux = 1

        if aux == 0:

            lista_aux = []

            for a in linea:

                lista_aux.append(a)

            lista_tickets.append(lista_aux)

    value_and_pos = {}  # diccionario de que campo es cada cual

    for i in range(0, len(lista_tickets[0]), 1):  # posicion actual del campo

        values_per_field = []

        for ticket in lista_tickets:

            values_per_field.append(int(ticket[i]))

        value_and_pos[i] = check_possible(values_per_field)

        # value_and_pos[primera columa]=posicion de la condicion

    while True:

        parada = 0

        for i in value_and_pos:

            if len(value_and_pos.get(i)) > 1:

                for j in value_and_pos:

                    if len(value_and_pos.get(j)) == 1 and value_and_pos.get(j)[0] in value_and_pos.get(i) and j != i:

                        value_and_pos[i].remove(value_and_pos.get(j)[0])

        for i in value_and_pos:

            if len(value_and_pos.get(i)) != 1:
                parada = 1

        if parada == 0:

            break

    answer = []

    # posicion ticket - posicion campo

    for i in value_and_pos:

        if value_and_pos.get(i)[0] >= 0 and value_and_pos.get(i)[0] <= 5:

            answer.append(i)

    sol = 1

    for i in range(0, len(my_ticket), 1):

        if i in answer:

            sol *= int(my_ticket[i])

    return sol


if __name__ == '__main__':

    print(">>> Parte 1 = ", main_function())

    lista_condiciones = []
    my_ticket = []
    lista_tickets = []
    
    print(">>> Parte 2 = ", main_function_v2())
