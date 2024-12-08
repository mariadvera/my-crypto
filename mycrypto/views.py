from flask import render_template, request

from mycrypto.models import ListaMovimientos, ListaMovimientosDB,  ListaMovimientosCsv

from . import app


@app.route('/')
def home():
    """
    Muestra las  compras en cryptomonedas y las conversiones  realizadas por el usuario     
    """   
    lista = ListaMovimientosDB
    return render_template('home.html', movs = lista.movimientos )


@app.route('/purchase', methods=['GET','POST'])
def purchase():
    """
    Permite realizar compras o  conversiones entre cryptos
    """
    if request.method =='GET':       
      return render_template('purchase.html')
    
    if request.method == 'POST':
        return  request.form
        
   



@app.route('/status')
def status():
    """
    Muestra el estado de la insversión: los euros gastados en 
    compras cryptos y el valor actual total  en euros de  las cryptomonedas 
    que existan en stock del usuario.
    """

    return render_template('status.html')
