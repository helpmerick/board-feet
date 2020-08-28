from flask import Flask, redirect, url_for, request, render_template, flash, session, g
from wtforms import Form, StringField, SubmitField, FloatField, validators
from flask_wtf import FlaskForm
import os

DEBUG = True
app = Flask(__name__)
app.secret_key = os.urandom(24)
project_dir = os.path.abspath(os.path.dirname(__file__))


class ReusableForm(Form):
    LengthVal = FloatField('Length:')
    WidthVal = FloatField('Width:')
    ThickVal = FloatField('Thickness:')
    errors = ('fill in all fields')

    @app.route('/', methods=['POST', 'GET'])
    def CalculateNum(*args, **kwargs):
        form = ReusableForm(request.form)
        print(form.errors)
        if request.method != 'POST':
            global Sum, total
            Sum = []
            total = []

        if request.method == 'POST':
            LengthVal = request.form['LengthVal']
            WidthVal = request.form['WidthVal']
            ThickVal = request.form['ThickVal']
            print(LengthVal, " ", WidthVal, " ", ThickVal, " ")
            if form.validate():
                total = total

                FinalCalc = float(LengthVal) * float(WidthVal) * float(ThickVal) / 144
                FinalCalc = round(FinalCalc, 2)
                total.append(FinalCalc)
                value = sum(total)
                Sum.append(value)

                tol = len(total)

                flash('Board Feet: ' + str(FinalCalc))

                return render_template('boards.html', LengthVal=LengthVal, WidthVal=WidthVal, ThickVal=ThickVal,
                                       sum=total, total=tol, value=value)

            else:
                flash('Error: All form fields required')

        return render_template('boards.html')


if __name__ == '__main__':
    app.run(debug=True)
