from flask_wtf import FlaskForm 
from wtforms import validators, ValidationError  
from wtforms import IntegerField, TextAreaField, SubmitField, RadioField, SelectField  
  
class GetChoice(FlaskForm):     
   option = SelectField('Black Owned', choices = [('Restaurants', 'Restaurants'),('Barber Shops', 'Barbershops'),('Clothing Stores','Clothing Stores'),('Hair Salons', 'Hair Salons'),('Banks', 'Banks'), ('Coffee Shops', 'Coffee Shops'), ('Healthcare','Healthcare')])  
   submit = SubmitField("Submit")
