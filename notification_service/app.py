# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/notify', methods=['POST'])
def send_notification():
    classification = request.json.get('classification')
    response_message = "Pothole detected!" if classification == "Pothole" else "No pothole detected."

    return jsonify({"message": response_message}), 200

# Add this to each service's app.py
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200
    
if __name__ == '__main__':
    app.run(port=5003)
