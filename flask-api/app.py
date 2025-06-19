from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    name = data.get('name', 'User')
    return jsonify({'message': f'Hello from Python, {name}!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
