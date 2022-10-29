# Se importa de la libreria tkinter todas sus funciones

from tkinter import *

#----------------------------
# Ventana Principal
#----------------------------

# Se declara una ventana llamada ventana_principal y que adquiera las características de un objeto de tipo Tk
ventana_principal = Tk()

# Títutlo de la ventana
ventana_principal.title("Sistemas Uis")

# Dimensiones/Tamaño de la ventana, 1ro ancho y 2do alto.
ventana_principal.geometry("500x500")

# Deshabilitar botón de maximizar
ventana_principal.resizable(0,0)

ventana_principal.config(bg= "purple")

#---------------------------
#Frame entrada datos
#---------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="yellow", width=480, height=240)
frame_entrada.place(x=10,y=10)

#------------------
#Frame operaciones
#------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=480, height=120)
frame_operaciones.place(x=10, y=240)

#--------------
#Frame output
#--------------

frame_output = Frame(ventana_principal)
frame_output.config(bg="red", width= 480, height=120)
frame_output.place(x=10,y=360)

# Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "UIS Socorro")
titulo.config(bg="white", fg="blue", font=("Arial", 16))
titulo.place(x=10, y=10)

# Se ejecuta el método mainloop() de la clase Tk a través de la instancia (objeto). Éste método despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en un botón, escribir , etc...) Cada acción del usuario se conoce como un evento. El método mainloop es un bucle infinito.
ventana_principal.mainloop()