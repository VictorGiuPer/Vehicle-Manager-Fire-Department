"""
Module for modifying vehicle attributes and managing vehicle data.

Functions:
    - find_vehicle: Locates a vehicle based on its license plate.
    - delete_vehicle: Removes a specific vehicle from the fleet.
    - copy_vehicle: Creates a copy of a specific vehicle.
    - update_license_p: Modifies the license plate of a vehicle.
    - update_file: Saves the updated vehicle data to a file.
    - vehicle_change: Main function for handling vehicle modifications based on user input.
"""

# Import the necessary modules
import copy


# Function to find a vehicle in the vehicle_list based on its license plate
def find_vehicle(vehicle_list, vehicle_lp):
    for vehicle in vehicle_list:
        if vehicle.license_p == vehicle_lp:
            return vehicle
    return None


# Function to delete a specific vehicle from the vehicle_list
def delete_vehicle(vehicle, vehicle_list):
    confirmation = str(
        input("Are you sure you want to delete this vehicle \nYes [1] | No [2]: ")
    )
    if confirmation == "1":
        vehicle_list.remove(vehicle)
        with open("vehicle_list.txt", "r") as file:
            lines = file.readlines()
        with open("vehicle_list.txt", "w") as file:
            for line in lines:
                if vehicle.license_p not in line:
                    file.write(line)
        file.close()
        print("Vehicle deleted succesfully.")
    else:
        print("Vehicle NOT deleted.")


# Function to create a copy of a specific vehicle and add it to the vehicle_list
def copy_vehicle(vehicle_list, vehicle):
    vehicle_copy = copy.copy(vehicle)
    vehicle_list.append(vehicle_copy)
    with open("vehicle_list.txt", "a") as file:
        file.write(repr(vehicle_copy) + "\n")
        file.close()
    vehicle_change(vehicle_list, vehicle_copy.license_p)
    return vehicle_list


#
#
#


# Function to update the license plate of a specific vehicle
def update_license_p(vehicle_list, vehicle):
    license_p_new = str(input("What is the new license plate of the vehicle?: "))
    original_license_p = vehicle.license_p
    while True:
        duplicate_found = False
        for element in vehicle_list:
            if element.license_p == license_p_new:
                print("A vehicle with this license plate already exists.")
                license_p_new = str(
                    input("What is the new license plate of the vehicle?: ")
                )
                duplicate_found = True

        if not duplicate_found:
            with open("vehicle_list.txt", "r") as file:
                lines = file.readlines()

            for index, line in enumerate(lines):
                if original_license_p in line:
                    vehicle.license_p = license_p_new
                    lines[index] = repr(vehicle) + "\n"
                    break

            with open("vehicle_list.txt", "w") as file:
                file.writelines(lines)

            break


# Function to update the purpose of a specific vehicle
def update_purpose(vehicle):
    purpose_new = str(input("What is the new purpose of the vehicle?: "))
    vehicle.purpose = purpose_new


# Function to update the weight of a specific vehicle
def update_weight(vehicle):
    while True:
        # Choose between increasing or decreasing weight
        add_reduce = int(input("Add weight [1] or reduce weight [2]?: "))
        if add_reduce == 1:
            added = float(input("How much weight [kg] did you add?: "))
            vehicle.weight += added * 0.001
            vehicle.weight = round(vehicle.weight, 2)
            vehicle.range = round(vehicle.fuel_level / (vehicle.weight * (5 / 100)), 2)
            break
        elif add_reduce == 2:
            reduced = float(input("How much weight [kg] did you take off?: "))
            vehicle.weight -= abs(reduced) * 0.001
            vehicle.weight = round(vehicle.weight, 2)
            vehicle.range = round(vehicle.fuel_level / (vehicle.weight * (5 / 100)), 2)
            break
        else:
            print("\nInvalid input, try again.")
            continue


# Function to update the fuel level of a specific vehicle
def update_fuel_level(vehicle):
    fuel_level_new = float(input("How much fuel is left in the vehicle?: "))
    vehicle.fuel_level = fuel_level_new
    # Rearranged fuel consumption formula
    vehicle.range = round(vehicle.fuel_level / (vehicle.weight * (5 / 100)), 2)


# Function to update the range of a specific vehicle
def update_range(vehicle):
    while True:
        # Choose between increasing or decreasing weight
        choice = int(input("Increase [1] or decrease [2]: "))
        if choice == 1:
            distance_increase = float(
                input("How much did the estimated range increase after refueling?: ")
            )
            vehicle.range += distance_increase

            # Ensure realistic numbers
            if vehicle.range > 1500:
                print(
                    "Invalid range. No negative ranges and no ranges over 1500 km allowed."
                )
                vehicle.range -= distance_increase
            else:
                fuel_consumed = round(
                    (vehicle.weight * (5 / 100)) * distance_increase, 2
                )
                vehicle.fuel_level += fuel_consumed
                vehicle.fuel_level = round(vehicle.fuel_level, 2)
                break
        elif choice == 2:
            distance_driven = float(input("How far [km] did you drive the vehicle?: "))
            vehicle.range -= distance_driven

            # Ensure realistic numbers
            if vehicle.range < 0:
                print(
                    "Invalid range. No negative ranges and no ranges over 1500 km allowed."
                )
                vehicle.range += distance_driven
            else:
                fuel_consumed = round((vehicle.weight * (5 / 100)) * distance_driven, 2)
                vehicle.fuel_level -= fuel_consumed
                vehicle.fuel_level = round(vehicle.fuel_level, 2)
                break
        else:
            print("Wrong input, try again.")
            continue


#
#
#


# Function to update the saved vehicle data in the file
def update_file(updated_vehicle):
    with open("vehicle_list.txt", "r") as file:
        lines = file.readlines()

    # Iterate through each line in the file
    for index, line in enumerate(lines):
        # If the line contains details of the vehicle to be updated
        if updated_vehicle.license_p in line:
            # Replace the old vehicle data with the updated data
            lines[index] = repr(updated_vehicle) + "\n"
            break

    # Write the updated list of vehicles back to the file
    with open("vehicle_list.txt", "w") as file:
        file.writelines(lines)

    file.close()


#
#
#


# Main function to handle modifications to a specific vehicle based on user input
def vehicle_change(vehicle_list, user_choice):
    # Find the vehicle in the list based on the provided license plate
    edit_vehicle = find_vehicle(vehicle_list, user_choice)

    # If the vehicle is not found, print a message and return
    # ( NOT NEEDED ANYMORE )
    # if not edit_vehicle:
    #   print("\nNo vehicle with that license plate. Try again")
    #   return

    # Display the vehicle details and available modification options to the user
    while True:
        print(
            f"""
        [0] Exit
        [1] Delete Vehicle
        [2] Copy Vehicle
        [3] {edit_vehicle.license_p}
        [4] {edit_vehicle.purpose}
        [5] {edit_vehicle.weight}
        [6] {edit_vehicle.fuel_level}
        [7] {edit_vehicle.range}
        """
        )

        # Get the user's choice for modification
        change = int(input("What would you like to do: "))

        # Execute the desired modification based on the user's choice
        if change == 0:
            print("\n Main Menu")
            break

        # Delete the selected vehicle
        elif change == 1:
            delete_vehicle(edit_vehicle, vehicle_list)
            print("\n Main Menu")
            break

        # Create a copy of the selected vehicle
        elif change == 2:
            copy_vehicle(vehicle_list, edit_vehicle)
            break

        # Update the license plate of the selected vehicle
        elif change == 3:
            update_license_p(vehicle_list, edit_vehicle)
            update_file(edit_vehicle)
            print(
                "\nLicense plate successfully updated.\nWhat would you like to do next?"
            )

        # Update the purpose of the selected vehicle
        elif change == 4:
            update_purpose(edit_vehicle)
            update_file(edit_vehicle)
            print("\nPurpose successfully updated.\nWhat would you like to do next?")

        # Update the weight of the selected vehicle
        elif change == 5:
            update_weight(edit_vehicle)
            update_file(edit_vehicle)
            print(
                "\nWeight (and range) successfully updated.\nWhat would you like to do next?"
            )

        # Update the fuel level of the selected vehicle
        elif change == 6:
            update_fuel_level(edit_vehicle)
            update_file(edit_vehicle)
            print(
                "\nFuel (and range) successfully updated.\nWhat would you like to do next?"
            )

        # Update the range of the selected vehicle
        elif change == 7:
            update_range(edit_vehicle)
            update_file(edit_vehicle)
            print("\nRange successfully updated.\nWhat would you like to do next?")

        else:
            print("\nInvalid input, try again.")
