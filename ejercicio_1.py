# Ejercicio 1 Tkinter


from cProfile import label
from cgitb import text
from sys import builtin_module_names
from tkinter import *
from tkinter import messagebox


#-------------------
#Funciones de la app
#-------------------

def sumar():
    messagebox.showinfo("Suma 1.0", "Hizo click en el botón sumar")
    z = int(x.get()) + int(y.get())
    t_resultados.insert(INSERT, "La suma de "+ x.get() + " + " + y.get() + " casi siempre es "+ str(z) + "\n")


def borrar():
    messagebox.showinfo("Borrar 1.0", "Hizo click en el botón borrar")
    x.set("")
    y.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Salir 1.0", "La app se cerrará.")
    ventana.destroy()


ventana = Tk()


ventana.title("Sistemas uis")

ventana.geometry("500x500")

ventana.resizable(0,0)

ventana.config(bg="black")


#---------------------
#Variables Locales
#---------------------

x = StringVar()
y = StringVar()

#Frame entrada

frame_entrada= Frame(ventana)
frame_entrada.config(bg="white", width=480, height=480)
frame_entrada.place(x=10, y=10)

#Logo
logo= PhotoImage(file="img/logo uis.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=10, y=10)

# Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Suma Enteros" )
titulo.config(bg="black", fg="green", font=("Arial",16))
titulo.place(x=240, y=10)

# Etiqueta para x

lb_x = Label(frame_entrada, text="X = ")
lb_x.config(bg="black", fg="red", font=("Arial",16))
lb_x.place(x=240 , y=50 , width=115 , height=30)

#Entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial", 20), justify=LEFT)
entry_x.focus_set()
entry_x.place(x=355 , y=50, width=115 , height=30)

# Etiqueta para y

lb_y = Label(frame_entrada, text="Y =")
lb_y.config(bg="black", fg="blue", font=("Arial",16))
lb_y.place(x=240 , y=90 , width=115 , height=30)

# Entry para y
entry_y = Entry(frame_entrada, textvariable=y)
entry_y.config(font=("Arial", 20), justify=LEFT)
entry_y.focus_set()
entry_y.place(x=355 , y=90, width=115 , height=30)


#Frame operaciones

frame_operaciones = Frame(ventana)
frame_operaciones.config(bg="red", width=480, height=120)
frame_operaciones.place(x=10 , y=260)

# Boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45 , y=45 , width=100, height=30)

# Boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190 , y=45 , width=100, height=30)

# Boton para salir

bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335 , y=45 , width=100, height=30)

# Frame resultados
frame_resultados = Frame(ventana)
frame_resultados.config(bg="white", width=450, height=100)
frame_resultados.place(x=10 , y=390)

# Area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial", 20))
t_resultados.place(x=10 , y=10 , width=490 , height=80)

# Mostrar interfaz
ventana.mainloop()
