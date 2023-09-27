import mysql.connector

def conectar_db():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='pablo',
            host='127.0.0.1',
            database='Jugueteriadb',
            port='3306'
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error de conexión a la base de datos: {str(e)}")
        return None