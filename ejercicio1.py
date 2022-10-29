# Se importa de la libreria tkinter todas sus funciones

from tkinter import *

#----------------------------
# Ventana Principal
#----------------------------

#Se declara una ventana llamada ventana_principal y que adquiera las características de un objeto de tipo Tk
ventana_principal = Tk()

# Se ejecuta el método mainloop() de la clase Tk a través de la instancia (objeto). Éste método despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en un botón, escribir , etc...) Cada acción del usuario se conoce como un evento. El método mainloop es un bucle infinito.
ventana_principal.mainloop()