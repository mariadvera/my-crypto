

from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

print('***DATOS DE CONFIGURACION***_')
print('SECRET KEY', app.config['SECRET_KEY'])
print('RUTA BD', app.config['RUTADB'])
