from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    vin: str
    brand: str
    model: str
    year: int
    color: str
    price: float
    mileage: int

@dataclass(frozen=True)
class MaintenanceRecord:
    record_id: int
    date: str
    service_type: str
    cost: float
    car: Car

@dataclass(frozen=True)
class Dealership:
    name: str
    address: str
    contact_info: str
