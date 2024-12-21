from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired, NumberRange


from config import MONEDAS


class PurchaseForm(FlaskForm):
    def __init__(self, *args, **kwargs):       
        super().__init__(*args, **kwargs)
        self.from_currency.choices = MONEDAS
        self.to_currency.choices = MONEDAS

    from_currency = SelectField(
        'Moneda Origen',
        choices=[],  
        validators=[DataRequired()]
    )
    to_currency = SelectField(
        'Moneda Destino',
        choices=[],  
        validators=[DataRequired()]
    )
    from_amount = DecimalField('Cantidad Origen', validators=[
                  DataRequired(), NumberRange(min=0.01)])
    unit_price = DecimalField('Precio Unitario')
    to_amount = DecimalField('Cantidad Destino')
    simulate = SubmitField('Simular')
    confirm = SubmitField('Confirmar')



  
