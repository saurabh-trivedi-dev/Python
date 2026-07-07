class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return (f"The car brand is {self.brand}. And the car model is {self.model}")

my_car = Car("Tata", "Safari")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())