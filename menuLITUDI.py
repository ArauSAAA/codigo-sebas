import time


def menu():
    print('\n''''-------------------------------------------------------------------------------------
|        			Menú Principal   			            |
-------------------------------------------------------------------------------------
|   1.- Tuplas						    	                     |
|   2.- Diccionario 				                                     |
|   3.- Listas    							             |
|   4.- Salir							                     |
--------------------------------------------------------------------------------------
    
''')

def ejercicioTupla():

    tuplaPar= ()
    tuplaImpar= ()

    contador= 1
    while contador <= 10:
        
        try:
            ingresaNumero= int(input(f'Ingrese numero positivo {contador}:'))
            
            while ingresaNumero <= 0:
                ingresaNumero= int(input('INGRESA UN NUMERO POSITIVO!:'))
            

            if ingresaNumero % 2==0:
                tuplaPar+= (ingresaNumero,)
            else:
                tuplaImpar+= (ingresaNumero,)

            contador+=1
        except:
            print('error dato no válido')
        
    print(f'\ntuplaImpar={tuplaImpar}\n')
    print(f'\ntuplaPar={tuplaPar}\n')
    
    print('\nImpares\n')
    print(' / ' . join(str(num) for num in tuplaImpar) )
    print('\npares\n')
    print(' / ' . join(str(num) for num in tuplaPar) )

def ejercicioDiccionario():
    cadena = "10001-1,cemento melón,2590,140;10202-1,ladrillo fiscal,210,9000;10022- 9,ladrillo princesa,320,4000;10220-8,yeso,890,400"
    

def ejercicioListas():
    pass

def salir():
    global bucle
    bucle= True
    time.sleep(5)
    return bucle

bucle=False

while not bucle:
    menu()
    try:
        opcion= int(input('Digite Opción-------->'))

        match opcion:
            case 1:
                ejercicioTupla()
            case 2:
                ejercicioDiccionario()
            case 3:
                ejercicioListas()
            case 4:
                salir()
    except:
        print('debe de ingresar un numero')