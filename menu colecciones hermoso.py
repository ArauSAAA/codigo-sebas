import time


def menu(): #Menu del aplicativo
    print("+" + "-" * 60 + "+")
    print("|" + " " *20 + " Menú Principal " + " " *24 + "|")
    print("|" + "-" *60 + "|")
    print("|" + " " *12 + "1. Ingresar superhéroes a una lista o tupla	" + " " *16 + "|")
    print("|" + " " *12 + "2. Analizando a mi mascota" + " " *22 + "|")
    print("|" + " " *12 + "3. Salir" + " " *40 + "|")
    print("+" + "-" * 60 + "+")
    print(" ")


def subMenuMascota():
    print('''---------------------------------------------------------------
+			Submenú mascota		+
+ 1. Alimentar					+
+ 2. Beber agua					+
+ 3. Jugar						+
+ 4. Estado mascota					+
+ 5. Cambiar valores de la mascota			+
+ 6. Volver a menú principal				+
------------------------------------------------------------------------
''')


def alimentar(mascota):
    
    if mascota['hambre'] == False:
        return (f'{mascota['nombre']} no tiene hambre por el momento')
    elif mascota['hambre']:
        mascota['hambre']= False
        mascota['peso']= mascota['peso'] + 1
        mascota['energia']= mascota['energia']+0.5


def beber(mascota):
    if mascota['sed'] == False:
        print(f'{mascota['nombre']} no tiene sed por el momento ')






def superHeroes():
    correr= False
    listaHeroes=[]
    while not correr:
        
        ponerHeroe=input('\nEscriba un heroe:').lower()
        listaHeroes.append(ponerHeroe)
        
        if listaHeroes.count(ponerHeroe) >1:
            print('ya exite elija otro')
            listaHeroes.remove(ponerHeroe)

        if ponerHeroe == 'fin':
            return

        if ponerHeroe == 'm':
            listaHeroes.remove(ponerHeroe)
            count=1
            for i in listaHeroes:
                print(f'{count}.{i}', end= ' / ')
                count+=1
            

        if ponerHeroe == '':
            print('campo vacio')
            listaHeroes.remove(ponerHeroe)

        if ponerHeroe.isdigit(): 
            print('debe ingresar un heroe valido')
            listaHeroes.remove(ponerHeroe)



def analizarMascota():
    
    while True:
        try:
            opcion2= int(input('Digite numero:'))
            
            
            perro = {
            'nombre':'manchas', 
            'hambre':True,
            'sed':False,
            'aburrido': True, 
            'peso': 8.3,
            'energía':45, 
            'vida': True,
            'foto':'(°^°)/'
            }
            subMenuMascota()
                
            print(f'peso:{perro['peso']}')
            print(f'energia:{perro["energía"]}\n')

            print(f'{perro["foto"]}\n')
                
            match opcion2:
                    case 1:
                        print(alimentar(perro))
                    case 2:
                        beber(perro)
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        return
                    case _:
                        print('digite un numero valido')
        except:
            print('dijite un numero')    



running= False

while not running:
    menu()
    try:
        opcion= int(input('Elige una opcion:'))
        match opcion:
            case 1:
                superHeroes()
            case 2:
                analizarMascota()
            case 3:
                running=True
                time.sleep(2)
            case _:
                print('ingrese una opcion valida !!!!!!!')
                time.sleep(3)
    except:
        print('tienes que dijitar un numero')
        time.sleep(3)
