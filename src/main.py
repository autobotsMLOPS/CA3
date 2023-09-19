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


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        choice = data['choice']
        input1 = data['input1']
        input2 = data['input2']

        if choice == 1:
            result = add(input1, input2)
        elif choice == 2:
            result = sub(input1, input2)
        elif choice == 3:
            result = mul(input1, input2)
        elif choice == 4:
            result = div(input1, input2)
        elif choice == 5:
            result = modu(input1, input2)
        else:
            return jsonify({'error': 'Invalid choice'}), 400

        return jsonify({'result': result})

    except (ValueError, KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
