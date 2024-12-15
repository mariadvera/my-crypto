from .models import DBManager
from flask import jsonify
from . import app

@app.route('/api/v1/movimientos')
def inicio():
    try:
        db = DBManager(app.config['RUTADB'])
        sql = 'SELECT id, fecha, hora, moneda_origen, cantidad_origen, moneda_destino,  cantidad_destino, precio_unitario FROM movimientos'
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





 
    





