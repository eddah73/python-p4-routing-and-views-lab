#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"


@app.route ('/print/<string:param>')
def print_string(param = 'hello'):
    print (param)
    return f'{param}'

@app.route ('/count/<int:param>')
def count(param):
      return '\n'.join(str(i) for i in range(param)) + '\n'


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is undefined"
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Modulus of zero is undefined"
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
