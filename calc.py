#!/usr/bin/env python3

from flask import Flask, render_template, request
from decimal import Decimal

app = Flask(__name__)


@app.route('/')
def start_page():
    return render_template("index.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    
    operations = {
        "+": lambda first_number, second_number: first_number + second_number,
        "-": lambda first_number, second_number: first_number - second_number,
        "*": lambda first_number, second_number: first_number * second_number,
        "/": lambda first_number, second_number: first_number / second_number,
    }
    form = request.form
    first_number = form['first_number']
    operator = form['operator']
    second_number = form['second_number']

    try:
        result = operations[operator](Decimal(first_number), Decimal(second_number))
        return render_template('result.html', form = form, result = result)
    except ArithmeticError:
       error = "InvalidDataNotNumberError"
       return render_template('result.html', error = error)
    except ZeroDivisionError:
        error = "DivisionByZeroError"
        return render_template('result.html', error = error)
    except Exception:
        error = "UnexpectedAndUnknownError"
        return render_template('result.html', error = error)
