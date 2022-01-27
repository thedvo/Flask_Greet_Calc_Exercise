# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def _add():
    """Sums inputs"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def _sub():
    """Subtracts inputs"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def _mult():
    """Multiples inputs"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route('/div')
def _div():
    """Divides inputs"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)


# FURTHER STUDY
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route("/math/<operation>")
def _math(operation):
    """Do a math operation on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a, b)

    return str(result)
