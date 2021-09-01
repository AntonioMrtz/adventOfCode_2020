'''
Created on 29 August 2021

@author: Antonio Martínez Fernández
'''

from collections import defaultdict

input_v1 = [0, 3, 6]
input_v2 = [9, 3, 1, 0, 8, 4]

FINAL_NUMBER_V1 = 2020
FINAL_NUMBER_V2 = 30000000


dic = defaultdict(lambda: int(-1))


def main_function():

    actual_seq = []

    for i in range(0, FINAL_NUMBER_V1):

        if i <= len(input_v1)-1:
            actual_seq.append(input_v1[i])

        else:

            control = 0

            for aux in range(len(actual_seq)-2, -1, -1):

                if actual_seq[i-1] == actual_seq[aux]:

                    ans = i-(aux+1)
                    actual_seq.append(ans)
                    control += 1
                    break

            if control == 0:
                actual_seq.append(0)

    return actual_seq[-1]


def main_function_larger():

    for i in range(len(input_v2)-1):

        dic[input_v2[i]] = i

    actual = input_v2[len(input_v2)-1]

    for i in range(len(input_v2), FINAL_NUMBER_V2+1):

        aux = actual

        if(i == FINAL_NUMBER_V2):

            return actual

        if dic[actual] != -1:

            nuevo = i-dic[actual]
            nuevo -= 1
            dic[actual] = nuevo
            actual = nuevo

        else:

            dic[actual] = i
            actual = 0

        dic[aux] = i-1


if __name__ == '__main__':
    print(">>> PART 1 = ", main_function())
    print(">>> PART 2 = ", main_function_larger())
