import unittest
from entities.car import Car
from service import can_customer_afford_car, is_car_sold, is_service_date_valid, is_vin_unique

class TestServiceRules(unittest.TestCase):
    def test_can_customer_afford_car(self):
        self.assertTrue(can_customer_afford_car(30000, 25000))
        self.assertFalse(can_customer_afford_car(20000, 25000))

    def test_is_car_sold(self):
        car = Car("1HGCM82633A123456", "Honda", "Accord", 2020, "Black", 25000, 10000)
        contracts = []
        self.assertFalse(is_car_sold(car, contracts))
        contracts.append(SalesContract(1, "2024-11-25", 25000, car, None, None))
        self.assertTrue(is_car_sold(car, contracts))

    def test_is_service_date_valid(self):
        self.assertTrue(is_service_date_valid("2024-11-30", "2024-11-25"))
        self.assertFalse(is_service_date_valid("2024-11-20", "2024-11-25"))

    def test_is_vin_unique(self):
        car1 = Car("1HGCM82633A123456", "Honda", "Accord", 2020, "Black", 25000, 10000)
        car2 = Car("2HGCM82633A654321", "Toyota", "Corolla", 2021, "White", 22000, 5000)
        existing_cars = [car1]
        self.assertTrue(is_vin_unique(car2, existing_cars))
        self.assertFalse(is_vin_unique(car1, existing_cars))

if __name__ == "__main__":
    unittest.main()
