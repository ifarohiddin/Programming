from pydantic import BaseModel

class Flight(BaseModel):
    flight_number: str
    from_city : str
    to_city : str
    plane_id: int
    data_time: datatime

class Plane(BaseModel):
    model: str
    space_bus: int
    space_eco: int

class Ticket(BaseModel) :
    pasanger_id: int
    flight_id: int
    price: int
    class_type: int

class passanger(BaseModel):
    fullname: str
    passport_id: str 
    phone_number: int
    birth_date: data  
    emain: EmailStr

class Order(BaseModel):
    ticket_id:int 
    amount:int

class User(BaseModel):
    login:str
    password:str