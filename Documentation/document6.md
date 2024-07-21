### Overview
This script generates input data for 3D packing by creating truck and item data, then saving it in JSON format. The data includes truck dimensions, weight capacity, and a list of items with their respective dimensions and weights.

### Detailed Explanation
##### Import Statements
```
import random
import json
import os
```
* random: Used for generating random dimensions and weights for items.
* json: Used for reading from and writing to JSON files.
* os: Used for file path manipulations.
##### Generate Truck Data
```
def generate_truck_data(length, width, height, maximum_capacity):
    truck = {
        "length": length,
        "width": width,
        "height": height,
        "maximum_capacity": maximum_capacity
    }
    return truck
```
* Creates a dictionary representing the truck with given dimensions and maximum capacity.
##### Generate Item Data
```
def generate_item_data(itemid, length, width, height, maximum_capacity, no_items):
    item = {
        "itemid": itemid,
        "length": random.randint(1, length // 2),
        "width": random.randint(1, width // 2),
        "height": random.randint(1, height // 2),
        "weight": random.randint(1, maximum_capacity // no_items)
    }
    return item
```
* Creates a dictionary representing an item with random dimensions and weight. Dimensions and weight are constrained to be reasonable fractions of the truck's dimensions and capacity.
##### Generate Test Cases
```
def generate_test_cases(truck_dimensions, truck_weight_capacity, num_items):
    truck_data = generate_truck_data(*truck_dimensions, truck_weight_capacity)
    items_data = [generate_item_data(i, *truck_dimensions, truck_weight_capacity, num_items) for i in range(num_items)]

    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    file_name = parent_dir + "/Input_dataset/input1.json"

    if os.path.exists(file_name):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {"testcases": []}

    new_test_case = {
        "truck": truck_data,
        "items": items_data
    }

    data["testcases"].append(new_test_case)

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
```
* Generates truck and item data.
* Reads existing data from input1.json if it exists; otherwise, initializes a new data dictionary.
* Appends the new test case to the data.
* Writes the updated data back to input1.json.
##### Main Function
```
def main():
    truck_spec_1 = ((20, 15, 8), 4000)
    num_items_1 = 40
    generate_test_cases(*truck_spec_1, num_items_1)

    truck_spec_2 = ((18, 12, 8), 3500)
    num_items_2 = 35
    generate_test_cases(*truck_spec_2, num_items_2)
```
* Specifies two sets of truck dimensions, capacities, and item counts.
* Calls generate_test_cases for each set to generate and save the corresponding test cases.
##### Entry Point
```
if __name__ == "__main__":
    main()
```
* Runs the main function if the script is executed directly.

### Note:
We have created three input files for generating input data for three variants of the code we developed.There is only little bit difference in the three code in the part of the items generation function.
* dataGen1json.py is for packing_3d and packing_3d_tight.
* dataGen2json.py is for packing_3d_fragility and fragility packing.
* dataGen3json.py is for multiple_destinaions whose code is still in devlopment but input generation is over.
* dataGen1.py and PS(input test case generation) are the initial codes we developed for the txt input data format.

This is the end of the documentation.Back to [Table fo contents](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/README.md).
