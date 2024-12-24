from fastapi import FastAPI, HTTPException
from schemas import *
from models import *

app = FastAPI()

@app.post("/flight")
def flight_add(data:Flight_validation):
    db = session()
    new_flight = Flight(space_count=data.space_count,from_city=data.from_city, to_city=data.to_city)
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    db.close()
    return new_flight

@app.get('/flights')
def update_flight(flight_id=int,flight__date=Flight_validation):
    db = session()
    flight = db.query(Flight).filter(Flight.id ==flight_id).first()
    if not flight:
        return HTTPException(status_code=404,detail="Flight not found")
    if flight.space_count:
        flight.space_count = flight__date.space_count
    if flight.from_city:
        flight.from_city = flight__date.from_city
    if flight.to_city:
        flight.to_city = flight__date.to_city
    db.commit()
    db.close()
    return flight


@app.put('/flights')
def update_flight(flight_id:int,flight_date:Flight_validation):
    db = session()
    flight = db.query(Flight).filter(Flight.id ==flight_id).first()
    if not flight:
        return HTTPException(status_code=404, detail="Flight not found")
    new_flight = Flight(space_count = flight_date.space_count,from_city=flight_date.from_city, to_city=flight_date.to_city)
    db.commit()
    db.close()
    return new_flight
        
@app.delete("/flight")
def delete_flights(fligth_id:int):
    db = session()
    fligth = db.query(Flight).filter(Flight.id == fligth_id).first()
    if not fligth:
        return HTTPException(status_code=404, detail="Flight not found")
    db.delete(fligth)
    db.close()
    return {"detail": "Flight deleted"}