from flask import Flask, request, jsonify

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


@app.route('/calculate/<int:operation>/<num1>/<num2>', methods=['GET'])
def calculate(operation, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 1:
            result = add(num1, num2)
        elif operation == 2:
            result = sub(num1, num2)
        elif operation == 3:
            result = mul(num1, num2)
        elif operation == 4:
            result = div(num1, num2)
        elif operation == 5:
            result = modu(num1, num2)
        else:
            return jsonify({'error': 'Invalid choice'}), 400

        return jsonify({'result': result})

    except (ValueError, ZeroDivisionError):
        return jsonify({'error': 'Invalid input data'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
