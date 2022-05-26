from cgitb import grey
import re
from shutil import which
import tkinter as tk
from tkinter.tix import Tk

from setuptools import Command

ventana=tk.Tk()
ventana.title("Razones Financiera")
ventana.geometry('600x500')
ventana.configure(background='dark turquoise')

encabesado=tk.Label(ventana, text="Menu de Razones Financiera",bg="light blue")
encabesado.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)

enc=tk.Label(ventana, text="Seleccione una opción a ejecutar ",bg="light blue")
enc.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)



def ctn():
 
 

 ventana1=tk.Toplevel()
 ventana1.title("Capital del Trabajo Neto o fondo de maniobra")
 ventana1.geometry('600x500')
 ventana1.configure(background='dark turquoise')
 

 encabesado=tk.Label(ventana1, text="Ingrese los datos para calcular el Capital del Trabajo Neto (CTN)",bg="light blue")
 encabesado.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)

 def resta():
     resta=int(entrada1.get())-int(entrada2.get())
     return var.set(resta)

 e1=tk.Label(ventana1,text="Activo circulante:",bg="blue",fg="white")
 e1.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
 entrada1=tk.Entry(ventana1)
 entrada1.pack(padx=5,pady=5,ipadx=5,ipady=5)
 var=tk.StringVar()

 e2=tk.Label(ventana1,text="Pasivo circulante:",bg="blue",fg="white")
 e2.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
 entrada2=tk.Entry(ventana1)
 entrada2.pack(padx=5,pady=5,ipadx=5,ipady=5)

 botonresta=tk.Button(ventana1,text="Calcular CTN",fg="white",bg="SkyBlue4",command=resta)
 botonresta.pack(side=tk.TOP)

 interpretacion=tk.Label(ventana1, text='Si la empresa tueviese que pagar toda las deudas a corto plazo le quedaria un exedente de:',bg="light blue")
 interpretacion.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)

 res=tk.Label(ventana1,bg="light green",textvariable=var,padx=5,pady=5,width=50)
 res.pack()

 def clear_text():
       var.set( "" )
       entrada1.delete(0, "end")
       entrada2.delete(0, "end")
       return clear_text
 buttonlimpiar = tk.Button(ventana1, text="Limpiar", bg="khaki1", command=clear_text)
 buttonlimpiar.pack(padx=5,pady=10,ipadx=50,ipady=6)

 def cerrarVentana():
       ventana1.destroy()
 boton=tk.Button(ventana1,text="Salir",bg="violet",fg="black",command=cerrarVentana)
 boton.pack(padx=5,pady=10,ipadx=50,ipady=6)
    #---------------------------------------------------------------------------------------------------------------------------


boton1=tk.Button(ventana,text="Capital del Trabajo Neto (CTN)",bg="turquoise4",command=ctn,padx=5,pady=5,width=50).pack(padx=5,pady=10,ipadx=50,ipady=6)

def IS():

 ventana2=tk.Toplevel()
 ventana2.title("Razon de Circulante o Indice de Solvencia")
 ventana2.geometry('600x500')
 ventana2.configure(background='dark turquoise')

 encabesado=tk.Label(ventana2, text="Ingrese los datos para calcular la Razon del circulante (IS)",bg="light blue")
 encabesado.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)

 def division():
     division=int(entrada1.get())/int(entrada2.get())
     return var.set(division)

 e1=tk.Label(ventana2,text="Activo circulante:",bg="blue",fg="white")
 e1.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
 entrada1=tk.Entry(ventana2)
 entrada1.pack(padx=5,pady=5,ipadx=5,ipady=5)
 var=tk.StringVar()

 e2=tk.Label(ventana2,text="Pasivo circulante:",bg="blue",fg="white")
 e2.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
 entrada2=tk.Entry(ventana2)
 entrada2.pack(padx=5,pady=5,ipadx=5,ipady=5)

 botondivision=tk.Button(ventana2,text="Calcular el indice de solvencia (IS)",fg="white",bg="SkyBlue4",command=division)
 botondivision.pack(side=tk.TOP)

 interpretacion=tk.Label(ventana2, text='Califique a la empresa en base a la regla del indice de solvencia, ya que el "1" como el nivel óptimo, para no tener exceso de liquidez que se traduce en pérdidas de rentabilidad el cual su resultado es:',bg="light blue")
 interpretacion.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)

 res=tk.Label(ventana2,bg="light green",textvariable=var,padx=5,pady=5,width=50)
 res.pack()

 def clear_text():
       var.set( "" )
       entrada1.delete(0, "end")
       entrada2.delete(0, "end")
       return clear_text
 buttonlimpiar = tk.Button(ventana2, text="Limpiar", bg="khaki1", command=clear_text)
 buttonlimpiar.pack(padx=5,pady=10,ipadx=50,ipady=6)

 def cerrarVentana():
       ventana2.destroy()
 boton=tk.Button(ventana2,text="Salir",bg="violet",fg="black",command=cerrarVentana)
 boton.pack(padx=5,pady=10,ipadx=50,ipady=6)
 #----------------------------------------------------------------------------------------------------------------------
 
boton2=tk.Button(ventana,text="Razón de circulante o indice de solvencia (IS))",bg="turquoise4",command=IS,padx=5,pady=5,width=50).pack(padx=5,pady=10,ipadx=50,ipady=6)

def RPR():

 ventana3=tk.Toplevel()
 ventana3.title("Razón de prueva rapida o prueba acida (RPR)")
 ventana3.geometry('600x500')
 ventana3.configure(background='dark turquoise')

 encabesado=tk.Label(ventana3, text="Ingrese los datos para calcular la Razon de prueba rapida (RPR)",bg="light blue")
 encabesado.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)

 def fraccion():
     fraccion=(int(entrada1.get())-int(entrada2.get()))/int(entrada3.get())
     return var.set(fraccion)

 e1=tk.Label(ventana3,text="Activo circulante:",bg="blue",fg="white")
 e1.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
 entrada1=tk.Entry(ventana3)
 entrada1.pack(padx=5,pady=5,ipadx=5,ipady=5)
 var=tk.StringVar()

 e2=tk.Label(ventana3,text="Inventario:",bg="blue",fg="white")
 e2.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
 entrada2=tk.Entry(ventana3)
 entrada2.pack(padx=5,pady=5,ipadx=5,ipady=5)

 e3=tk.Label(ventana3,text="Pasivo circulante:",bg="blue",fg="white")
 e3.pack(padx=5,pady=4,ipadx=5,ipady=5,fill=tk.X)
 entrada3=tk.Entry(ventana3)
 entrada3.pack(padx=5,pady=5,ipadx=5,ipady=5)

 botonfraccion=tk.Button(ventana3,text="Calcular la Razón de prueba",fg="white",bg="SkyBlue4",command=fraccion)
 botonfraccion.pack(side=tk.TOP)

 interpretacion=tk.Label(ventana3, text='El resultado que se muestre indica que la empresa por cada peso que debe tiene esta cantidad para cubrirlo sin disponer del inventario, en donde su resultado es:',bg="light blue")
 interpretacion.pack(padx=5,pady=4,ipadx=5,ipady=10,fill=tk.X)

 res=tk.Label(ventana3,bg="light green",textvariable=var,padx=5,pady=5,width=50)
 res.pack()

 def clear_text():
       var.set( "" )
       entrada1.delete(0, "end")
       entrada2.delete(0, "end")
       entrada3.delete(0, "end")
       return clear_text
 buttonlimpiar = tk.Button(ventana3, text="Limpiar", bg="khaki1", command=clear_text)
 buttonlimpiar.pack(padx=5,pady=10,ipadx=50,ipady=6)

 def cerrarVentana():
       ventana3.destroy()
 boton=tk.Button(ventana3,text="Salir",bg="violet",fg="black",command=cerrarVentana)
 boton.pack(padx=5,pady=10,ipadx=50,ipady=6)
#---------------------------------------------------------------------------------------------------------------------------------  

boton3=tk.Button(ventana,text="Razón de prueba rápida (RPR)",bg="turquoise4",command=RPR,padx=5,pady=5,width=50).pack(padx=5,pady=10,ipadx=50,ipady=6)

def cerrarVentana():
       ventana.destroy()
boton=tk.Button(ventana,text="Salir",bg="violet",fg="black",command=cerrarVentana)
boton.pack(padx=5,pady=10,ipadx=50,ipady=6)



ventana.mainloop()