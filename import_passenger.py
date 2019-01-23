import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

engine = create_engine("mysql+mysqlconnector://pal0720:Mozart&bach3@localhost/airlines")
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("passengers.csv") as f:
        reader = csv.reader(f)
        for passenger_id,passenger,flight_id in reader:
            db.execute("INSERT INTO passengers(passenger_id,passenger,flight_id) VALUES(:passenger_id,:passenger,:flight_id)",
            {'passenger_id':passenger_id,'passenger':passenger,'flight_id':flight_id})
            print(f"Added {passenger} with id {passenger_id} on flight no {flight_id}")

    db.commit()


if __name__ == '__main__':
        main()
