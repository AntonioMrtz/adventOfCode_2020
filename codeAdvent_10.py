'''
Created on 31 july 2021

@author: Antonio Martínez Fernández
'''

array=[]
contador=0

diff_1=0
diff_3=1 # el ultimo siempre será diferencia de 3

def lectura():
    archivo = open("input9.txt")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        array.append(int(linea))
    array.sort()

def getChained_Addapters():

    global diff_1
    global diff_3
    anterior=0

    for i in array:

        if(i-anterior==3):
            diff_3+=1
            
                
        elif(i-anterior==1):
            diff_1+=1
            

        anterior=i
        

    return diff_1*diff_3

def allChained_Combinations():
    dp = [1]
    
    
    for i in range(1, len(array)): # recorre desde el 1
        ans = 0
        for j in range(i):        # recorre los anteriores a i
            
            if array[j] + 3 >= array[i]: # comprueba si no es imprescindible
                ans += dp[j]
        
        dp.append(ans)  # para cada numero escribe el total acumulado de posibilidades

    print("part 2", dp[len(array)-1])
    


if __name__ == '__main__':
    lectura()
    print("part 1 ",getChained_Addapters())
    allChained_Combinations()