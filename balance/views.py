from flask import render_template

from . import app, RUTA
from .models import DBManager


@app.route('/')
def home():
    db = DBManager(RUTA)
    sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
    movimientos = db.consultaSQL(sql)

    return render_template('inicio.html', movs=movimientos)

# - Función borrar
# - Operar con la BD
# - Poner un botón de borrado en cada movimiento
# - Plantilla con el resultado


@app.route('/borrar')
def eliminar():
    return render_template('borrado.html', resultado=False)
