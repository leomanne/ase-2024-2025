from flask import Flask, request, make_response, jsonify
import random
import json
import os
import operator

app = Flask(__name__)

LAST_OPERATION_FILE = "last_operation.txt"

def save_last_operation(op, args, result):
    with open(LAST_OPERATION_FILE, 'w') as f:
        f.write(f"{op}({args})={result}")

def load_last_operation():
    if os.path.exists(LAST_OPERATION_FILE):
        with open(LAST_OPERATION_FILE, 'r') as f:
            return f.read()
    return None

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        result = a + b
        save_last_operation("add", f"{a},{b}", result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        result = a - b
        save_last_operation("sub", f"{a},{b}", result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        result = a * b
        save_last_operation("mul", f"{a},{b}", result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if b == 0:
            return make_response('Division by zero\n', 400)
        result = a / b
        save_last_operation("div", f"{a},{b}", result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if b == 0:
            return make_response('Division by zero\n', 400)
        result = a % b
        save_last_operation("mod", f"{a},{b}", result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/upper')
def upper():
    a = request.args.get('a', type=str)
    if a is not None:
        result = a.upper()
        save_last_operation("upper", a, result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/lower')
def lower():
    a = request.args.get('a', type=str)
    if a is not None:
        result = a.lower()
        save_last_operation("lower", a, result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/concat')
def concat():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    if a is not None and b is not None:
        result = a + b
        save_last_operation("concat", f"{a},{b}", result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/reduce')
def reduce():
    op = request.args.get('op', type=str)
    lst = request.args.get('lst', type=str)
    try:
        numbers = json.loads(lst)
        if not isinstance(numbers, list) or any(not isinstance(x, (int, float)) for x in numbers):
            return make_response('Invalid list\n', 400)
    except (json.JSONDecodeError, TypeError):
        return make_response('Invalid list format\n', 400)

    operations = {
        'add': sum,
        'sub': lambda x: x[0] - sum(x[1:]),
        'mul': lambda x: operator.prod(x),
        'div': lambda x: x[0] / operator.prod(x[1:]) if all(x[1:]) else None,
        'concat': lambda x: ''.join(map(str, x))
    }

    if op not in operations:
        return make_response('Invalid operation\n', 400)

    result = operations[op](numbers)
    if result is None:
        return make_response('Division by zero\n', 400)
    
    save_last_operation("reduce", f"{op},{lst}", result)
    return make_response(jsonify(result=result), 200)

@app.route('/random')
def random_number():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if a > b:
            return make_response('Invalid range\n', 400)
        result = random.uniform(a, b)
        save_last_operation("random", f"{a},{b}", result)
        return make_response(jsonify(result=result), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/crash')
def crash():
    host = request.host
    result = {"host": host}
    save_last_operation("crash", "", result)
    make_response(jsonify(result=result), 200)
    os._exit(1)

@app.route('/last')
def last():
    last_op = load_last_operation()
    if last_op:
        return make_response(last_op, 200)
    else:
        return make_response('No operations performed\n', 404)

if __name__ == '__main__':
    app.run(debug=True)
