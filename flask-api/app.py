from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    name = data.get('name', 'User')
    result = {'message': f'Hello from Python, {name}!'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)  # Runs on localhost:5000
