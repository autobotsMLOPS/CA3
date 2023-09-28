from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)


def add(var1: int, var2: int):
    """Function to Add"""
    return var1 + var2


def sub(var1: int, var2: int):
    """Function to Substract"""
    return var1 - var2


def mul(var1: int, var2: int):
    """Function to Multiple"""
    return var1 * var2


def div(var1: int, var2: int):
    """Function to Divide"""
    if var2 == 0:
        raise ValueError('Cannot divide by zero')

    return var1 / var2


def modu(var1: int, var2: int):
    """Function to get modulus"""
    if var2 == 0:
        raise ValueError('Cannot divide by zero')

    return var1 % var2


def square_root(var1: float):
    """Function to calculate the square root"""
    if var1 < 0:
        raise ValueError('Cannot calculate square root of a negative number')

    return math.sqrt(var1)

def power(var1: float, var2: float):
    """Function to calculate the power"""
    return var1 ** var2

def factorial(var1: int):
    """Function to calculate the factorial"""
    if var1 < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    if var1 == 0:
        return 1
    return var1 * factorial(var1 - 1)

calculations = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div,
    'modu': modu,
    'sqrt': square_root,
    'pow': power,
    'fact': factorial
}
# render_template('index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate/<operation>/<num1>/<num2>', methods=['GET'])
@app.route('/calculate/<operation>/<num1>', methods=['GET'])
def calculate(operation, num1, num2=None):
    try:
        num1 = float(num1)
        if num2:
            num2 = float(num2)
            
        result = calculations[operation](num1, num2) if num2 else calculations[operation](num1)
        
        return jsonify({'result': result})

    except (ValueError, ZeroDivisionError):
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)