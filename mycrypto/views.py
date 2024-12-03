from . import  app

@app.route('/') 
def home():    
    """
    Muestra las  compras en cryptomonedas y las conversiones  realizadas por el usuario 
    """
    return 'lista de transcacciones'


@app.route('/purchase')
def purchase():
   """
   Permite realizar compras o  conversiones entre cryptos
   """ 
   return 'Agregar nueva transacción'


@app.route('/status')
def status():
    """
    Muestra el estado de la insversión: los euros gastados en 
    compras cryptos y el valor actual total  en euros de  las cryptomonedas 
    que existan en stock del usuario.
    """

    return 'Estado de la inversión'