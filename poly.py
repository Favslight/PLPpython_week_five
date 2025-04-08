# Base class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle is moving...")  # Default behavior


# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying through the sky.")


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("🚢 The boat is sailing across the sea.")


# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("🚲 The bicycle is pedaling along the path.")


# Function to demonstrate polymorphism
def vehicle_movement_demo(vehicles):
    for v in vehicles:
        v.move()


# Create a list of vehicle objects
fleet = [Car(), Plane(), Boat(), Bicycle()]

vehicle_movement_demo(fleet)