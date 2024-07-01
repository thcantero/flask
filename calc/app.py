from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

"""Basic operations"""

@app.route('/add')
def do_add():
    """Add a + b parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def do_sub():
    """Substract a - b param"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def do_mult():
    """Multiply a and b param"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def do_div():
    """Divide a by b param"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)

###Further Study

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
    }

@app.route('/math/<op>')
def do_math(op):
    'Do operation with a & b'

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(operations[op](a,b))
    