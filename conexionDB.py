import mysql.connector

def conectar_db():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='pablo',
            host='localhost',
            database='Jugueteriadb',
            port='3307'
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error de conexión a la base de datos: {str(e)}")
        return None
    
    