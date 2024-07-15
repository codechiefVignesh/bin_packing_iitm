from multiple_destinations1 import packing_3d
from visualisation2 import visualise
import os
import json

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

item_arrangements = packing_3d(data_input)
# print(item_arrangements)
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
output_file = parent_dir + "/Output/output2.json"

if os.path.exists(output_file):
    with open(output_file, 'r') as json_file:
        data = json.load(json_file)
else:
    data = {"Outputs":[]}

new_item_arrangements = json.loads(item_arrangements)

# print(new_item_arrangements)

new_output = {
    "item_arrangements":new_item_arrangements
    }
data["Outputs"].append(new_output)

with open(output_file, 'w') as json_file:
    json.dump(data, json_file, indent=5)

# print(type(item_arrangements))
visualise(item_arrangements,data_input["truck"])
