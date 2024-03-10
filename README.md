Fire Department Vehicle Manager by Victor Giustini Perez

~ Description: ~

The Fire Department Vehicle Manager is a Python-based application designed to help the fire department manage its fleet of vehicles. It offers a computerized system that ensures the driving range of vehicles is always clear and accurate, taking into account the weight, fuel level, and other properties of each vehicle.


~ Features: ~

Vehicle Management: Add, modify, or delete vehicles from the fleet.
Unique Call Signs: Ensure that each vehicle has a unique identifier.
Detailed Overview: View a sorted list of all vehicles based on their driving range.
Range Calculation: Automatically calculate and update the driving range of vehicles based on their weight and fuel level.
Persistence: Save vehicle data to a file and load it the next time the program is run.
Testing: Run tests to ensure the accurate calculation of the range and other functionalities.

~ How to Use: ~

Start the Program:

Run main.py to initiate the program. This script serves as the main entry point for the user interface.
Main Menu Options:

Upon starting, the main menu will present you with options to exit the program, add a new vehicle, run tests on the program, or select an existing vehicle to modify.
Adding a New Vehicle:

Choose the option to add a new vehicle. You will need to input details such as the license plate, purpose, passengers, weight, and fuel level. The program ensures that each vehicle has a unique identifier.
Modifying an Existing Vehicle:

The program provides an overview of all vehicles sorted by their driving range. Select a vehicle by choosing the corresponding alphabet letter shown next to the vehicle details.
Once a vehicle is selected, you can modify various attributes such as the license plate, purpose, weight, fuel level, and range. You also have options to delete the vehicle or create a copy of it.
Deleting a Vehicle:

While modifying a vehicle, you can choose to delete it. You will be asked to confirm your decision before the vehicle is permanently removed from the fleet.
Copying a Vehicle:

The option to copy a vehicle allows you to create an exact duplicate of the selected vehicle with a new license plate. This is useful for quickly adding vehicles with similar specifications.
Viewing Vehicles Overview:

At any point, you can view a detailed overview of all vehicles, which includes sorted listings based on their driving range. This feature is part of the main menu and can be accessed directly.
Running Tests:

The program includes a testing feature to validate the accuracy of functionalities such as the calculation of the driving range and the updating of vehicle details. Select the "Test Program" option from the main menu to run these tests.
Exiting the Program:

To exit the program, select the exit option from the main menu. The program will terminate after saving any changes made during the session.
Data Persistence:

Vehicle data is saved to a file, ensuring that all modifications are retained between sessions. The program automatically loads this data upon startup.
Remember, the program assumes specific conditions for fuel consumption rate, maximum weight, fuel level, and range for vehicles, as detailed in your documentation. This guide should provide users with a clear understanding of how to effectively use the Fire Department Vehicle Manager application.

~ Assumptions: ~

The program assumes a fuel consumption rate of 
5 liters / (100km × 1t)

The maximum weight for a vehicle is set to 100 tons.
The maximum fuel level for a vehicle is set to 500 liters.
The maximum range for a vehicle is set to 1000 km.
