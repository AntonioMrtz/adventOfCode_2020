'''
Created on 07 August 2021

@author: Antonio Martínez Fernández
'''

import re

array = []

# ACTUAL COORDENATES

x_pos = 0
y_pos = 0
x_pos_way = 10
y_pos_way = 1
facing = "E"

# FACING COORDENATES

EAST = "E"
NORTH = "N"
SOUTH = "S"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"


def processMovement(letter, number):

    global x_pos
    global y_pos
    global facing

    if letter in NORTH:

        y_pos += number

    elif letter in SOUTH:

        y_pos -= number

    elif letter in EAST:

        x_pos += number

    elif letter in WEST:

        x_pos -= number

    elif letter in LEFT:

        if number == 90 and facing in NORTH:
            facing = WEST

        elif number == 180 and facing in NORTH:
            facing = SOUTH

        elif number == 270 and facing in NORTH:
            facing = EAST

        elif number == 90 and facing in SOUTH:
            facing = EAST

        elif number == 180 and facing in SOUTH:
            facing = NORTH

        elif number == 270 and facing in SOUTH:
            facing = WEST

        elif number == 90 and facing in EAST:
            facing = NORTH

        elif number == 180 and facing in EAST:
            facing = WEST

        elif number == 270 and facing in EAST:
            facing = SOUTH

        elif number == 90 and facing in WEST:
            facing = SOUTH

        elif number == 180 and facing in WEST:
            facing = EAST

        elif number == 270 and facing in WEST:
            facing = NORTH

    elif letter in RIGHT:

        if number == 90 and facing in NORTH:
            facing = EAST

        elif number == 180 and facing in NORTH:
            facing = SOUTH

        elif number == 270 and facing in NORTH:
            facing = WEST

        elif number == 90 and facing in SOUTH:
            facing = WEST

        elif number == 180 and facing in SOUTH:
            facing = NORTH

        elif number == 270 and facing in SOUTH:
            facing = EAST

        elif number == 90 and facing in EAST:
            facing = SOUTH

        elif number == 180 and facing in EAST:
            facing = WEST

        elif number == 270 and facing in EAST:
            facing = NORTH

        elif number == 90 and facing in WEST:
            facing = NORTH

        elif number == 180 and facing in WEST:
            facing = EAST

        elif number == 270 and facing in WEST:
            facing = SOUTH

    elif letter in FORWARD:

        if facing in NORTH:
            y_pos += number

        elif facing in SOUTH:
            y_pos -= number

        elif facing in EAST:
            x_pos += number

        elif facing in WEST:
            x_pos -= number


def main_Function():

    archivo = open("input11.txt")

    while True:
        linea = archivo.readline()

        if not linea:

            print("x= ", x_pos, " y = ", y_pos)
            print("Answer 1 = ", abs(x_pos)+abs(y_pos))

            break

        letter = re.search('[A-Z]+', linea)[0]
        number = int(re.search('\d+', linea)[0])

        processMovement(letter, number)


def processMovement_v2(letter, number):

    global x_pos
    global y_pos
    global facing
    global x_pos_way
    global y_pos_way

    if letter in NORTH:

        y_pos_way += number

    elif letter in SOUTH:

        y_pos_way -= number

    elif letter in EAST:

        x_pos_way += number

    elif letter in WEST:

        x_pos_way -= number

    elif letter in LEFT:

        if number == 90:

            aux = x_pos_way
            x_pos_way = y_pos_way*-1
            y_pos_way = aux

        elif number == 180:

            x_pos_way *= -1
            y_pos_way *= -1

        elif number == 270:

            aux = x_pos_way
            x_pos_way = y_pos_way
            y_pos_way = aux*-1

    elif letter in RIGHT:

        if number == 90:

            aux = x_pos_way
            x_pos_way = y_pos_way
            y_pos_way = aux*-1

        elif number == 180:

            x_pos_way *= -1
            y_pos_way *= -1

        elif number == 270:

            aux = x_pos_way
            x_pos_way = y_pos_way*-1
            y_pos_way = aux

    elif letter in FORWARD:

        x_pos += x_pos_way*number
        y_pos += y_pos_way*number


def main_Function_v2():

    archivo = open("input11.txt")

    while True:
        linea = archivo.readline()

        if not linea:

            print("x= ", x_pos, " y = ", y_pos)
            print("Answer 2 = ", abs(x_pos)+abs(y_pos))

            break

        letter = re.search('[A-Z]+', linea)[0]
        number = int(re.search('\d+', linea)[0])

        processMovement_v2(letter, number)


if __name__ == '__main__':

    main_Function()
    print()
    x_pos = 0  # reinicializar variables
    y_pos = 0
    facing = EAST
    main_Function_v2()
