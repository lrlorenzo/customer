from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import joinedload

from customer import Customer, Name, Vehicle
from sqlalchemy import text, create_engine, MetaData, Table, Column, BigInteger, Integer, String, Date, ForeignKey, \
    select

from customer_exception import CustomerException

metadata_obj = MetaData()

customer = Table(
    "customer",
    metadata_obj,
    Column("id", BigInteger, primary_key=True),
    Column("last_name", String(50), nullable=False),
    Column("first_name", String(50), nullable=False),
    Column("birthdate", Date(), nullable=False),
    Column("phone_number", String(15))
)

customer_vehicle = Table(
    "customer_vehicle",
    metadata_obj,
    Column("customer_id", BigInteger, ForeignKey("customer.id"), primary_key=True),
    Column("vehicle_id", BigInteger, ForeignKey("vehicle.id"), primary_key=True)
)

vehicle = Table(
    "vehicle",
    metadata_obj,
    Column("id", BigInteger, primary_key=True),
    Column("brand", String(50), nullable=False),
    Column("year", Integer, nullable=False),
    Column("plate_number", String(15))
)


def create_customer(conn, c):
    stmt = customer.insert().values(last_name=c.name.last_name, first_name=c.name.first_name,
                                    birthdate=c.birthdate, phone_number=c.phone_number)
    result = conn.execute(stmt)
    return result.inserted_primary_key[0]


def create_vehicle(conn, v):
    stmt = vehicle.insert().values(brand=v.brand, year=v.year, plate_number=v.plate_number)
    result = conn.execute(stmt)
    return result.inserted_primary_key[0]


def create_customer_vehicle(conn, cv):
    stmt = customer_vehicle.insert().values(customer_id=cv.customer_id, vehicle_id=cv.vehicle_id)
    conn.execute(stmt)


def find(conn, customer_id):
    stmt = select(customer.c.last_name, customer.c.first_name, customer.c.birthdate, customer.c.phone_number,
                  vehicle.c.brand, vehicle.c.year, vehicle.c.plate_number,
                  customer_vehicle.c.customer_id, customer_vehicle.c.vehicle_id).\
        select_from(customer_vehicle.join(customer).join(vehicle)).\
        where(customer.c.id == customer_id)

    result = conn.execute(stmt)

    print(result)
    if result.rowcount == 0:
        raise NoResultFound(f"No user found with id={customer_id}")

    vehicle_list = []
    for i, r in enumerate(result):
        if i == 0:
            print(r)
            name = Name(r.last_name, r.first_name)
            birthdate = r.birthdate
            phone_number = r.phone_number
            customer_id = r.customer_id

        v = Vehicle(r.brand, r.year, r.plate_number, r.vehicle_id)
        vehicle_list.append(v)

    return Customer(name, birthdate, phone_number, vehicle_list, customer_id)


# TODO group by customer
def find_all(conn):
    stmt = select(customer.c.last_name, customer.c.first_name, customer.c.birthdate, customer.c.phone_number,
                  vehicle.c.brand, vehicle.c.year, vehicle.c.plate_number,
                  customer_vehicle.c.customer_id, customer_vehicle.c.vehicle_id).\
        select_from(customer_vehicle.join(customer).join(vehicle))

    result = conn.execute(stmt)

    vehicle_list = []
    for i, r in enumerate(result):
        if i == 0:
            print(r)
            name = Name(r.last_name, r.first_name)
            birthdate = r.birthdate
            phone_number = r.phone_number
            customer_id = r.customer_id

        v = Vehicle(r.brand, r.year, r.plate_number, r.vehicle_id)
        vehicle_list.append(v)

    return Customer(name, birthdate, phone_number, vehicle_list, customer_id)
