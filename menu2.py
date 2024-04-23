import time #utilizar libreria time, para realizar una pausa
import random #utilizar libreria, para generar números aleatorios
"""
en esta función, se deberá validar que la opción ingresada,
se encuentre entre 1 a 4"""
def validaOpcion():
    try:
        opcion = int(input("Ingrese la opción requerida:"))
        return opcion
    except:
        print('no se permiten simbolos ni numeros')
        time.sleep(3)
        return

def diaSemana():
    while True:
        try:
            ingresarDia= int(input('Ingresa un dia de la semana.'))
            match ingresarDia:
                case 1:
                    print('dia lunes')
                    time.sleep(3)
                    return
                case 2:
                    print('dia martes')
                    time.sleep(3)
                    return
                case 3:
                    print('dia miercoles')
                    time.sleep(3)
                    return
                case 4:
                    print('dia jueves')
                    time.sleep(3)
                    return
                case 5:
                    print('dia viernes')
                    time.sleep(3)   
                    return
                case 6:
                    print('dia sabado')
                    time.sleep(3)
                    return
                case 7:
                    print('dia domingo')
                    time.sleep(3)
                    return   
                case _:
                    print('tienes que ingresar un numero valido')
        except:
            print('este simbolo no es invalido')


def frecuencia():
    while True:
        try:
            opcion2= input('Quieres seguir? [S/N]').lower()
            match opcion2:
                case 's':
                    tupla=()
                    ingresarNumero= int(input('ingrese numero el largo de la tupla:'))

                    if ingresarNumero <= 0:
                        print('no puede poner un numero menor o igual a 0')
                        time.sleep(3)
                        

                    else:
                        for num in range(1,ingresarNumero+1):
                            n= random.randint(1,10)
                            tupla= tupla + (n,)

                        
                    
                        ingresarNumeroRepetido=int(input('ingrese numero repetido:'))
                        numFrecuencia= tupla.count(ingresarNumeroRepetido)

                        print(f'El numero {ingresarNumeroRepetido} se repite {numFrecuencia} veces')
                        print(tupla)
                case 'n':
                    print('has salido de la aplicacion')
                    time.sleep(3)
                    return
                case _:
                    print('es [S/N]') 


        except:
            print('no puedes agregar simbolos')
            time.sleep(5)
            return
        

def verduleria():
    listaCompras= []

    while True:
        try:
            tuplaFrutas= ()
            num=0

            diccionario= {'manzanas':1200,'platanos':1400,'uvas':2000,'naranjas':850,'peras':1000, 'tunas':1300}

            for clave,valor in diccionario.items():
                print(f'fruta:{clave}, valor:{valor}')
            
            elegirFruta= input('elige la fruta que te quieras llevar:').lower()
            elegirKilos= int(input('cuantos kilos Quieres?:'))
            seguir= input("¿Desea agregar otra fruta? (s/n): ").lower()


            frutasClaves= list(diccionario.keys())
            frutaValor= list(diccionario.values())
            valor= diccionario[elegirFruta]

            

            if elegirFruta in frutasClaves:
                tuplaFrutas+=(elegirFruta,elegirKilos,valor)
                listaCompras.append(tuplaFrutas)
            
            match seguir:
                case 'n':                
                    print('total compra')
                    num=0
                    for fruta in listaCompras:
                        num+=fruta[1]*fruta[2]
                        print(f'Fruta:{fruta[0]} kilos {fruta[1]} valor {fruta[2]}. Total parcial {fruta[1]*fruta[2]}')
                        print(f'Total compra:{num}')
                    return
        except:
            print('no esta tal fruta')



def menu(): #Menu del aplicativo
    print("+" + "-" * 60 + "+")
    print("|" + " " *20 + " Menú Principal " + " " *24 + "|")
    print("|" + "-" * 60 + "|")
    print("|" + " " *12 + "1. Determinar el día en palabras" + " " *16 + "|")
    print("|" + " " *12 + "2. Frecuencia de un número" + " " *22 + "|")
    print("|" + " " *12 + "3. Venta de frutas" + " " *30 + "|")
    print("|" + " " *12 + "4. Salir" + " " *40 + "|")
    print("+" + "-" * 60 + "+")
    print(" ")

while True:
    menu()
    opcion = validaOpcion() 
    match opcion:
        case 1:
            diaSemana()
        case 2:
            frecuencia()
        case 3:
            verduleria()
            time.sleep(2)
        case 4:
            print("Adios")
            time.sleep(3)
            break
        case _:
            print('ese numero no es valido')
            time.sleep(3)
            
            
            
            
            
            
