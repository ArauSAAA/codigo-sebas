def menu():
    
    condicion= False
    while not condicion:
        try:
            print('''********************************
* \t Menu principal
* 1.Vocal o cosonante
* 2.Palindromo
* 3.Salid
********************************''')
            numero= int(input('Elija una opcion:'))
            match numero:
                case 1:
                    vocalOConsonante()
                case 2:
                    palindromo()
                case 3:
                    condicion= True
                case _:
                    print('debe ingresar un numero del 1 al 3 tampoco una letra')
        except:
            print('tienes que digitar un numero')

def vocalOConsonante():
    condicion= False
    while not condicion:
    
        letra= input('Escriba una letra:')
        if len(letra) > 1:
            print('Tiene que ser una vocal o consonante. Intente nuevamente')
            condicion= True
        elif letra.lower().isdigit():
            print('no puede ingresar un numero intentelo de nuevo')
            condicion= True
        else:
            if letra.lower() in 'aeiou':
                print('vocal')
            elif letra.lower() in 'bcdfghjklmnñpQrstvxzwy':
                print('consonante')


def palindromo():
    condicion= False
    while not condicion:
        Palabra=input('Escribe cualquier palabra que tenga minimo 3 letras:')

        if  Palabra.isdigit():
            print('no puedes colocar un numero')
            condicion = True
            
        elif len(Palabra) < 3:
            print('no puede ingresar, esa palabra')
        elif Palabra == Palabra[::-1] :
            print(f'{Palabra} Es palindromo')
        else:
            print(f'({Palabra}) no es palindromo')

menu()

