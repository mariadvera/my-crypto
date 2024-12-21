# forms.py
from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from config import MONEDAS


class PurchaseForm(FlaskForm):
    def __init__(self, ):
       
        
        self.from_currency.choices = MONEDAS
        self.to_currency.choices = MONEDAS

    from_currency = SelectField('Moneda Origen', validators=[DataRequired()])
    to_currency = SelectField('Moneda Destino', validators=[DataRequired()])
    from_amount = DecimalField('Cantidad Moneda Origen', validators=[
                               DataRequired(), NumberRange(min=0)])
    unit_price = DecimalField('Precio Unitario', render_kw={"readonly": True})
    to_amount = DecimalField('Cantidad Moneda Destino',
                             render_kw={"readonly": True})
    simulate = SubmitField('Simular')
    confirm = SubmitField('Confirmar')
    

  
