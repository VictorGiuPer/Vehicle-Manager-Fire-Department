# DOCSTRING:
"""
Module for the Vehicle class representation and related tests.

Classes:
    Vehicle: A representation of a vehicle in the fire department's fleet.

Functions:
    - test_fuel_level: Checks fuel level functionality.
    - test_weight: Validates weight handling.
    - test_range: Tests range calculation.
    - test_repr: Confirms the __repr__ method.
    - test_copy: Validates the __copy__ method.
"""

# Import necessary libraries
import random


# Constructor to initialize the attributes of the Vehicle classe
class Vehicle:
    def __init__(
        self,
        license_p,
        purpose,
        passengers,
        weight,
        fuel_level,
    ):
        self.license_p = str(license_p)  # Unique identifier for the vehicle
        self.purpose = str(purpose)  # Purpose of the vehicle (e.g., ladder, engine)
        self.passengers = int(passengers)  # Number of passengers in the vehicle
        self.fuel_level = float(fuel_level)  # Amount of fuel in the vehicle in liters
        self.weight = weight  # Weight of the vehicle in tons

        self.range = round(
            20 * (self.fuel_level / self.weight)
        )  # Calculate the range based on the formula provided in the assignment

    # Getter and setter for the attributes
    @property
    def License_P(self):
        return self.license_p

    @License_P.setter
    def License_P(self, value):
        self.license_p = value

    @property
    def Purpose(self):
        return self.purpose

    @Purpose.setter
    def Purpose(self, value):
        self._purpose = value

    @property
    def Passengers(self):
        return self.passengers

    @Passengers.setter
    def Passengers(self, value):
        self._passengers = value

    @property
    def Weight(self):
        return self.weight

    @Weight.setter
    def Weight(self, value):
        # ensuring correct values
        if value <= 0:
            raise ValueError("Weight must be positive.")
        elif value > 100:
            raise ValueError("Weight can't exceed 100 tons.")
        else:
            self.weight = value
            self.recalculate_range()

    @property
    def Fuel_Level(self):
        return self.fuel_level

    @Fuel_Level.setter
    def Fuel_Level(self, value):
        # ensuring correct values
        if value < 0:
            raise ValueError("Fuel level must be positive (or zero).")
        elif value > 500:
            raise ValueError("Fuel level can't exceed 500 liters.")
        else:
            self.fuel_level = value
            self.recalculate_range()

    @property
    def Range(self):
        return self.range

    @Range.setter
    def Range(self, value):
        # ensuring correct values
        if value < 0:
            raise ValueError("Range must be positive (or zero).")
        elif value > 1500:
            raise ValueError("Range can't exceed 1500 kilometers.")
        else:
            self.range = value

    # Method to recalculate the range of the vehicle based on current attributes
    def recalculate_range(self):
        self.range = round(20 * (self.fuel_level / self.weight))

    # Represent the Vehicle object as a string for saving and reloading purposes
    def __repr__(self):
        return f'Vehicle("{self.license_p}", "{self.purpose}", {self.passengers}, {self.weight}, {self.fuel_level}, {self.range})'

    # Define the "less than" comparison method for sorting vehicles by range
    def __lt__(self, other):
        try:
            return self.range > other.range
        except AttributeError:
            return NotImplemented

    # Method to create a copy of the Vehicle object
    def __copy__(self):
        vehicle_copy = Vehicle(
            str(self.license_p) + "_copy",
            self.purpose,
            self.passengers,
            self.weight,
            self.fuel_level,
        )
        return vehicle_copy

    # Generate 10 randomized vehicles
    @classmethod
    def create(cls):
        def random_license_plate():
            return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))

        test_vehicles = [
            Vehicle(
                license_p=random_license_plate(),
                purpose=random.choice(["Ladder", "Engine", "Command"]),
                passengers=random.randint(4, 6),
                weight=random.randint(4, 8),
                fuel_level=random.randint(60, 90),
            )
            for _ in range(10)
        ]

        return test_vehicles

    # Test setters of weight, fuel level and range
    def test_weight(test_vehicles):
        for vehicle in test_vehicles:
            # ARRANGE
            original_weight = vehicle.Weight
            original_range = vehicle.Range
            #    print(
            #       f"Original weight: {original_weight}, Original range: {original_range}"
            #  )

            # ACT
            added_weight = 15
            vehicle._weight = original_weight + added_weight

            # ASSERT
            expected_range = round(20 * (vehicle.Fuel_Level / vehicle.Weight))
            if vehicle.Range != expected_range:
                print(
                    f"Test failed for weight. Expected range {expected_range}, but got {vehicle.Range}"
                )
                return False
            elif vehicle.Range == expected_range:
                print(
                    f"Test passed. Expected range {expected_range}, got {vehicle.Range}"
                )

        return True

    def test_fuel_level(test_vehicles):
        for vehicle in test_vehicles:
            # ARRANGE
            original_fuel_level = vehicle.Fuel_Level
            original_range = vehicle.Range
            #    print(
            #       f"Original fuel level: {original_fuel_level}, Original range: {original_range}"
            #  )

            # ACT
            added_fuel = 15
            vehicle._fuel_level = original_fuel_level + added_fuel

            # ASSERT
            expected_range = round(20 * (vehicle.Fuel_Level / vehicle.Weight))
            if vehicle.Range != expected_range:
                print(
                    f"Test failed for fuel level. Expected range {expected_range}, but got {vehicle.Range}"
                )
                return False
            elif vehicle.Range == expected_range:
                print(
                    f"Test passed. Expected range {expected_range}, got {vehicle.Range}"
                )

        return True

    def test_range(test_vehicles):
        for vehicle in test_vehicles:
            # ARRANGE
            original_range = vehicle.Range

            # ACT: Direct modification of the range
            new_range = original_range
            vehicle.range = new_range

            # ASSERT
            if vehicle.Range != new_range:
                print(
                    f"Test failed for range. Expected {new_range}, but got {vehicle.Range}"
                )
                return False
            elif vehicle.Range == new_range:
                print(f"Test passed. Expected range {new_range}, got {vehicle.Range}")
        return True

    def test_errors():
        # Create your test vehicles
        test_vehicles = Vehicle.create()

        # Introduce deliberate error for range in one of the vehicles
        test_vehicles[0].range = -10  # setting an incorrect range value
        assert not Vehicle.test_range(
            test_vehicles
        ), "Range test failed to catch error!"

        # Re-create the vehicles to reset them
        test_vehicles = Vehicle.create()

        # Introduce deliberate error for fuel_level in one of the vehicles
        test_vehicles[1].fuel_level = -20  # setting an out-of-bounds fuel level
        assert not Vehicle.test_fuel_level(
            test_vehicles
        ), "Fuel level test failed to catch error!"

        # Re-create the vehicles to reset them
        test_vehicles = Vehicle.create()

        # Introduce deliberate error for weight in one of the vehicles
        test_vehicles[2].weight = -30  # setting an out-of-bounds weight
        assert not Vehicle.test_weight(
            test_vehicles
        ), "Weight test failed to catch error!"

        print("All error tests passed!")


"""     def test_repr(test_vehicles):
        for vehicle in test_vehicles:
            # ARRANGE
            original_range = vehicle.Range

            # ACT: serialize and deserialize using __repr__
            for vehicle in test_vehicles:
                vehicle_repr = repr(vehicle)
                vehicle_from_repr = eval(str(vehicle_repr[:-1]) + ")")

                # Compare the attributes
                if (
                    vehicle.fuel_level == vehicle_from_repr.fuel_level
                    and vehicle.weight == vehicle_from_repr.weight
                    and vehicle.range == vehicle_from_repr.range
                ):
                    continue
                else:
                    print(f"Test failed for __repr__ for vehicle {vehicle.license_p}.")
                    return False
        return True """

"""     def test_copy(test_vehicles):
        for vehicle in test_vehicles:
            # ARRANGE
            original_range = vehicle.Range

            # ACT: create a copy of the vehicle
            vehicle_copy = vehicle.__copy__()

            # ASSERT
            if vehicle_copy.Range != original_range:
                print(
                    f"Test failed for __copy__. Expected range {original_range}, but got {vehicle_copy.Range}"
                )
                return False

        return True
 """
