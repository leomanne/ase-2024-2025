from flask import Flask, request, make_response, jsonify
import random

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return make_response(jsonify(result=a + b), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return make_response(jsonify(result=a - b), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return make_response(jsonify(result=a * b), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if b == 0:
            return make_response('Division by zero\n', 400)
        return make_response(jsonify(result=a / b), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if b == 0:
            return make_response('Division by zero\n', 400)
        return make_response(jsonify(result=a % b), 200)
    else:
        return make_response('Invalid input\n', 400)

@app.route('/random')
def random_number():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if a > b:
            return make_response('Invalid range\n', 400)
        return make_response(jsonify(result=random.uniform(a, b)), 200)
    else:
        return make_response('Invalid input\n', 400)

if __name__ == '__main__':
    app.run(debug=True)
