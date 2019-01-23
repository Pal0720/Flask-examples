from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine("mysql+mysqlconnector://pal0720:Mozart&bach3@localhost/airlines")
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT * FROM flights")
    for flight in flights:
        print(f"Origin : {flight.origin}, Destination:{flight.destination}, Duration : {flight.duration}")

if __name__ == "__main__":
    main()
