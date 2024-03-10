"""
Module for displaying an overview of the vehicle fleet.

Functions:
    - vehicle_overview: Displays a list of all vehicles, sorted by their driving range.
"""


# Import necessary functions from the vehicle_load_data module
from vehicle_load_data import vehicle_load_data

# Define a list of uppercase alphabets to be used for displaying vehicle options
alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


# Define the function to provide an overview of the vehicles
def vehicle_overview(a):
    # Use the provided alphabet list (or default to the one above if not provided)
    alphabet = a

    # Load the vehicle data from the file
    vehicle_list = vehicle_load_data()

    # Sort the vehicle list based on range (__lt__)
    vehicle_list.sort()

    # Display each vehicle's details with an associated alphabet option for selection
    for vehicle, letter in zip(vehicle_list, alphabet):
        # Convert the vehicle object to string format for display
        vehicle_str = repr(vehicle).replace("Vehicle(", "").replace(")", "")

        # Print the vehicle details in the desired format
        print("\n[" + letter + "] " + vehicle_str.replace(",", " | "))
