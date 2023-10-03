from datetime import date
from .models import DBManager
from flask import render_template, request

from . import app, RUTA
from .forms import MovimientoForm


@app.route('/')
def home():
    db = DBManager(RUTA)
    sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
    movimientos = db.consultaSQL(sql)

    return render_template('inicio.html', movs=movimientos)


@app.route('/borrar/<int:id>')
def eliminar(id):
    db = DBManager(RUTA)
    ha_ido_bien = db.borrar(id)
    return render_template('borrado.html', resultado=ha_ido_bien)


@app.route('/editar/<int:id>')
def actualizar(id):
    if request.method == 'GET':
        movimiento = {
            'id': 55,
            'fecha': date.fromisoformat('2023-10-03'),
            'concepto': 'Curso de formularios en Python',
            'tipo': 'I',
            'cantidad': 55.95
        }
        formulario = MovimientoForm(data=movimiento)
        return render_template('form_movimiento.html', form=formulario)
    return f'TODO: tratar el método POST para actualizar el movimiento {id}'
