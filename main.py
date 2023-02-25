from flask import Flask, jsonify
from customer_controller import customer_controller
from vehicle_controller import vehicle_controller

app = Flask(__name__)
app.register_blueprint(customer_controller, url_prefix='/customer_api')
app.register_blueprint(vehicle_controller, url_prefix='/customer_api')

if __name__ == '__main__':
    app.run(port=5001, debug=True)

