
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return (f"The car brand is {self.__brand}. And the car model is {self.model}")
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")
print(my_electric_car.full_name())
print(my_electric_car.fuel_type())


my_car = Car("Tata", "Safari")
print(my_car.full_name())
print(my_car.fuel_type())