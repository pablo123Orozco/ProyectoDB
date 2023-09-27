
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from conexionDB import conectar_db

# Declara datos como una variable global
datos = None

def consultaU():
    conn = conectar_db()
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT idProveedor, Nombre, Apellido, Telefono, Direccion, Empresa FROM Proveedor")
    
    proveedores = cursor.fetchall()
    
    # Borrar cualquier dato previo en el Treeview
    for row in datos.get_children():
        datos.delete(row)

    
    for proveedor in proveedores:
        datos.insert('', 'end', values=proveedor)

    
    conn.close()


def insertar_proveedor():
    conn = conectar_db()
    cursor = conn.cursor()
    
    
    nombre_proveedor = nombre.get()
    apellido_proveedor = apellido.get()
    telefono_proveedor = telefono.get()
    direccion_proveedor = direccion.get()
    empresa_proveedor = empresa.get()
    
    
    cursor.execute("INSERT INTO Proveedor (Nombre, Apellido, Telefono, Direccion, Empresa) VALUES (%s, %s, %s, %s, %s)",
                   (nombre_proveedor, apellido_proveedor, telefono_proveedor, direccion_proveedor, empresa_proveedor))
    
    conn.commit()
    
    
    conn.close()

    
    nombre.set('')
    apellido.set('')
    telefono.set('')
    direccion.set('')
    empresa.set('')

    
    consultaU()    

def cargar_datos(event):
    global id_proveedor_seleccionado

    seleccion = datos.selection()
    if seleccion:
        item = seleccion[0]  # Obtener el primer elemento seleccionado

        valores = datos.item(item, 'values')

        id_proveedor_seleccionado = valores[0]  
        nombre.set(valores[1]) 
        apellido.set(valores[2])
        telefono.set(valores[3]) 
        direccion.set(valores[4]) 
        empresa.set(valores[5])  

        
        txtnombre.config(state="normal")
        txtapellido.config(state="normal")
        txttelefono.config(state="normal")
        txtdireccion.config(state="normal")
        txtempresa.config(state="normal")

def actualizar_proveedor():
    global id_proveedor_seleccionado

    if not id_proveedor_seleccionado:
        messagebox.showerror("Error", "Selecciona un proveedor para actualizar.")
        return

    
    nombre_proveedor = nombre.get()
    apellido_proveedor = apellido.get()
    telefono_proveedor = telefono.get()
    direccion_proveedor = direccion.get()
    empresa_proveedor = empresa.get()

    if not nombre_proveedor or not apellido_proveedor:
        messagebox.showerror("Error", "Nombre y Apellido son campos requeridos.")
        return

    try:
        conn = conectar_db()
        cursor = conn.cursor()

        
        cursor.execute("UPDATE Proveedor SET Nombre=%s, Apellido=%s, Telefono=%s, Direccion=%s, Empresa=%s WHERE idProveedor=%s",
                       (nombre_proveedor, apellido_proveedor, telefono_proveedor, direccion_proveedor, empresa_proveedor, id_proveedor_seleccionado))

        conn.commit()
        conn.close()

        messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")

        
        nombre.set('')
        apellido.set('')
        telefono.set('')
        direccion.set('')
        empresa.set('')

        
        consultaU()

        
        txtnombre.config(state="disabled")
        txtapellido.config(state="disabled")
        txttelefono.config(state="disabled")
        txtdireccion.config(state="disabled")
        txtempresa.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar el proveedor: {str(e)}")

def habilitar_campos():
    txtnombre.config(state="normal")
    txtapellido.config(state="normal")
    txttelefono.config(state="normal")
    txtdireccion.config(state="normal")
    txtempresa.config(state="normal")

def eliminar_proveedor():
    global id_proveedor_seleccionado

    if not id_proveedor_seleccionado:
        messagebox.showerror("Error", "Selecciona un proveedor para eliminar.")
        return

    try:
        conn = conectar_db()
        cursor = conn.cursor()

        
        cursor.execute("DELETE FROM Proveedor WHERE idProveedor=%s", (id_proveedor_seleccionado,))

        conn.commit()
        conn.close()

        messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")

        
        nombre.set('')
        apellido.set('')
        telefono.set('')
        direccion.set('')
        empresa.set('')

        
        consultaU()

        
        id_proveedor_seleccionado = None

        
        habilitar_campos()

    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar el proveedor: {str(e)}")
def main():

    ventana = tk.Tk()
    ventana.title("Usuarios")
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
    btn_ver = tk.Button(marco, text="Ver", command=consultaU)
    btn_ver.grid(column=1, row=10, padx=5, pady=5)
    btn_guardar = tk.Button(marco,text="Guardar",command=insertar_proveedor)
    btn_guardar.grid(column=2,row=10,padx=5,pady=5)
    btn_actualizar = tk.Button(marco, text="Actualizar",command=actualizar_proveedor)
    btn_actualizar.grid(column=3,row=10,padx=5,pady=5)
    btn_Borrar = tk.Button(marco,text="Borrar",command=eliminar_proveedor)
    btn_Borrar.grid(column=4,row=10,padx=5,pady=5)
    datos.bind("<ButtonRelease-1>",cargar_datos)
    ventana.mainloop()

if __name__ == "__main__":
    main()