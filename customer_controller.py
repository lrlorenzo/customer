from flask import Blueprint, Flask, request, jsonify, make_response
from sqlalchemy.exc import NoResultFound

from customer import Name, Customer, Vehicle
import customer_service
from customer_exception import CustomerException

app = Flask(__name__)
customer_controller = Blueprint('customer_controller', __name__)


@customer_controller.route('/customers/', methods=['GET'])
def find_all():
    try:
        customer = customer_service.find_all()
        return make_response(jsonify(customer.to_dict()), 200)
    except CustomerException as e:
        return make_response(jsonify(str(e)), 500)


@customer_controller.route('/customers/<int:customer_id>', methods=['GET'])
def find_customer(customer_id):
    try:
        customer = customer_service.find(customer_id)
        return make_response(jsonify(customer.to_dict()), 200)
    except NoResultFound as e:
        return make_response(jsonify(str(e)), 404)
    except CustomerException as e:
        return make_response(jsonify(str(e)), 500)


@customer_controller.route('/customers', methods=['POST'])
def add_customer():
    try:
        last_name = request.json['last_name']
        first_name = request.json['first_name']
        birthdate = request.json['birthdate']
        phone_number = request.json['phone_number']
        name = Name(last_name, first_name)
        vehicles = request.json['vehicles']
        vehicle_list = []
        for v in vehicles:
            brand = v['brand']
            year = v['year']
            plate_number = v['plate_number']
            vehicle = Vehicle(brand, year, plate_number)
            vehicle_list.append(vehicle)
        customer = Customer(name, birthdate, phone_number, vehicle_list)
        customer_service.add_customer(customer)
        response = {
            'message': 'Customer Successfully Created',
        }
        return make_response(jsonify(response), 201)

    except:
        error_response = {
            'error': 'Application error occurred',
            'status': 500
        }
        return make_response(jsonify(error_response), 500)
