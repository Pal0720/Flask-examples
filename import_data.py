import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+mysqlconnector://root:Mozart&bach3@localhost/airlines')
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("airline_data.csv") as f:
        reader = csv.reader(f)
        for origin, destination, duration in reader:
            db.execute("INSERT INTO flights(origin, destination, duration) VALUES (:origin, :destination, :duration)", #colon:placeholder
            {"origin":origin,"destination":destination, "duration":duration})
            print(f"Added flight from {origin} to {destination} lasting {duration} minutes")
        db.commit()

if __name__ == "__main__":
    main()
