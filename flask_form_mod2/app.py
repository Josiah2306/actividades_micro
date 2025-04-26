from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

class RegistrationForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=3)])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrarse')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('register.html', form=form)

@app.route('/')
def home():
    return redirect('/register')

@app.route('/success')
def success():
    return 'Registro exitoso!'

if __name__ == '__main__':
    app.run(debug=True)

