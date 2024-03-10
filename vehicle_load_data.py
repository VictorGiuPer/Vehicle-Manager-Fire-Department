"""
Module to load vehicle data from a file.

Functions:
    - vehicle_load_data: Loads the list of vehicles from a file or creates default vehicles if the file doesn't exist.
"""

# Import necessary classes and functions from the vehicle_class module
from vehicle_class import Vehicle


# Define the function to load vehicle data from the file
def vehicle_load_data():
    try:
        # Attempt to open the file that contains the list of vehicles
        with open("vehicle_list.txt", "r") as f:
            vehicle_list = []

            # Iterate over each line in the file
            for line in f:
                # Remove the last entry (assuming there's no comma in the attributes)
                stripped_line = line.rsplit(",", 1)[0] + ")"

                # Convert the line from the file into a Vehicle object
                vehicle_obj = eval(stripped_line)

                # Add the created vehicle object to the vehicle list
                vehicle_list.append(vehicle_obj)

    # Handle the case where the file does not exist
    except FileNotFoundError:
        # Create a new file and add some default vehicles to it
        with open("vehicle_list.txt", "w") as f:
            vehicle1 = Vehicle("X00", "Command", 4, 2, 60)
            vehicle2 = Vehicle("0X0", "Engine", 4, 10, 100)
            vehicle3 = Vehicle("00X", "Ladder", 4, 12, 120)
            vehicle_list = []
            vehicle_list.append(vehicle1)
            vehicle_list.append(vehicle2)
            vehicle_list.append(vehicle3)

            # Write the default vehicles to the file
            for vehicle in vehicle_list:
                f.write(repr(vehicle) + "\n")

            f.close()

    # Return the list of vehicles loaded from the file (or the default list if the file didn't exist)
    return vehicle_list
