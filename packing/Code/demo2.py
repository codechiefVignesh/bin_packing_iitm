# Import the packing function for multiple destinations
from multiple_destinations import packing_3d_multiple_destinations
# Import the visualization function
from visualise_3d_packing_locations import visualise

import os
import json

# Define the input data
data_input = {
    "truck": {
        "length": 15,
        "width": 10,
        "height": 6,
        "maximum_capacity": 900
    },
    "items": [
        {
            "itemid": 0,
            "length": 4,
            "width": 1,
            "height": 2,
            "weight": 21,
            "location": 3
        },
        {
            "itemid": 1,
            "length": 7,
            "width": 3,
            "height": 2,
            "weight": 57,
            "location": 1
        },
        {
            "itemid": 2,
            "length": 1,
            "width": 3,
            "height": 1,
            "weight": 10,
            "location": 4
        },
        {
            "itemid": 3,
            "length": 7,
            "width": 5,
            "height": 2,
            "weight": 9,
            "location": 3
        },
        {
            "itemid": 4,
            "length": 1,
            "width": 4,
            "height": 1,
            "weight": 7,
            "location": 4
        },
        {
            "itemid": 5,
            "length": 7,
            "width": 5,
            "height": 2,
            "weight": 4,
            "location": 1
        },
        {
            "itemid": 6,
            "length": 1,
            "width": 1,
            "height": 1,
            "weight": 5,
            "location": 4
        },
        {
            "itemid": 7,
            "length": 6,
            "width": 5,
            "height": 1,
            "weight": 7,
            "location": 2
        },
        {
            "itemid": 8,
            "length": 2,
            "width": 5,
            "height": 3,
            "weight": 26,
            "location": 5
        },
        {
            "itemid": 9,
            "length": 7,
            "width": 5,
            "height": 3,
            "weight": 40,
            "location": 4
        },
        {
            "itemid": 10,
            "length": 1,
            "width": 4,
            "height": 3,
            "weight": 38,
            "location": 4
        },
        {
            "itemid": 11,
            "length": 1,
            "width": 2,
            "height": 3,
            "weight": 36,
            "location": 1
        },
        {
            "itemid": 12,
            "length": 6,
            "width": 5,
            "height": 1,
            "weight": 31,
            "location": 5
        },
        {
            "itemid": 13,
            "length": 1,
            "width": 3,
            "height": 1,
            "weight": 33,
            "location": 4
        },
        {
            "itemid": 14,
            "length": 3,
            "width": 5,
            "height": 3,
            "weight": 52,
            "location": 1
        }
    ]
}

# Call the packing function to get the item arrangements
item_arrangements = packing_3d_multiple_destinations(data_input)

# Get the current working directory
current_dir = os.getcwd()
# Get the parent directory
parent_dir = os.path.dirname(current_dir)
# Define the output file path
output_file = parent_dir + "/Output/output3.json"

# Check if the output file exists
if os.path.exists(output_file):
    # If the file exists, read the existing data
    with open(output_file, 'r') as json_file:
        data = json.load(json_file)
else:
    # If the file does not exist, create an empty dictionary with "Outputs" as a key
    data = {"Outputs":[]}

# Load the new item arrangements from the packing function
new_item_arrangements = json.loads(item_arrangements)

# Create a new output dictionary with the item arrangements
new_output = {
    "item_arrangements": new_item_arrangements
}
# Append the new output to the existing data
data["Outputs"].append(new_output)

# Write the updated data back to the output file
with open(output_file, 'w') as json_file:
    json.dump(data, json_file, indent=5)

# Visualize the item arrangements in the truck
visualise(item_arrangements, data_input["truck"])