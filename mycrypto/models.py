
from datetime import  date

import requests

import sqlite3

from config import API_KEY, BASE_URL

from . import app





class DBManager:

    """
    Clase para interactuar con la base de datos.
    """
    def __init__(self, ruta):
        self.ruta = ruta

    def consultarSQL(self, consulta):
        # conectar a la base de datos
        conexion = sqlite3.connect(self.ruta)

        # Abrir cursor
        cursor = conexion.cursor()

        # Ejecutar la consulta
        cursor.execute(consulta)
    
        #  Obtener los datos 
        datos = cursor.fetchall()

        self.registros = []
        nombres_columna = []

        for columna in cursor.description:
            nombres_columna.append(columna[0])

        #  guardar los datos localmente 
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columna:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.registros.append(movimiento)

        

        # cerrar la conexion
        conexion.close()  

        # devolver resultado
        return self.registros
     
    
class Movimiento:

    def __init__(self, dict_mov):
        self.errores = []
        
        fecha = dict_mov.get('fecha', '')
        hora = dict_mov.get('hora', '')
        moneda_origen = dict_mov.get('moneda_origen','')
        cantidad_origen = dict_mov.get('cantidad_origen', 0)
        moneda_destino = dict_mov.get('moneda_destino','')
        cantidad_destino = dict_mov.get('cantidad_destino','')
        precio_unitario = dict_mov.get('precio_unitario','')
        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            mensaje = f'La fecha {fecha} no es una fecha ISO 8601 válida'
            self.errores.append(mensaje)
        except TypeError:
            self.fecha = None
            mensaje = f'La fecha {fecha} no es una cadena'
            self.errores.append(mensaje)
        except:
            self.fecha = None
            mensaje = f'Error desconocido con la fecha'
            self.errores.append(mensaje)

        self.hora = hora
        self.moneda_origen = moneda_origen
        self.cantidad_origen = cantidad_origen
        self.moneda_destino = moneda_destino
        self.cantidad_destino = cantidad_destino
        self.precio_unitario = precio_unitario

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha} | {self.hora} | {self.moneda_origen} |  {self.moneda_destino} | {self.cantidad_origen} | {self.cantidad_destino} |  {self.precio_unitario}'

    def __repr__(self):
        return self.__str__()
      


class ListaMovimientos:
    def __init__(self):
        try:
            self.cargar_movimientos()
        except:
            self.movimientos = []
    

    def guardar(self):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def agregar(self, movimiento):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos')

    def cargar_movimientos(self):
        raise NotImplementedError(
            'Debes usar una clase concreta de ListaMovimientos') 
    

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result
      
    def __repr__(self):
        return self.__str__()
    
class ListaMovimientosDB(ListaMovimientos):
  
    
    def cargar_movimientos(self):
        db = DBManager(app.config['RUTADB'])
        sql = 'SELECT * FROM movimientos'   
        datos = db.consultarSQL(sql)

        self.movimientos = []
        for dato in datos:
            mov_dict = {
                'fecha':dato[1],
                'hora':dato[2],
                'moneda_origen':dato[3],
                'cantidad_origen':dato[4],
                'moneda_destino':dato[5],
                'cantidad_destino':dato[6],
                'precio_unitario':dato[7]
            }
            mov = Movimiento(mov_dict)
            self.movimientos.append(mov)

           

    def calcular_resumen(self):        
        """
        Euros invertidos: La cantidad total de euros gastados en transacciones de compra de criptomonedas.
        Saldo en euros: La diferencia entre las compras de criptomonedas con euros y las ventas de criptomonedas a cambio de euros.
        Valor actual de las criptomonedas: La cantidad total de cada criptomoneda en posesión convertida a euros según la tasa de cambio actual.
        Valor actual total: La suma de euros invertidos, el saldo en euros, y el valor de las criptomonedas.
        """
        movimientos = self.movimientos

        total_invertido = 0
        saldo_euros = 0
        valores_cripto = {}

        for mov in movimientos:
            moneda_origen = mov[3]
            cantidad_origen = mov[4]
            moneda_destino = mov[5]
            cantidad_destino = mov[6]

            # Calcular euros invertidos
            if moneda_origen == 'EUR':
                total_invertido += cantidad_origen
                saldo_euros -= cantidad_origen
            elif moneda_destino == 'EUR':
                saldo_euros += cantidad_destino

            # Calcular cantidad de criptos
            if moneda_destino != 'EUR':
                valores_cripto[moneda_destino] = valores_cripto.get(moneda_destino, 0) + cantidad_destino
            if moneda_origen != 'EUR':
                valores_cripto[moneda_origen] = valores_cripto.get(moneda_origen, 0) - cantidad_origen

        # Obtener valor actual en euros de cada cripto
        valor_actual_euros = 0
        for cripto, cantidad in valores_cripto.items():
            if cantidad > 0:
                response = requests.get(f"{BASE_URL}/{cripto}/EUR", headers={"X-CoinAPI-Key": API_KEY})
                if response.status_code == 200:
                    rate = response.json().get('rate', 0)
                    valor_actual_euros += cantidad * rate

        return {
            'invertido': total_invertido,
            'saldo_euros': saldo_euros,
            'valor_criptos': valor_actual_euros,
            'valor_actual': total_invertido + saldo_euros + valor_actual_euros
        }

