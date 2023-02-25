import customer_dao
from database import engine
from customer import CustomerVehicle


def add_customer(customer):
    with engine.begin() as conn:
        customer_id = customer_dao.create_customer(conn, customer)
        for v in customer.vehicles:
            vehicle_id = customer_dao.create_vehicle(conn, v)
            cv = CustomerVehicle(customer_id, vehicle_id)
            customer_dao.create_customer_vehicle(conn, cv)


def find_all():
    with engine.begin() as conn:
        customer = customer_dao.find_all(conn)
        return customer


def find(customer_id):
    with engine.begin() as conn:
        customer = customer_dao.find(conn, customer_id)
        return customer
