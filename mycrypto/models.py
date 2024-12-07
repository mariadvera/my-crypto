import csv
from datetime import date

from . import RUTA_FICHERO




class Movimiento:
    def __init__(self, fecha, hora, de, q, a, cantidad, precio_unitario):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(fecha)
           
        except ValueError:
            self.fecha = None
            mensaje = f'La fecha {fecha} no es una fecha ISO 8601 válida'
            self.errores.append(mensaje)
           

        self.hora = hora
        self.de = de
        self.q = q
        self.a = a
        self.cantidad= cantidad
        self.precio_unitario= precio_unitario

    @property
    def has_errors(self):
        return len(self.errores) > 0


    def __str__(self):
        return f'{self.fecha} | {self.hora} | {self.de} | {self.q} | {self.a} | {self.cantidad}   | {self.precio_unitario}'

class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)              
            for fila in reader:
                movimiento = Movimiento(
                    fila.get('fecha', None),
                    fila.get('hora', '__'),
                    fila.get('de', 'varios'),
                    fila.get('q', ''),
                    fila.get('a',''),
                    fila.get('cantidad', 0),                    
                    fila.get('precio_unitario','--')
                )
                self.movimientos.append(movimiento) 

    def guardar(self):
        with open(RUTA_FICHERO,  'w') as fichero:
          #  cabeceras = ['fecha', 'hora', 'de,' 'q', 'a', 'cantidad', 'precio_unitario']
          #  writer = csv.writer(fichero)
          #  writer.writerow(cabeceras)
            cabeceras =list(self.movimientos[0].__dict__.keys())
            cabeceras.remove('errores')
            writer = csv.DictWriter(fichero, fieldnames=cabeceras)
            writer.writeheader()

            for mov in self.movimientos:
                mov_dict = mov.__dict__
                mov_dict.pop('errors')
                writer.writerow(mov_dict)

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
            return result
        
   


