from packing_3d_dup import packing_3d
from visualisation1 import visualise
import os
import json

data_input ={
                "truck": {
                "length": 18,
                "width": 10,
                "height": 5,
                "maximum_capacity": 4000
            },
            "items": [
                {
                    "itemid": 0,
                    "length": 2,
                    "width": 1,
                    "height": 1,
                    "weight": 90
                },
                {
                    "itemid": 1,
                    "length": 3,
                    "width": 2,
                    "height": 2,
                    "weight": 99
                },
                {
                    "itemid": 2,
                    "length": 4,
                    "width": 2,
                    "height": 1,
                    "weight": 38
                },
                {
                    "itemid": 3,
                    "length": 7,
                    "width": 2,
                    "height": 2,
                    "weight": 108
                },
                {
                    "itemid": 4,
                    "length": 8,
                    "width": 2,
                    "height": 1,
                    "weight": 123
                },
                {
                    "itemid": 5,
                    "length": 2,
                    "width": 4,
                    "height": 2,
                    "weight": 54
                },
                {
                    "itemid": 6,
                    "length": 5,
                    "width": 1,
                    "height": 2,
                    "weight": 159
                },
                {
                    "itemid": 7,
                    "length": 8,
                    "width": 2,
                    "height": 2,
                    "weight": 135
                },
                {
                    "itemid": 8,
                    "length": 9,
                    "width": 4,
                    "height": 2,
                    "weight": 24
                },
                {
                    "itemid": 9,
                    "length": 7,
                    "width": 2,
                    "height": 2,
                    "weight": 17
                },
                {
                    "itemid": 10,
                    "length": 8,
                    "width": 4,
                    "height": 1,
                    "weight": 86
                },
                {
                    "itemid": 11,
                    "length": 4,
                    "width": 4,
                    "height": 1,
                    "weight": 59
                },
                {
                    "itemid": 12,
                    "length": 6,
                    "width": 4,
                    "height": 1,
                    "weight": 105
                },
                {
                    "itemid": 13,
                    "length": 1,
                    "width": 2,
                    "height": 2,
                    "weight": 73
                },
                {
                    "itemid": 14,
                    "length": 2,
                    "width": 5,
                    "height": 1,
                    "weight": 100
                },
                {
                    "itemid": 15,
                    "length": 4,
                    "width": 1,
                    "height": 1,
                    "weight": 104
                },
                {
                    "itemid": 16,
                    "length": 6,
                    "width": 5,
                    "height": 1,
                    "weight": 32
                },
                {
                    "itemid": 17,
                    "length": 9,
                    "width": 4,
                    "height": 2,
                    "weight": 145
                },
                {
                    "itemid": 18,
                    "length": 8,
                    "width": 2,
                    "height": 2,
                    "weight": 100
                },
                {
                    "itemid": 19,
                    "length": 5,
                    "width": 4,
                    "height": 2,
                    "weight": 71
                },
                {
                    "itemid": 20,
                    "length": 3,
                    "width": 4,
                    "height": 2,
                    "weight": 93
                },
                {
                    "itemid": 21,
                    "length": 7,
                    "width": 1,
                    "height": 1,
                    "weight": 23
                },
                {
                    "itemid": 22,
                    "length": 4,
                    "width": 3,
                    "height": 2,
                    "weight": 38
                },
                {
                    "itemid": 23,
                    "length": 7,
                    "width": 3,
                    "height": 2,
                    "weight": 91
                },
                {
                    "itemid": 24,
                    "length": 2,
                    "width": 5,
                    "height": 2,
                    "weight": 32
                }
            ]
        }

item_arrangements = packing_3d(data_input)
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
