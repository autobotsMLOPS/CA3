from flask import Flask, request, jsonify
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

@app.route('/calculate/sqrt/<num1>', methods=['GET'])
def calculate_square_root(num1):
    try:
        num1 = float(num1)
        result = square_root(num1)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input data'}), 400

@app.route('/calculate/fact/<num1>', methods=['GET'])
def calculate_factorial(num1):
    try:
        num1 = int(num1)
        result = factorial(num1)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input data'}), 400

@app.route('/calculate/<operation>/<num1>/<num2>', methods=['GET'])
def calculate(operation, num1, num2=None):
    try:
        num1 = float(num1)
        if num2 is not None:
            num2 = float(num2)

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'sub':
            result = sub(num1, num2)
        elif operation == 'mul':
            result = mul(num1, num2)
        elif operation == 'div':
            result = div(num1, num2)
        elif operation == 'modu':
            result = modu(num1, num2)
        elif operation == 'pow':
            result = power(num1, num2)
        else:
            return jsonify({'error': 'Invalid choice'}), 400

        return jsonify({'result': result})

    except (ValueError, ZeroDivisionError):
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)