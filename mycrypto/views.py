from flask import render_template
from .forms import PurchaseForm
from .models import ListaMovimientosDB
from .forms import *
from . import app





@app.route('/')
def index():     
    return render_template('inicio.html')

  
  

@app.route('/purchase')
def purchase():       
   form= PurchaseForm() 
   return render_template('purchase.html', form=form)


@app.route('/status')
def status():
    resumen= None
    try:
        lista = ListaMovimientosDB()
        resumen = lista.calcular_resumen()
    except Exception as ex:
        print(f"Error al calcular el resumen: {ex}")
    return render_template('status.html', resumen=resumen)
