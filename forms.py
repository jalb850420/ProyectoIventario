from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class TipoUsuario(FlaskForm):
    codigo = StringField('Tipo de Usuario', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    enviar = SubmitField('Agregar Tipo de Usuario')

class Producto(FlaskForm):
    id = StringField('Id Producto', validators=[DataRequired("Tienes que introducir el dato")])
    enviar = SubmitField('Ver Producto')