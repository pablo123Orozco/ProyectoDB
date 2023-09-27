import tkinter as tk
from tkinter import messagebox
import mysqlx
from Cliente import main
from conexionDB import conectar_db
from Pantalla_Principal import usuario

def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = conectar_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM usuario WHERE NombreUsuario = %s AND Contraseña = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
hanmachi
            if user:
                messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
                root.withdraw()  # Oculta la ventana de inicio de sesión

                if username == "Admin":
                    usuario()
                else:
                    main()

            else:
                messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

            cursor.close()
            conn.close()
        except mysqlx.connector.Error as e:
            messagebox.showerror("Error", f"Error de conexión a la base de datos: {str(e)}")

# Crear la ventana de inicio de sesión
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("1300x850")

# Crear campos de entrada
username_label = tk.Label(root, text="Nombre de usuario:")
username_label.pack()
username_label.place(x=800, y=200)
username_entry = tk.Entry(root)
username_entry.pack()
username_entry.place(x=800, y=240)

password_label = tk.Label(root, text="Contraseña:")
password_label.pack()
password_label.place(x=800, y=300)
password_entry = tk.Entry(root, show="*")  # La contraseña se muestra como asteriscos
password_entry.pack()
password_entry.place(x=800, y=340)

# Botón de inicio de sesión
login_button = tk.Button(root, text="Iniciar Sesión", command=login)
login_button.pack()
login_button.place(x=800, y=400)
root.mainloop()
