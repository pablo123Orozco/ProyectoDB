import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from conexionDB import conectar_db

Proveedor=None

def obtenerProveedor():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Empresa FROM Proveedor")
    proveedor = [row[0] for row in cursor.fetchall()]
    conn.close()
    return proveedor

def main():

    ventana = tk.Tk()
    ventana.title("Productos")
    ventana.geometry("1300x850")
    marco = tk.LabelFrame(ventana)
    marco.place(x=350, y=50, width=750, height=650)

    global nombre, precio,cantidad,proveedores,txtnombre,txtCantidad,txtPrecio,Proveedor
    nombre =tk.StringVar()
    precio =tk.StringVar()
    cantidad =tk.StringVar()
    proveedores = tk.StringVar()

    lblnombre = tk.Label(marco, text="Nobre")
    lblnombre.grid(column=0, row=0, padx=5, pady=5)
    txtnombre = tk.Entry(marco,textvariable=nombre)
    txtnombre.grid(column=1,row=0)

    lblPrecio = tk.Label(marco, text="Precio")
    lblPrecio.grid(column=2, row=0, padx=5, pady=5)
    txtPrecio = tk.Entry(marco,textvariable=precio)
    txtPrecio.grid(column=3,row=0)

    lblCantidad = tk.Label(marco, text="Cantidad")
    lblCantidad.grid(column=0, row=1, padx=5, pady=5)
    txtCantidad=tk.Entry(marco,textvariable=cantidad)
    txtCantidad.grid(column=1, row=1)

    listaProveedor = obtenerProveedor()
    lblProveedor = tk.Label(marco, text="Proveedor")
    lblProveedor.grid(column=2, row=1, padx=5, pady=5)
    Proveedor = Combobox(marco, values=listaProveedor, textvariable=proveedores)
    Proveedor.grid(column=3, row=1)
    

    global datos  
    datos = Treeview(marco)
    datos.grid(column=1, row=8, columnspan=5)
    datos["columns"] = ("ID", "Nombre", "Precio","Cantidad","Proveedor")
    datos.column("#0", width=0, stretch=tk.NO)
    datos.column("ID", width=90, stretch=False)
    datos.column("Nombre", width=80, stretch=False)
    datos.column("Precio", width=80, stretch=False)
    datos.column("Cantidad", width=100, stretch=False)
    datos.column("Proveedor", width=100, stretch=False)
    datos.heading("ID", text="ID", anchor=tk.CENTER)
    datos.heading("Nombre", text="Nombre", anchor=tk.CENTER)
    datos.heading("Precio", text="Precio", anchor=tk.CENTER)
    datos.heading("Cantidad", text="Cantidad", anchor=tk.CENTER)
    datos.heading("Proveedor", text="Proveedor", anchor=tk.CENTER)
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