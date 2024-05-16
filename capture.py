from tkinter import *
import pyautogui
import time


def tomarFoto():
    texto= entrada.get()
    foto= pyautogui.screenshot()
    foto.save(f'{texto}.png')
    entrada.delete(0,END)

ventana= Tk()

entrada= Entry(ventana)
entrada.grid(row=0,column=0)

boton= Button(ventana, text='tomar foto', command=tomarFoto)
boton.grid(row=1, column=0, padx=10, pady=10)


ventana.mainloop()
