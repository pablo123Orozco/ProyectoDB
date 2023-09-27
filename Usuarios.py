import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from conexionDB import conectar_db

# Definir las variables globales
name = None
contra = None
rol = None
txtMensaje = None
datos = None
comboRol = None
def consultaU():
    conn = conectar_db()
    cursor = conn.cursor()
    
    # Modifica la consulta SQL para unir las tablas Usuario y Rol
    cursor.execute("SELECT u.idUsuario, u.NombreUsuario, u.Contraseña, r.NombreRol FROM Usuario u "
                   "JOIN Usuario_Rol ur ON u.idUsuario = ur.Usuario_idUsuario "
                   "JOIN Rol r ON ur.Rol_idRol = r.idRol")
    
    usuarios = cursor.fetchall()
    for row in datos.get_children():
        datos.delete(row)

    # Mostrar los datos en el Treeview
    for usuario in usuarios:
        datos.insert('', 'end', values=usuario)

    # Cerrar la conexión a la base de datos
    conn.close()

def obtener_roles():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT NombreRol FROM Rol")
    roles = [row[0] for row in cursor.fetchall()]
    conn.close()
    return roles

    global name, contra, comboRol, id_usuario_actualizar  # Añade id_usuario_actualizar como global
    id_usuario_actualizar = None  # Inicializa id_usuario_actualizar en None
    
    nombre_usuario = name.get()
    contraseña = contra.get()
    
    # Obtener el rol seleccionado del Combobox
    rol_seleccionado = comboRol.get()
    
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        
        # Comprobar si el rol seleccionado existe en la base de datos
        cursor.execute("SELECT idRol FROM Rol WHERE NombreRol = %s", (rol_seleccionado,))
        result = cursor.fetchone()
        
        if result:
            id_rol = result[0]
            
            # Insertar el nuevo usuario en la tabla Usuario
            cursor.execute("INSERT INTO Usuario (NombreUsuario, Contraseña) VALUES (%s, %s)", (nombre_usuario, contraseña))
            
            # Obtener el ID del usuario recién insertado
            cursor.execute("SELECT LAST_INSERT_ID()")
            id_usuario = cursor.fetchone()[0]
            
            # Insertar la relación entre usuario y rol en la tabla Usuario_Rol
            cursor.execute("INSERT INTO Usuario_Rol (Usuario_idUsuario, Rol_idRol) VALUES (%s, %s)", (id_usuario, id_rol))
            
            # Confirmar los cambios en la base de datos
            conn.commit()
            
            # Cerrar la conexión a la base de datos
            conn.close()
            
            txtMensaje.config(text="Usuario guardado con éxito", fg="green")
            consultaU()  # Actualizar la lista de usuarios en el Treeview
            
            # Limpiar los campos de entrada después de guardar
            name.set("")
            contra.set("")
            comboRol.set("")
        else:
            txtMensaje.config(text="El rol seleccionado no existe en la base de datos", fg="red")
    except Exception as e:
        txtMensaje.config(text=f"Error al guardar usuario: {str(e)}", fg="red")

def guardar_usuario():
    global name, contra, comboRol, id_usuario_actualizar  # Añade id_usuario_actualizar como global
    id_usuario_actualizar = None  # Inicializa id_usuario_actualizar en None
    
    nombre_usuario = name.get()
    contraseña = contra.get()
    
    # Obtener el rol seleccionado del Combobox
    rol_seleccionado = comboRol.get()
    
    try:
        # Validar la longitud de la contraseña
        if len(contraseña) < 8:
            txtMensaje.config(text="La contraseña debe tener al menos 8 caracteres", fg="red")
            return  # Detener el proceso si la contraseña no cumple con la longitud mínima
        
        conn = conectar_db()
        cursor = conn.cursor()
        
        # Comprobar si el rol seleccionado existe en la base de datos
        cursor.execute("SELECT idRol FROM Rol WHERE NombreRol = %s", (rol_seleccionado,))
        result = cursor.fetchone()
        
        if result:
            id_rol = result[0]
            
            # Insertar el nuevo usuario en la tabla Usuario
            cursor.execute("INSERT INTO Usuario (NombreUsuario, Contraseña) VALUES (%s, %s)", (nombre_usuario, contraseña))
            
            # Obtener el ID del usuario recién insertado
            cursor.execute("SELECT LAST_INSERT_ID()")
            id_usuario = cursor.fetchone()[0]
            
            # Insertar la relación entre usuario y rol en la tabla Usuario_Rol
            cursor.execute("INSERT INTO Usuario_Rol (Usuario_idUsuario, Rol_idRol) VALUES (%s, %s)", (id_usuario, id_rol))
            
            # Confirmar los cambios en la base de datos
            conn.commit()
            
            # Cerrar la conexión a la base de datos
            conn.close()
            
            txtMensaje.config(text="Usuario guardado con éxito", fg="green")
            consultaU()  # Actualizar la lista de usuarios en el Treeview
            
            # Limpiar los campos de entrada después de guardar
            name.set("")
            contra.set("")
            comboRol.set("")
        else:
            txtMensaje.config(text="El rol seleccionado no existe en la base de datos", fg="red")
    except Exception as e:
        txtMensaje.config(text=f"Error al guardar usuario: {str(e)}", fg="red")

def eliminar_usuario():
    try:
        conn = conectar_db()
        cursor = conn.cursor()

        # Obtener el elemento seleccionado en el Treeview
        item = datos.selection()[0]  # El [0] obtiene el primer elemento seleccionado

        # Obtener el ID del usuario seleccionado
        id_usuario = datos.item(item, 'values')[0]

        # Eliminar la relación entre usuario y rol en la tabla Usuario_Rol
        cursor.execute("DELETE FROM Usuario_Rol WHERE Usuario_idUsuario = %s", (id_usuario,))

        # Luego, eliminar el usuario de la tabla Usuario
        cursor.execute("DELETE FROM Usuario WHERE idUsuario = %s", (id_usuario,))

        # Confirmar los cambios en la base de datos
        conn.commit()

        # Cerrar la conexión a la base de datos
        conn.close()

        txtMensaje.config(text="Usuario eliminado con éxito", fg="green")
        consultaU()  # Actualizar la lista de usuarios en el Treeview
        name.set("")
        contra.set("")
        comboRol.set("")
    except Exception as e:
        txtMensaje.config(text=f"Error al eliminar usuario: {str(e)}", fg="red")

def mostrar_detalle_usuario(event):
    global id_usuario_actualizar
    
    item = datos.selection()[0]  # El [0] obtiene el primer elemento seleccionado

    # Obtener los valores de las columnas para el usuario seleccionado
    valores = datos.item(item, 'values')
    
    # Asignar los valores a los campos correspondientes
    id_usuario_actualizar = valores[0]  # ID del Usuario
    name.set(valores[1])  # Nombre de Usuario
    contra.set(valores[2])  # Contraseña
    comboRol.set(valores[3])  # Rol
    textname.config(state="normal")
    textcontra.config(state="normal")

def actualizar_usuario():
    global id_usuario_actualizar
    try:
        conn = conectar_db()
        cursor = conn.cursor()

        # Obtener los nuevos valores de los campos de entrada
        nuevo_nombre = name.get()
        nueva_contrasena = contra.get()
        nuevo_rol = comboRol.get()

        # Actualizar los datos del usuario en la base de datos
        cursor.execute("UPDATE Usuario SET NombreUsuario = %s, Contraseña = %s WHERE idUsuario = %s",
                       (nuevo_nombre, nueva_contrasena, id_usuario_actualizar))
        
        # Obtener el ID del nuevo rol seleccionado
        cursor.execute("SELECT idRol FROM Rol WHERE NombreRol = %s", (nuevo_rol,))
        nuevo_id_rol = cursor.fetchone()[0]

        # Actualizar el rol del usuario en la tabla Usuario_Rol
        cursor.execute("UPDATE Usuario_Rol SET Rol_idRol = %s WHERE Usuario_idUsuario = %s",
                       (nuevo_id_rol, id_usuario_actualizar))
        
        # Confirmar los cambios en la base de datos
        conn.commit()

        # Cerrar la conexión a la base de datos
        conn.close()

        txtMensaje.config(text="Usuario actualizado con éxito", fg="green")
        consultaU()  # Actualizar la lista de usuarios en el Treeview
        name.set("")
        contra.set("")
        comboRol.set("")
    except Exception as e:
        txtMensaje.config(text=f"Error al actualizar usuario: {str(e)}", fg="red")


def main1():
    global name, contra, txtMensaje, datos, comboRol,textname,textcontra  # Declarar como globales
    ventana = tk.Tk()
    ventana.title("Usuarios")
    ventana.geometry("1300x850")

    name = tk.StringVar()
    contra = tk.StringVar()
    comboRol = tk.StringVar()
    marco = tk.LabelFrame(ventana)
    marco.place(x=350, y=50, width=600, height=500)

    lblname = tk.Label(marco, text="Nombre de Usuario")
    lblname.grid(column=0, row=0, padx=5, pady=5)
    textname = tk.Entry(marco, textvariable=name)
    textname.grid(column=1, row=0)

    lblcontra = tk.Label(marco, text="Contraseña")
    lblcontra.grid(column=0, row=1, padx=5, pady=5)
    textcontra = tk.Entry(marco, textvariable=contra,show="*")
    textcontra.grid(column=1, row=1)

    lista_Rol = obtener_roles()
    lblRol = tk.Label(marco, text="Rol")
    lblRol.grid(column=3, row=0, padx=5, pady=5)
    comboRol = Combobox(marco, values=lista_Rol, textvariable=comboRol)
    comboRol.grid(column=4, row=0)

    txtMensaje = tk.Label(marco, text="Texto de prueba", fg="green")
    txtMensaje.grid(column=1, row=3, columnspan=2)
    
    datos = Treeview(marco)
    datos.grid(column=1, row=4, columnspan=5)
    datos["columns"] = ("ID", "Usuario", "Contraseña", "Rol")
    datos.column("#0", width=0, stretch=tk.NO)
    datos.column("ID", width=90, stretch=False)
    datos.column("Usuario", width=80, stretch=False)
    datos.column("Contraseña", width=80, stretch=False)
    datos.column("Rol", width=100, stretch=False)
    datos.heading("ID", text="ID", anchor=tk.CENTER)
    datos.heading("Usuario", text="Usuario", anchor=tk.CENTER)
    datos.heading("Contraseña", text="Contraseña", anchor=tk.CENTER)
    datos.heading("Rol", text="Rol", anchor=tk.CENTER)

    btnEliminar = tk.Button(marco, text="Eliminar",command=eliminar_usuario)  
    btnEliminar.grid(column=1, row=7)  
    btnActualizar = tk.Button(marco, text="Actualizar",command=actualizar_usuario)
    btnActualizar.grid(column=2, row=7)
    btnGuardar = tk.Button(marco, text="Guardar", command=guardar_usuario)
    btnGuardar.grid(column=3, row=7)
    btnConsultar = tk.Button(marco, text="Consultar Usuarios", command=consultaU)
    btnConsultar.grid(column=4, row=7)
    datos.bind("<ButtonRelease-1>", mostrar_detalle_usuario)

    ventana.mainloop()

if __name__ == "__main__":
    main1()