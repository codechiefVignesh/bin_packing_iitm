#This is a demo code demonstrates the working of the 3d packing with fragility constraints and visualisation of the same.

#Import normal fragility function 
from packing_3d_fragility import packing_3d_fragility

#Import tight fragility function for better results. 
# from fragility_packing import packing_3d_fragility
from visualise_3d_packing_json import visualise
import os
import json
import time

start = time.time()

data_input = {
            "truck": {
                "length": 20,
                "width": 15,
                "height": 8,
                "maximum_capacity": 4000
            },
            "items": [
                {
                    "itemid": 0,
                    "length": 7,
                    "width": 3,
                    "height": 1,
                    "weight": 26,
                    "fragility": 52
                },
                {
                    "itemid": 1,
                    "length": 1,
                    "width": 5,
                    "height": 4,
                    "weight": 82,
                    "fragility": 142
                },
                {
                    "itemid": 2,
                    "length": 7,
                    "width": 6,
                    "height": 2,
                    "weight": 85,
                    "fragility": 110
                },
                {
                    "itemid": 3,
                    "length": 1,
                    "width": 4,
                    "height": 1,
                    "weight": 25,
                    "fragility": 19
                },
                {
                    "itemid": 4,
                    "length": 9,
                    "width": 4,
                    "height": 4,
                    "weight": 15,
                    "fragility": 22
                },
                {
                    "itemid": 5,
                    "length": 4,
                    "width": 4,
                    "height": 3,
                    "weight": 99,
                    "fragility": 155
                },
                {
                    "itemid": 6,
                    "length": 9,
                    "width": 3,
                    "height": 2,
                    "weight": 92,
                    "fragility": 74
                },
                {
                    "itemid": 7,
                    "length": 1,
                    "width": 6,
                    "height": 4,
                    "weight": 58,
                    "fragility": 46
                },
                {
                    "itemid": 8,
                    "length": 10,
                    "width": 6,
                    "height": 2,
                    "weight": 60,
                    "fragility": 62
                },
                {
                    "itemid": 9,
                    "length": 10,
                    "width": 7,
                    "height": 4,
                    "weight": 49,
                    "fragility": 27
                },
                {
                    "itemid": 10,
                    "length": 9,
                    "width": 1,
                    "height": 4,
                    "weight": 37,
                    "fragility": 49
                },
                {
                    "itemid": 11,
                    "length": 4,
                    "width": 6,
                    "height": 1,
                    "weight": 54,
                    "fragility": 72
                },
                {
                    "itemid": 12,
                    "length": 8,
                    "width": 3,
                    "height": 2,
                    "weight": 94,
                    "fragility": 157
                },
                {
                    "itemid": 13,
                    "length": 7,
                    "width": 1,
                    "height": 3,
                    "weight": 67,
                    "fragility": 33
                },
                {
                    "itemid": 14,
                    "length": 6,
                    "width": 7,
                    "height": 2,
                    "weight": 26,
                    "fragility": 19
                },
                {
                    "itemid": 15,
                    "length": 7,
                    "width": 1,
                    "height": 2,
                    "weight": 15,
                    "fragility": 8
                },
                {
                    "itemid": 16,
                    "length": 8,
                    "width": 7,
                    "height": 3,
                    "weight": 81,
                    "fragility": 142
                },
                {
                    "itemid": 17,
                    "length": 10,
                    "width": 2,
                    "height": 2,
                    "weight": 92,
                    "fragility": 63
                },
                {
                    "itemid": 18,
                    "length": 1,
                    "width": 6,
                    "height": 4,
                    "weight": 7,
                    "fragility": 13
                },
                {
                    "itemid": 19,
                    "length": 5,
                    "width": 5,
                    "height": 4,
                    "weight": 68,
                    "fragility": 105
                },
                {
                    "itemid": 20,
                    "length": 3,
                    "width": 2,
                    "height": 3,
                    "weight": 30,
                    "fragility": 28
                },
                {
                    "itemid": 21,
                    "length": 5,
                    "width": 6,
                    "height": 3,
                    "weight": 42,
                    "fragility": 49
                },
                {
                    "itemid": 22,
                    "length": 1,
                    "width": 4,
                    "height": 3,
                    "weight": 39,
                    "fragility": 32
                },
                {
                    "itemid": 23,
                    "length": 10,
                    "width": 3,
                    "height": 1,
                    "weight": 43,
                    "fragility": 33
                },
                {
                    "itemid": 24,
                    "length": 4,
                    "width": 3,
                    "height": 2,
                    "weight": 19,
                    "fragility": 27
                },
                {
                    "itemid": 25,
                    "length": 10,
                    "width": 6,
                    "height": 3,
                    "weight": 12,
                    "fragility": 22
                },
                {
                    "itemid": 26,
                    "length": 3,
                    "width": 4,
                    "height": 1,
                    "weight": 1,
                    "fragility": 1
                },
                {
                    "itemid": 27,
                    "length": 7,
                    "width": 1,
                    "height": 2,
                    "weight": 38,
                    "fragility": 25
                },
                {
                    "itemid": 28,
                    "length": 1,
                    "width": 6,
                    "height": 2,
                    "weight": 52,
                    "fragility": 95
                },
                {
                    "itemid": 29,
                    "length": 2,
                    "width": 1,
                    "height": 1,
                    "weight": 98,
                    "fragility": 77
                },
                {
                    "itemid": 30,
                    "length": 4,
                    "width": 4,
                    "height": 3,
                    "weight": 94,
                    "fragility": 51
                },
                {
                    "itemid": 31,
                    "length": 10,
                    "width": 5,
                    "height": 4,
                    "weight": 24,
                    "fragility": 21
                },
                {
                    "itemid": 32,
                    "length": 2,
                    "width": 4,
                    "height": 2,
                    "weight": 54,
                    "fragility": 71
                },
                {
                    "itemid": 33,
                    "length": 10,
                    "width": 6,
                    "height": 4,
                    "weight": 11,
                    "fragility": 19
                },
                {
                    "itemid": 34,
                    "length": 4,
                    "width": 5,
                    "height": 4,
                    "weight": 98,
                    "fragility": 193
                },
                {
                    "itemid": 35,
                    "length": 4,
                    "width": 1,
                    "height": 2,
                    "weight": 2,
                    "fragility": 1
                },
                {
                    "itemid": 36,
                    "length": 3,
                    "width": 2,
                    "height": 1,
                    "weight": 55,
                    "fragility": 58
                },
                {
                    "itemid": 37,
                    "length": 4,
                    "width": 6,
                    "height": 3,
                    "weight": 68,
                    "fragility": 104
                },
                {
                    "itemid": 38,
                    "length": 7,
                    "width": 5,
                    "height": 3,
                    "weight": 99,
                    "fragility": 165
                },
                {
                    "itemid": 39,
                    "length": 7,
                    "width": 2,
                    "height": 1,
                    "weight": 90,
                    "fragility": 104
                }
            ]
        }

# Call the packing function to get the item arrangements
item_arrangements = packing_3d_fragility(data_input)

# Get the current working directory
current_dir = os.getcwd()
# Get the parent directory
parent_dir = os.path.dirname(current_dir)
# Define the output file path
output_file = parent_dir + "/Output/output2.json"

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

end = time.time()

print(f"Time taken: {end-start}seconds")

# Visualize the item arrangements in the truck
visualise(item_arrangements, data_input["truck"])
