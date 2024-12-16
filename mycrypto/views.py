from flask import render_template

from .models import ListaMovimientosDB,Movimiento

from . import app


@app.route('/')
def home():    
    return render_template('inicio.html' )

