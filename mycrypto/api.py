
from datetime import date, datetime
from  .forms import PurchaseForm
from .models import DBManager, ListaMovimientosDB, Movimiento
from flask import   app, flash, jsonify,  redirect, url_for
import requests
from config import API_KEY, BASE_URL


@app.route('/api/v1/movimientos')
def inicio():
    try:
        db = DBManager(app.config['RUTADB'])
        sql = 'SELECT * FROM movimientos'
        movs = db.consultarSQL(sql)
        resultado = {
            'status': 'success',
            'results': movs
        }
        status_code = 200
    except Exception as ex:
        resultado = {
            'status': 'error',
            'message': str(ex)
        }
        status_code = 500

    return jsonify(resultado), status_code    

   
@app.route('/api/v1/calculate', methods=['GET', 'POST'])
def simulatePurchase():
    form = PurchaseForm()
    if form.validate_on_submit():          
        # Simulación
        from_currency = form.from_currency.data
        to_currency = form.to_currency.data
        from_amount = form.from_amount.data

        # Llamada a la API para obtener la tasa de cambio
        response = requests.get(f"{BASE_URL}/{from_currency}/{to_currency}", 
                                headers={"X-CoinAPI-Key": API_KEY})
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data['rate']
            to_amount = from_amount * exchange_rate
            return jsonify({
                'unit_price': round(exchange_rate, 6),
                'to_amount': round(to_amount, 6)
            })
        else:
            return jsonify({'error': 'Error al consultar la API.'}), 500
        

@app.route('/api/v1/purchase', methods=['POST'])
def confirmPurchase():
    form = PurchaseForm()
    if form.validate_on_submit():
        nuevo_movimiento = Movimiento({
            'fecha': date.today().isoformat(),
            'hora': datetime.now().strftime('%H:%M:%S'),
            'moneda_origen': form.from_currency.data,
            'cantidad_origen': form.from_amount.data,
            'moneda_destino': form.to_currency.data,
            'cantidad_destino': form.to_amount.data,
            'precio_unitario': form.unit_price.data
        })
        lista = ListaMovimientosDB()
        lista.agregar(nuevo_movimiento)
        flash("Transacción confirmada.", "success")
        return redirect(url_for('inicio'))

                    
       
    

   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    