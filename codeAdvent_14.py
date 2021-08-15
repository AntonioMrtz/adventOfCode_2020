'''
Created on 13 August 2021

@author: Antonio Martínez Fernández
'''

ans = 0
mask = "000000000000000000000000000000000000"

dic = {}


def processMask(linea):

    global mask

    linea = linea.split("=")[1]
    linea = linea.strip()

    mask = linea


def processMem(linea):

    global mask

    aux = mask
    i_substring = 0

    linea = linea.strip()

    num = int(linea.split("=")[1])
    num = str(bin(num)[2:])  # -> binario

    pos = linea.split("=")[0].split("[")[1]
    pos = int(pos.replace("]", ""))

    # aplicar filtro
    for i in range(0, 36, 1):

        if((len(mask)-i) <= len(num)):

            if mask[i] == "X":
                aux = aux[:i]+num[i_substring]+aux[i+1:]

            i_substring += 1

    aux = aux.replace("X", "0")

    dic[pos] = aux


def processLine(linea):

    if linea[1] == 'a':

        processMask(linea)

    else:

        processMem(linea)


def processMem_v2(linea):

    global mask

    linea = linea.strip()

    num = int(linea.split("=")[1])  # = numero

    pos = linea.split("=")[0].split("[")[1]
    pos = int(pos.replace("]", ""))  # [memoria]
    binary_pos = str(bin(pos)[2:]).rjust(36, '0')  # ajustamos a 36 bits

    aux = []

    rec(mask, binary_pos, 0, aux)

    for i in aux:
        dic[int(i)] = num


def processLine_v2(linea):

    if linea[1] == 'a':

        processMask(linea)

    else:

        processMem_v2(linea)


def mainFunction():

    global ans

    archivo = open("input13.txt")
    linea = archivo.readline()

    while linea:

        processLine(linea)
        linea = archivo.readline()

    for i in dic:

        ans += int(int(dic.get(i), 2))

    print("part 1 ", ans)


def mainFunction_v2():
    global ans
    global dic

    dic = {}
    ans = 0

    archivo = open("input13.txt")
    #

    linea = archivo.readline()

    while linea:

        processLine_v2(linea)
        linea = archivo.readline()

    for i in dic:

        ans += int(dic.get(i))

    print("part 2 ", ans)

    


def rec(mask, mem, i, aux):

    if i == 36:
        aux.append(mem)
    elif mask[i] == "X":

        rec(mask, mem[:i]+"1"+mem[i+1:], i+1, aux)
        rec(mask, mem[:i]+"0"+mem[i+1:], i+1, aux)
    elif mask[i] == "1":
        rec(mask, mem[:i]+"1"+mem[i+1:], i+1, aux)
    else:
        rec(mask, mem, i+1, aux)


if __name__ == '__main__':

    mainFunction()
    mainFunction_v2()
