from datetime import date
import sqlite3
"""
SELECT id, fecha, concepto, tipo, cantidad FROM movimientos
"""


class DBManager:

    def __init__(self, ruta):
        self.ruta = ruta

    def conectar(self):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        return (conexion, cursor)

    def desconectar(self, conexion):
        conexion.close()

    def consultaSQL(self, consulta):

        # 1. Conectar a BD
        conexion = sqlite3.connect(self.ruta)

        # 2. Abrir cursor
        cursor = conexion.cursor()

        # 3. Ejecutar consulta
        cursor.execute(consulta)

        # 4. Tratar los datos
        # 4.1. Obtener datos
        datos = cursor.fetchall()

        # 4.2. Guardarlos localmente
        self.registros = []
        nombres_columna = []
        for columna in cursor.description:
            nombres_columna.append(columna[0])

        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columna:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.registros.append(movimiento)

        # 5. Cerrar conexión
        conexion.close()

        # 6. Devolver resultados

        return self.registros

    def borrar(self, id):
        """
        DELETE FROM movimientos WHERE id=?
        """
        sql = 'DELETE FROM movimientos WHERE id=?'
        conexion, cursor = self.conectar()

        resultado = False

        try:
            cursor.execute(sql, (id,))
            conexion.commit()
            resultado = True
        except:
            conexion.rollback()

        self.desconectar()
        return resultado

    def obtener_movimiento(self, id):
        consulta = 'SELECT id, fecha, concepto, cantidad FROM movimientos WHERE id=?'

        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta, (id,))

        datos = cursor.fetchone()
        resultado = None

        if datos:
            nombres_columna = []
            for columna in cursor.description:
                nombres_columna.append(columna[0])

            movimiento = {}
            indice = 0
            for nombre in nombres_columna:
                movimiento[nombre] = datos[indice]
                indice += 1
            movimiento['fecha'] = date.fromisoformat(movimiento['fecha'])

            resultado = movimiento

        conexion.close()
        return resultado

    def consulta_con_parametros(self, consulta, parametros):
        conexion, cursor = self.conectar()

        resultado = False
        try:
            cursor.execute(consulta, parametros)
            conexion.commit()
            resultado = True
        except:
            conexion.rollback()

        self.desconectar()
        return resultado
