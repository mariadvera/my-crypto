
from datetime import date

import csv
import sqlite3

RUTA_FICHERO = 'mycrypto/data/movimientos.csv'
RUTA_DB = 'mycrypto/data/mycrypto.db'


class DBManager:

    """
    Clase para interactuar con la base de datos.
    """
    def __init__(self, ruta):
        self.ruta = ruta

    def consultarSQL(self, consulta):
      #1. conectar a la base de datos
      conexion = sqlite3.connect(self.ruta)

      #2. Abrir cursor
      cursor = conexion.cursor()

      #3. Ejecutar la consulta
      cursor.execute(consulta)

      #4. Tratar los datos
      # 4.1 Obtener los datos 
      datos = cursor.fetchall()

      # 4.2 guardar los datos localmente    
    

      #5 cerrar la conexion
      conexion.close()

      #6. Devolver el resultado
    #  return self.registros
      return datos
    
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
        return f'{self.fecha} | {self.hora} | {self.moneda_origen} | {self.cantidad_origen}|  {self.moneda_destino} | {self.cantidad_destino}  | {self.precio_unitario}'

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
        db = DBManager(RUTA_DB)
        sql = 'SELECT id, fecha, hora, moneda_origen, cantidad_origen, moneda_destino, cantidad destino, precio_unitario FROM  movimientos'
        datos = db.consultarSQL(sql)

        self.movimientos = []
        for dato in datos:
            mov_dict = {
                'fecha': dato[1],
                'hora': dato[2],
                'moneda_origen': dato[3],
                'cantidad_origen':dato[4],
                'moneda_destino': dato[5],
                'cantidad_destino':dato[6],
                'precio_unitario': dato[7]
            }
            mov = Movimiento(mov_dict)
            self.movimientos.append(mov)
    

class  ListaMovimientosCsv(ListaMovimientos):
    def __init__(self):
        super().__init__()
     

    def cargar_movimientos(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(fila)
                self.movimientos.append(movimiento)

    



       

