from tkinter import *
from tkinter import messagebox

class Tareas:
    tareasHechas=[]
    tareasNoHechas=[]
    def __init__(self):
        try:
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
            self.lista.grid(row=2,column=0)

            self.text= Label(self.ventana, text='tarea completa')
            self.text.grid(row=1, column=1)


            self.lista2=Listbox(self.ventana, listvariable=self.tareasHecha)
            self.lista2.grid(row=2,column=1)
        except:
            messagebox.showinfo(title='error', message='no selecciono ningun elemento')
    


    def correr(self):
        self.ventana.mainloop()

    def agregar(self):
        try:
            self.texto= self.entrada.get()
            if  self.texto == '':
                pass
            else:
                self.tareasNoHechas.append(self.texto)
                self.lista.insert(len(self.tareasNoHechas), f'{self.texto}')
                self.entrada.delete(0, END)
        except:
            messagebox.showinfo(title='error', message='no seleccionaste ningun elemento')

    def quitar(self):
        try:
            self.cosa= self.lista.curselection()

            self.tareasHechas.insert(self.cosa[0], self.lista2.get(self.cosa[0]) )

            self.elemento= self.lista.get(self.cosa[0])

            self.lista2.insert(len(self.tareasHechas), f'{self.elemento}✅')

            self.tareasNoHechas.pop(self.cosa[0])
            self.lista.delete(self.cosa)
        except:
            messagebox.showinfo(title='error', message='no seleccionaste ningun elemento')

        
        


app=Tareas()
app.correr()
