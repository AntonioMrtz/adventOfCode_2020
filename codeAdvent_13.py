'''
Created on 10 August 2021

@author: Antonio Martínez Fernández
'''

# PART 1

timestamp=0
number=0
smallest=999999999999

# PART 2

actual_time=0
actual_bus=0
start_time=0

x=["x"]



def busFinder():

    global timestamp
    global smallest
    global number

    archivo = open("input12.txt")
    linea = archivo.readline()
    timestamp=int(linea)
    linea=archivo.readline()
    linea=linea.split(",")
    
    for bus in linea:
        
        if bus!="x":
            
            aux=timestamp // int(bus)

            if(aux*int(bus)<timestamp):
                mod=((aux+1)*int(bus))-timestamp

            else:

                mod=aux-timestamp



            if mod<smallest:
                number=int(bus)
                smallest=mod

    

def mainFunction():

    busFinder()
    print("bus número ",number," , tiempo de espera ",smallest," min","\n")


def checkSequence_old(linea): # ! deprecated , demasiado lenta

    global actual_bus
    global actual_time
    global start_time
    i=0 # caracter actual que toca

    while True:
        
        #print("BUS ",actual_bus)
        #print("TIME ",actual_time)

        if(actual_bus not in x):
            
            actual_bus=int(actual_bus)
            if (actual_time % actual_bus == 0 and i+1==len(linea)):

                print("timestamp where the sequence starts ",start_time)
                break

            elif(actual_time % actual_bus == 0 and i<len(linea)):
                i+=1
                actual_bus=linea[i]

                if(start_time==0):
                    start_time=actual_time

            else:
        
                actual_bus=linea[0]
                i=0
                start_time=0
        else:
            i+=1
            actual_bus=linea[i]

        
            
        actual_time+=1

def mainFunction():

    busFinder()
    print("bus número ",number," , tiempo de espera ",smallest," min","\n")
    print("answer = ",number*smallest)


def checkSequence(linea):  # * objetivo , buscar a partir de los multiplos del primero

    global actual_bus
    global actual_time
    global start_time
    i=0 # caracter actual que toca
    contador=1

    actual_time=int(linea[0])*1  # en este caso empieza en el segundo 17

    while True:
        
        #print("BUS ",actual_bus)
        #print("TIME ",actual_time)

        if(actual_bus not in x):
            
            actual_bus=int(actual_bus)
            if (actual_time % actual_bus == 0 and i+1==len(linea)):

                print("timestamp where the sequence starts ",start_time)
                break

            elif(actual_time % actual_bus == 0 and i<len(linea)):
                i+=1
                actual_bus=linea[i]

                if(start_time==0):
                    start_time=actual_time

                actual_time+=1

            else:
        
                actual_bus=linea[0]
                i=0
                start_time=0
                contador+=1
                actual_time=int(linea[0])*contador
        else:
            i+=1
            actual_bus=linea[i]
            actual_time+=1
        
            
        


def mainFunction_v2():

    global actual_bus

    archivo = open("input12.txt")
    #archivo = open("prueba.txt")
    archivo.readline()
    linea=archivo.readline()
    linea=linea.split(",")

    actual_bus=linea[0]
    checkSequence(linea)



if __name__ == '__main__':

    mainFunction()
    mainFunction_v2()
    

    