from flask import Blueprint, Flask, request, jsonify, make_response

import vehicle_service


app = Flask(__name__)
vehicle_controller = Blueprint('vehicle_controller', __name__)


@vehicle_controller.route('/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify({'message': 'All Employees'})


@vehicle_controller.route('/vehicles', methods=['POST'])
def add_vehicles():
    try:
        vehicles = request.json['vehicles']
        vehicle_list = []
        for v in vehicles:
            brand = v['brand']
            year = v['year']
            plate_number = v['plate_number']
            customer_id = v['customer_id']
            vehicle = Vehicle(brand, year, plate_number, customer_id)
            vehicle_list.append(vehicle)
        vehicle_service.add_vehicles(vehicle_list)
        return {'message': 'success'}

    except:
        error_response = {
            'error': 'Application error occurred',
            'status': 500
        }
        return make_response(jsonify(error_response), 500)
