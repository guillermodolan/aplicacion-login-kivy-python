import sqlite3

class ProgressDao:
    @classmethod
    def crear_tabla(cls):
        conexion = sqlite3.connect("progressform_database.db")
        cursor = conexion.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuario(name CHAR(30), password CHAR(30), mail CHAR(30), birthdate CHAR(30))")
        conexion.commit()
        conexion.close()

    @classmethod
    def agregar_usuario(cls, nombre, contrasenia, mail, fecha_nacimiento):
        conexion = sqlite3.connect("progressform_database.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuario VALUES(?,?,?,?)", (nombre, contrasenia, mail, fecha_nacimiento))
        filaModificada = cursor.rowcount
        conexion.commit()
        conexion.close()
        return filaModificada

    @classmethod
    def login(cls, name, password):
        conexion = sqlite3.connect("progressform_database.db")
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM usuario WHERE name = ? AND password = ?', (name, password))
        user = cursor.fetchone()
        if user:
            return user

    @classmethod
    def find_user(cls, name):
        conexion = sqlite3.connect("progressform_database.db")
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM usuario WHERE name = ?', (name, ))
        user = cursor.fetchone()
        if user:
            return user

    @classmethod
    def update_usuario(cls, nombre, contrasenia, mail, fecha_nacimiento):
        conexion = sqlite3.connect("progressform_database.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuario SET password = ?, mail = ?, birthdate = ? WHERE name = ?", (contrasenia, mail, fecha_nacimiento, nombre))
        filaModificada = cursor.rowcount
        conexion.commit()
        conexion.close()
        return filaModificada

    @classmethod
    def delete_user(cls, nombre):
        conexion = sqlite3.connect("progressform_database.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuario WHERE name = ?", (nombre, ))
        filaModificada = cursor.rowcount
        conexion.commit()
        conexion.close()
        return filaModificada