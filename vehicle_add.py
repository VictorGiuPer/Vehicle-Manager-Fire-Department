"""
Module to add a new vehicle to the fleet.

Functions:
    - vehicle_add: Interactively adds a new vehicle to the fleet ensuring unique license plates.
"""

# Import the necessary classes and functions
from vehicle_class import Vehicle


# Define the function to add a new vehicle to the fleet
def vehicle_add(vehicle_list):
    # Prompt the user for the license plate of the new vehicle
    license_new = str(input("What is the license plate of the new vehicle?: "))

    while True:
        # Initialize a flag to check for duplicate license plates
        duplicate_found = False

        # Check if a vehicle with the entered license plate already exists
        for vehicle in vehicle_list:
            if vehicle.license_p == license_new:
                print("A vehicle with this license plate already exists.")
                license_new = str(
                    input("What is the license plate of the new vehicle?: ")
                )
                duplicate_found = True
                break

        # If no duplicate license plate is found, gather additional details about the new vehicle
        if not duplicate_found:
            purpose_new = str(input("What is the purpose of the vehicle?: "))
            passengers_new = int(input("How many passengers does the vehicle carry?: "))

            # Calculate the total weight of the vehicle including passengers
            weight_new = float(input("What is the weight [t] of the vehicle?: "))
            weight_new = round(
                float(weight_new) + (float(passengers_new * 80) * 0.001), 3
            )
            fuel_new = float(input("How much fuel does the vehicle carry?: "))

            # Create a new Vehicle object with the gathered details
            new_vehicle = Vehicle(
                license_new,
                purpose_new,
                passengers_new,
                weight_new,
                fuel_new,
            )

            # Append the new vehicle to the list of vehicles
            vehicle_list.append(new_vehicle)

            # Save the details of the new vehicle to the file
            with open("vehicle_list.txt", "a") as file:
                file.write(repr(new_vehicle) + "\n")
                file.close()

            print("Vehicle added successfully")
            break
