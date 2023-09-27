import tkinter as tk
from tkinter.ttk import Treeview

def main():

    ventana = tk.Tk()
    ventana.title("Clientes")
    ventana.geometry("1300x850")
    marco = tk.LabelFrame(ventana)
    marco.place(x=350, y=50, width=750, height=650)

    global nombre, apellido, direccion  , telefono, empresa,txtnombre,txtapellido,txttelefono,txtdireccion,txtempresa
    nombre =tk.StringVar()
    apellido = tk.StringVar()
    direccion =tk.StringVar()
    telefono =tk.StringVar()
    empresa = tk.StringVar()

    lblnombre = tk.Label(marco, text="Nombre")
    lblnombre.grid(column=0, row=0, padx=5, pady=5)
    txtnombre = tk.Entry(marco,textvariable=nombre)
    txtnombre.grid(column=1,row=0)

    lblapellido = tk.Label(marco, text="Apellido")
    lblapellido.grid(column=2, row=0, padx=5, pady=5)
    txtapellido = tk.Entry(marco,textvariable=apellido)
    txtapellido.grid(column=3,row=0)

    lbltelefono = tk.Label(marco, text="telefono")
    lbltelefono.grid(column=0, row=1, padx=5, pady=5)
    txttelefono=tk.Entry(marco,textvariable=telefono)
    txttelefono.grid(column=1, row=1)

    lbldireccion = tk.Label(marco, text="Direccion")
    lbldireccion.grid(column=2, row=1, padx=5, pady=5)
    txtdireccion = tk.Entry(marco,textvariable=direccion)
    txtdireccion.grid(column=3,row=1)

    lblempresa = tk.Label(marco,text="Empresa")
    lblempresa.grid(column=0,row=4,padx=5,pady=5)
    txtempresa = tk.Entry(marco,textvariable=empresa)
    txtempresa.grid(column=1,row=4)

    global datos  
    datos = Treeview(marco)
    datos.grid(column=1, row=8, columnspan=5)
    datos["columns"] = ("ID", "Nombre", "Apellido","Telefono", "Direccion","Empresa")
    datos.column("#0", width=0, stretch=tk.NO)
    datos.column("ID", width=90, stretch=False)
    datos.column("Nombre", width=80, stretch=False)
    datos.column("Apellido", width=80, stretch=False)
    datos.column("Telefono", width=100, stretch=False)
    datos.column("Direccion", width=100, stretch=False)
    datos.column("Empresa", width=100, stretch=False)
    datos.heading("ID", text="ID", anchor=tk.CENTER)
    datos.heading("Nombre", text="Nombre", anchor=tk.CENTER)
    datos.heading("Apellido", text="Apellido", anchor=tk.CENTER)
    datos.heading("Telefono", text="Telefono", anchor=tk.CENTER)
    datos.heading("Direccion", text="Direccion", anchor=tk.CENTER)
    datos.heading("Empresa", text="Empresa", anchor=tk.CENTER)
    btn_ver = tk.Button(marco, text="Ver")
    btn_ver.grid(column=1, row=10, padx=5, pady=5)
    btn_guardar = tk.Button(marco,text="Guardar")
    btn_guardar.grid(column=2,row=10,padx=5,pady=5)
    btn_actualizar = tk.Button(marco, text="Actualizar")
    btn_actualizar.grid(column=3,row=10,padx=5,pady=5)
    btn_Borrar = tk.Button(marco,text="Borrar")
    btn_Borrar.grid(column=4,row=10,padx=5,pady=5)
    datos.bind("<ButtonRelease-1>")
    ventana.mainloop()

if __name__ == "__main__":
    main()