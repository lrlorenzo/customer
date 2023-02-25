import customer_dao
from database import engine


def add_vehicles(vehicles):
    with engine.begin() as conn:
        for v in vehicles:
            vehicle_dao.add_vehicle(conn, v)
