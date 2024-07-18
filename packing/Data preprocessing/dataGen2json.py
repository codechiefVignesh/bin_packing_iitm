#Generates input data for 3d packing with fragility constraints in form of json

import random
import json
import os

# Function to generate truck data
def generate_truck_data(length, width, height, maximum_capacity):
    truck = {
        "length":length,
        "width":width,
        "height":height,
        "maximum_capacity":maximum_capacity
    }

    return truck

# Function to generate item data
def generate_item_data(itemid, length, width, height, maximum_capacity, no_items):
    weight = random.randint(1,maximum_capacity // no_items)
    item = {
        "itemid":itemid,
        "length":random.randint(1,length//2),
        "width":random.randint(1,width//2),
        "height":random.randint(1,height//2),
        "weight":weight,
        "fragility":random.randint(weight // 2,2 * weight)
    }

    return item

# Function to generate test cases
def generate_test_cases(truck_dimensions, truck_weight_capacity, num_items):
    # Generate truck data
    truck_data = generate_truck_data( *truck_dimensions, truck_weight_capacity)
    # Generate items data
    items_data = [generate_item_data(i, *truck_dimensions, truck_weight_capacity, num_items) for i in range(num_items)]

    # Determine the path to the input file
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    file_name = parent_dir + "/Input_dataset/input2.json"

    # Load existing data if the file exists, otherwise initialize a new data dictionary
    if os.path.exists(file_name):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {"testcases":[]}

     # Add the new test case to the data
    new_test_case = {
        "truck":truck_data,
        "items":items_data
    }

    data["testcases"].append(new_test_case)

    # Write the updated data back to the file
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Main function to generate specific test cases
def main():
    truck_spec_1 = ((12, 6, 4), 400)
    num_items_1 = 10
    generate_test_cases( *truck_spec_1, num_items_1)

    truck_spec_2 = ((15, 10, 6), 900)
    num_items_2 = 15

    generate_test_cases( *truck_spec_2, num_items_2)

# Entry point of the script
if __name__ == "__main__":
    main()
