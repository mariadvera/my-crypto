
from datetime import date

import sqlite3

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

        #  guardar los datos localmente    
        

        # cerrar la conexion
        conexion.close()  

        # devolver los datos   
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
        db = DBManager(app.config['RUTADB'])
        sql = 'SELECT  id, fecha, hora, moneda_origen, cantidad_origen ,  moneda_destino ,  cantidad_destino  , precio_unitario  FROM   movimientos'   
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

           

    

