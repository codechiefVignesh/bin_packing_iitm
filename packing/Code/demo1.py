from packing.Code.packing_3d_fragility import packing_3d
from visualisation1 import visualise
import os
import json

data_input = {
    "truck": {
        "length": 18,
        "width": 10,
        "height": 5,
        "maximum_capacity": 4000
    },
    "items": [
        {"itemid": 0, "length": 2, "width": 1, "height": 1, "weight": 90, "fragility": 45},
        {"itemid": 1, "length": 3, "width": 2, "height": 2, "weight": 99, "fragility": 90},
        {"itemid": 2, "length": 4, "width": 2, "height": 1, "weight": 38, "fragility": 200},
        {"itemid": 3, "length": 7, "width": 2, "height": 2, "weight": 108, "fragility": 10},
        {"itemid": 4, "length": 8, "width": 2, "height": 1, "weight": 123, "fragility": 99},
        {"itemid": 5, "length": 2, "width": 4, "height": 2, "weight": 54, "fragility": 300},
        {"itemid": 6, "length": 5, "width": 1, "height": 2, "weight": 159, "fragility": 250},
        {"itemid": 7, "length": 8, "width": 2, "height": 2, "weight": 135, "fragility": 75},
        {"itemid": 8, "length": 9, "width": 4, "height": 2, "weight": 24, "fragility": 15},
        {"itemid": 9, "length": 7, "width": 2, "height": 2, "weight": 17, "fragility": 25},
        {"itemid": 10, "length": 8, "width": 4, "height": 1, "weight": 86, "fragility": 15},
        {"itemid": 11, "length": 4, "width": 4, "height": 1, "weight": 59, "fragility": 150},
        {"itemid": 12, "length": 6, "width": 4, "height": 1, "weight": 105, "fragility": 105},
        {"itemid": 13, "length": 1, "width": 2, "height": 2, "weight": 73, "fragility": 10},
        {"itemid": 14, "length": 2, "width": 5, "height": 1, "weight": 100, "fragility": 40},
        {"itemid": 15, "length": 4, "width": 1, "height": 1, "weight": 104, "fragility": 80},
        {"itemid": 16, "length": 6, "width": 5, "height": 1, "weight": 32, "fragility": 100},
        {"itemid": 17, "length": 9, "width": 4, "height": 2, "weight": 145, "fragility": 60},
        {"itemid": 18, "length": 8, "width": 2, "height": 2, "weight": 100, "fragility": 300},
        {"itemid": 19, "length": 5, "width": 4, "height": 2, "weight": 71, "fragility": 200},
        {"itemid": 20, "length": 3, "width": 4, "height": 2, "weight": 93, "fragility": 100},
        {"itemid": 21, "length": 7, "width": 1, "height": 1, "weight": 23, "fragility": 90},
        {"itemid": 22, "length": 4, "width": 3, "height": 2, "weight": 38, "fragility": 45},
        {"itemid": 23, "length": 7, "width": 3, "height": 2, "weight": 91, "fragility": 75},
        {"itemid": 24, "length": 2, "width": 5, "height": 2, "weight": 32, "fragility": 10}
    ]
}

item_arrangements = packing_3d(data_input)
# print(item_arrangements)
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
output_file = parent_dir + "/Output/output1.json"

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
