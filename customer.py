
class Name:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Customer:
    def __init__(self, name, birthdate, phone_number, vehicles=[], customer_id=0):
        self.name = name
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.vehicles = vehicles
        self.customer_id = customer_id

    def set_vehicles(self, vehicles):
        self.vehicles = vehicles

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'last_name': self.name.last_name,
            'first_name': self.name.first_name,
            'birthdate': self.birthdate,
            'phone_number': self.phone_number,
            'vehicles': [v.to_dict() for v in self.vehicles]
        }


class Vehicle:
    def __init__(self, brand, year, plate_number, vehicle_id=0):
        self.brand = brand
        self.year = year
        self.plate_number = plate_number
        self.vehicle_id = vehicle_id

    def to_dict(self):
        return {
            'vehicle_id': self.vehicle_id,
            'brand': self.brand,
            'year': self.year,
            'plate_number': self.plate_number
        }


class CustomerVehicle:
    def __init__(self, customer_id, vehicle_id):
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'vehicle_id': self.vehicle_id
        }
