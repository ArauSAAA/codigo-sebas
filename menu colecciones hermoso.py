import time
def menu(): #Menu del aplicativo
    print("+" + "-" * 60 + "+")
    print("|" + " " *20 + " Menú Principal " + " " *24 + "|")
    print("|" + "-" *60 + "|")
    print("|" + " " *12 + "1. Ingresar superhéroes a una lista o tupla  " + " " *16 + "|")
    print("|" + " " *12 + "2. Analizando a mi mascota" + " " *22 + "|")
    print("|" + " " *12 + "3. Salir" + " " *40 + "|")
    print("+" + "-" * 60 + "+")
    print(" ")


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
    perro = {
        "nombre": "manchas",
        "hambre": False,
        "sed": False,
        "aburrido": True,
        "peso": 8.3,
        "energía": 45,
        "vida": True,
        "foto": "(°^°)/"
    }

    def alimentar(perro):
        try:
            if not perro["hambre"]:
                print(f"{perro['nombre']} no tiene hambre por el momento")
            else:
                perro["hambre"] = False
                perro["peso"] += 1
                perro["energía"] += 0.5
        except KeyError as e:
            print(f"Error: La clave {e} no existe en el diccionario.")

    def beber(perro):
        try:
            if not perro["sed"]:
                print(f"{perro['nombre']} no tiene sed por el momento")
            else:
                perro["sed"] = False
                perro["energía"] += 0.3
        except KeyError as e:
            print(f"Error: La clave {e} no existe en el diccionario.")

    def jugar(perro):
        try:
            if not perro["aburrido"]:
                print(f"{perro['nombre']} no está aburrido por el momento")
            else:
                perro["aburrido"] = False
                perro["energía"] -= 0.5
                perro["peso"] -= 0.5
        except KeyError as e:
            print(f"Error: La clave {e} no existe en el diccionario.")

    def estado(perro):
        try:
            print("Estado actual de la mascota:")
            for key, value in perro.items():
                print(f"{key}: {value}")

            if perro["peso"] > 15:
                print(f"{perro['nombre']} está con obesidad")

            if perro["energía"] < 5:
                print(f"{perro['nombre']} está con muy poca energía")

            if not perro["hambre"] and perro["sed"] and perro["aburrido"]:
                print(f"{perro['nombre']} puede que tenga alguna enfermedad")
        except KeyError as e:
            print(f"Error: La clave {e} no existe en el diccionario.")

    def cambiaEstado(perro):
        try:
            perro["hambre"] = True
            perro["sed"] = True
            perro["aburrido"] = True
        except KeyError as e:
            print(f"Error: La clave {e} no existe en el diccionario.")

    def menu():
        while True:
            print("\n---------------------------------------------------------------")
            print("+                       Submenú mascota                      +")
            print("+ 1. Alimentar                                                +")
            print("+ 2. Beber agua                                               +")
            print("+ 3. Jugar                                                    +")
            print("+ 4. Estado mascota                                           +")
            print("+ 5. Cambiar valores de la mascota                            +")
            print("+ 6. Volver a menú principal                                  +")
            print("---------------------------------------------------------------")
            opcion = input("Digite opción: ")

            if opcion == "1":
                alimentar(perro)
            elif opcion == "2":
                beber(perro)
            elif opcion == "3":
                jugar(perro)
            elif opcion == "4":
                estado(perro)
            elif opcion == "5":
                cambiaEstado(perro)
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")

    menu()

# Llamada a la función principal


    
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