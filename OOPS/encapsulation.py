# __ in front of the attribute name, makes it private


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return (f"The car brand is {self.__brand}. And the car model is {self.model}")
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")
print(my_electric_car.full_name())
print(my_electric_car.get_brand())