from flask import Flask, jsonify, request

from .services import retrieve_computer_orders, create_computer_order

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello World!'})

@app.route('/health')
def health():
    return jsonify({'message': 'OK'})

@app.route('/api/orders/computers', methods=['POST'])
def create_computer_order():
    response = create_computer_order(request.get_json())
    return response

@app.route('/api/orders/computers', methods=['GET'])
def get_computer_order():
    response = retrieve_computer_orders()
    return response


if __name__ == '__main__':
    app.run(debug=True)