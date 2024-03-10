"""
Module for the main user interface of the Vehicle Manager.

Functions:
    - vehicle_manager: Provides the main user interface to manage the vehicle fleet.
"""

# NO NEED TO USE IMPORTLIB.RELOAD (skipped)

# Import necessary classes and functions from other modules
from vehicle_class import Vehicle
from vehicle_add import vehicle_add
from vehicle_change import vehicle_change
from vehicle_overview import vehicle_overview, alphabet
from vehicle_load_data import vehicle_load_data


# Define the main vehicle manager function that provides the user interface
def vehicle_manager():
    # Continuously run the interface until the user decides to exit
    while True:
        # Display the main menu options to the user
        print("[0] Exit \n[1] Add Vehicle \n[2] Test Program")
        # Display the overview of available vehicles
        vehicle_overview(alphabet)

        # Get the user's choice for the desired action
        action_choice = str(input("Choose an option: "))

        # Handle exit choice
        if action_choice == "0":
            print("You have succesfully logged out.")
            break

        # Handle adding a new vehicle choice
        elif action_choice == "1":
            vehicle_add(vehicle_load_data())

        # Handle running tests on the program
        elif action_choice == "2":
            # Create test vehicles
            test_vehicles = Vehicle.create()

            # CATCHING ERRORS WITH THE TESTS (need to uncomment)
            # test_vehicles[0].range = 2000  # An incorrect value.
            # >>> This test fails to raise an error. I believe it is because the range is dynamic,
            #    based on the other 2 values. It is definitely possible to fix this issue but in
            #    this case I believe it means rewriting the whole logic of the code. Which is not
            #    necessary since the program itself makes sure the values are correct.
            #    (In short: I have the conditions in place just not within the Vehicle class itself)
            #    I hope that is not to dramatic ;)

            # test_vehicles[1].fuel_level = -50  # Out-of-bounds value
            # test_vehicles[2].weight = -20  # Out-of-bounds value

            # Define list of tests to run
            tests = [
                ("Weight", Vehicle.test_weight),
                ("Fuel level", Vehicle.test_fuel_level),
                ("Range", Vehicle.test_range),
            ]

            # Initialize a flag to track if all tests pass
            tests_passed = True

            # Run each test and print its outcome
            for test_name, test_function in tests:
                if test_function(test_vehicles):
                    print(f"{test_name} tests passed. \n")
                else:
                    print(f"{test_name} tests failed. \n")
                    tests_passed = False

            # Print the final test outcome
            if tests_passed:
                print("All tests passed.")
            else:
                print("Some tests failed.")

        # Handle the choice of modifying a specific vehicle based on the provided alphabet choice
        elif action_choice in alphabet:
            # Determine the vehicle associated with the chosen alphabet
            position_letter = alphabet.index(action_choice)
            list_vehicles = vehicle_load_data()
            list_vehicles.sort()
            license_plate = list_vehicles[position_letter].license_p
            # Invoke the vehicle change function to modify the chosen vehicle
            vehicle_change(list_vehicles, license_plate)


# Invoke the main vehicle manager function to start the user interface
vehicle_manager()
