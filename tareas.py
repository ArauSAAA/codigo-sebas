from tkinter import *


class Tareas:
    tareasHechas=[]
    tareasNoHechas=[]
    def __init__(self):
        self.ventana= Tk()
        self.ventana.title('verificador de tareas')

        self.entrada= Entry(self.ventana)
        self.entrada.grid(row=0,column=0)

        self.botonAgregar= Button(self.ventana, text='agregar', command=self.agregar)
        self.botonAgregar.grid(row=0,column=1)

        self.botonQuitar= Button(self.ventana, text='completar', command=self.quitar)
        self.botonQuitar.grid(row=0,column=2)

        self.tareasNoHecha= StringVar(value=self.tareasNoHechas)
        self.tareasHecha= StringVar(value=self.tareasHechas)

        self.lista=Listbox(self.ventana, listvariable=self.tareasNoHecha)
        self.lista.grid(row=1,column=0)


        self.lista2=Listbox(self.ventana, listvariable=self.tareasHecha)
        self.lista2.grid(row=1,column=1)



    def correr(self):
        self.ventana.mainloop()

    def agregar(self):

        self.texto= self.entrada.get()
        if  self.texto == '':
            pass
        else:
            self.tareasNoHechas.append(self.texto)
            self.lista.insert(len(self.tareasNoHechas), f'{self.texto}')
            self.entrada.delete(0, END)


    def quitar(self):
        
        self.cosa= self.lista.curselection()

        self.tareasHechas.insert(self.cosa[0], self.lista2.get(self.cosa[0]) )

        self.elemento= self.lista.get(self.cosa[0])

        self.lista2.insert(len(self.tareasHechas), f'{self.elemento}✅')

        self.tareasNoHechas.pop(self.cosa[0])
        self.lista.delete(self.cosa)

        
        


app=Tareas()
app.correr()
