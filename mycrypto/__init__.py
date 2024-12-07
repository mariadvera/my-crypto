import os

from flask import Flask

RUTA_FICHERO = os.path.join('mycrypto' ,'data', 'movimientos.csv')

app = Flask(__name__)
print('El nombre de la app Flask es: ', __name__)