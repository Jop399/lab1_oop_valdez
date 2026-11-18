lass Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


# Create three car objects
car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Mitsubishi", "Mirage", 2021)

# Display car information
print("Car 1:")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Year:", car1.year)
print("Wheels:", car1.wheels)

print("\nCar 2:")
print("Brand:", car2.brand)
print("Model:", car2.model)
print("Year:", car2.year)
print("Wheels:", car2.wheels)

print("\nCar 3:")
print("Brand:", car3.brand)
print("Model:", car3.model)
print("Year:", car3.year)
print("Wheels:", car3.wheels)
