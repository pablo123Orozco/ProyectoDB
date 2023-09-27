import tkinter as tk
from Usuarios import main1
from Proveedor import main
def abrir_ventana_usuario():
    ventana.withdraw()  # Oculta la ventana principal
    main1()
    ventana.deiconify()  # Vuelve a mostrar la ventana principal cuando se cierre la ventana de usuario

def abrir_ventana_proveedor():
    ventana.withdraw()
    main()
    ventana.deiconify()

def usuario():
    global ventana
    ventana = tk.Tk()
    ventana.title("Gestión de Usuarios")
    ventana.geometry("1300x850")

    resultado = tk.Label(ventana, text="")
    resultado.pack()

    boton_crear = tk.Button(ventana, text="Usuario", command=abrir_ventana_usuario)
    boton_crear.pack()
    boton_crear.place(x=40, y=50)
    
    proveedor = tk.Button(ventana, text="Proveedor",command=abrir_ventana_proveedor)
    proveedor.pack()
    proveedor.place(x=40, y=90)

    ventana.mainloop()

if __name__ == "__main__":
    usuario()
 