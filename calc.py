#!/usr/bin/env python3

from flask import Flask, render_template, request
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def start_page():
    return render_template("index.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    def add(first_number, second_number):
        return first_number + second_number

    def minus(first_number, second_number):
        return first_number - second_number

    def multiply(first_number, second_number):
        return first_number * second_number

    def divide(first_number, second_number):
        return first_number / second_number
    
    operations = {
        "+": add,
        "-": minus,
        "*": multiply,
        "/": divide
    }

    form = request.form
    first_number = form['first_number']
    operator = form['operator']
    second_number = form['second_number']

    try:
        result = operations[operator](Decimal(first_number), Decimal(second_number))
        result_printed = "{0} {1} {2} = {3}".format(first_number, operator,\
                                                    second_number, result)
    except Exception:
        result_printed = "Oops. Something went wrong. Please try again"
    return render_template('result-page.html', result = result_printed)
