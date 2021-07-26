'''
Created on 26 july 2021

@author: Antonio Martínez Fernández
'''

h_id = 0

row_s = 0
row_e = 127
col_s = 0
col_e = 7

array=[]


# 128 rows     7 char =FRONT->0-mitad BACK->mitad-total
#  8  columns  3 char = R upper half , L lower half
# id = 8* row + column

def procesar(s):

    i = 1
    global row_s
    global row_e
    global col_s
    global col_e

    for c in s:
        if(i <= 7 and c == 'B'):

            row_s = (row_e+row_s)//2 + 1

        elif(i <= 7 and c == 'F'):

            row_e = (row_e+row_s)//2

        elif(i >= 7 and c == 'L'):

            col_e = (col_e+col_s)//2

        elif (i >= 7 and c == 'R'):

            col_s = (col_e+col_s)//2 + 1

        i += 1
    return 8*row_s+col_s


def lectura():
    global h_id
    global row_s
    global row_e
    global col_s
    global col_e
    global array

    with open('input4.txt') as f:
        for linea in f:
            aux = procesar(linea)
            if(aux > h_id):
                h_id = aux
            array.append(aux)
            row_s = 0
            row_e = 127
            col_s = 0
            col_e = 7


def encontrar_asiento(array):
    i=0
    for numero in array:

        if(i!=len(array)):

            if(array[i+1]-numero==2):
                return numero+1 

        i+=1

    return 0
        

if __name__ == '__main__':

    lectura()
    print(h_id)
    array.sort()
    print(encontrar_asiento(array))
    print(array)
