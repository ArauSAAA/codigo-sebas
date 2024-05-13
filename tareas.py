from tkinter import *


class Tareas:
    tareasHechas=[]
    tareasNoHechas=[]
    def __init__(self):
        self.ventana= Tk()
        self.ventana.title('verificador de tareas')

        self.entrada= Entry(self.ventana)
        self.entrada.grid(row=0,column=0)

        self.botonAgregar= Button(self.ventana, text='agregar')
        self.botonAgregar.grid(row=0,column=1)

        self.botonQuitar= Button(self.ventana, text='quitar')
        self.botonQuitar.grid(row=0,column=2)

    def correr(self):
        self.ventana.mainloop()

    def agregar(self):
        pass

    def quitar(selfg):
        pass



x=Tareas()

x.correr()
