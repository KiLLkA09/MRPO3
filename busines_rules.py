def can_customer_afford_car(customer_budget, car_price):
    return customer_budget >= car_price

def is_car_sold(car, sales_contracts):
    return any(contract.car.vin == car.vin for contract in sales_contracts)

def is_service_date_valid(service_date, current_date):
    return service_date >= current_date

def is_vin_unique(car, existing_cars):
    return all(existing_car.vin != car.vin for existing_car in existing_cars)
