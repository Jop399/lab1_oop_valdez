
class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.km_driven = 0

    # Part 3: Drive method
    def drive(self, km):
        if km > 0:
            self.km_driven += km
            print(self.brand, "drove", km, "km.")
        else:
            print("Invalid distance!")

    # Part 3: Age method
    def age(self, current_year):
        return current_year - self.year

    # Part 3: String method
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


# Create three car objects (Part 2)
car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Mitsubishi", "Mirage", 2021)


# Display car information
print("Car 1:", car1)
print("Wheels:", car1.wheels)

print("Car 2:", car2)
print("Wheels:", car2.wheels)

print("Car 3:", car3)
print("Wheels:", car3.wheels)


# Test Part 3 methods
car1.drive(50)
car2.drive(100)
car3.drive(30)

print("Car age:", car1.age(2026), "years")
print("Kilometers driven:", car1.km_driven)
