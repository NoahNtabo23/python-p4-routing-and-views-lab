#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f"<h2>Printed:{parameter}</h2>"

@app.route('/count/<int:int_param>')
def count(int_param):
    numbers = "<br>".join(str(i) for i in range(1, int_param+1))
    return f"<h1>Counted:</h1>{numbers}"


@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return f"<h1>Result: {result}</h1>"



if __name__ == '__main__':
    app.run(port=5555, debug=True)
