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

if __name__ == '__main__':
    add(1,1)
    sub(1,0)
    mul(2,1)
    div(4,2) 
    modu(3,2)
