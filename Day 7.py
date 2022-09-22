def drive():
    print("The car is moving.")


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def update_fuel_level(self, new_level):
        """Update the fuel level."""
        if 0 <= new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")

    def add_fuel(self, amount):
        if self.fuel_level + amount <= self.fuel_capacity:
            self.fuel_level += amount
            print("Added fuel.")
            print(f"Your fuel level now is {self.fuel_level} Litre")
        else:
            print("The tank won't hold that much.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery_size = 75
        self.charge_level = 0
        self.battery = Battery()

    def charge(self):
        self.charge_level = 100
        print("The vehicle is fully charged.")

    def fill_tank(self):
        """Display an error message."""
        print("This car has no fuel tank!")


class Battery:
    def __init__(self, size=75):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 75:
            return 260

        elif self.size == 100:
            return 315


my_car = Car('audi', 'a4', 2016)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.fill_tank()
drive()
print(my_car.fuel_level)
my_car.fuel_level = 150
print(my_car.fuel_level)
my_car.fuel_level = 5
my_car.add_fuel(6)
my_car.add_fuel(2)
my_car.add_fuel(-2)
my_car.add_fuel(15)

tesla1 = ElectricCar("Tesla", "A5", 2020)
print(tesla1.model)

tesla1.fill_tank()
my_car.fill_tank()

my_ecar = ElectricCar('tesla', 'model x', 2019)
my_ecar.charge()
print(my_ecar.battery.get_range())
drive()
