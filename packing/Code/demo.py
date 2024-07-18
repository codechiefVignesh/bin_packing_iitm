#This is a demo code demonstrates the working of the 3d packing and visuailistion of the same.

#The below line imports normal packing function
# from packing_3d import packing_3d

#The below line import tight packing function which will give better results
from packing_3d_tight import packing_3d
from visualise_3d_packing_json import visualise
import os
import json

#This is an example of sample input data which we have generated using the dataGen1.py file 
data_input ={
            "truck": {
                "length": 20,
                "width": 12,
                "height": 6,
                "maximum_capacity": 5000
            },
            "items": [
                {
                    "itemid": 0,
                    "length": 9,
                    "width": 1,
                    "height": 2,
                    "weight": 129
                },
                {
                    "itemid": 1,
                    "length": 9,
                    "width": 4,
                    "height": 2,
                    "weight": 163
                },
                {
                    "itemid": 2,
                    "length": 4,
                    "width": 2,
                    "height": 2,
                    "weight": 66
                },
                {
                    "itemid": 3,
                    "length": 7,
                    "width": 6,
                    "height": 2,
                    "weight": 98
                },
                {
                    "itemid": 4,
                    "length": 8,
                    "width": 1,
                    "height": 3,
                    "weight": 61
                },
                {
                    "itemid": 5,
                    "length": 10,
                    "width": 5,
                    "height": 2,
                    "weight": 56
                },
                {
                    "itemid": 6,
                    "length": 5,
                    "width": 6,
                    "height": 2,
                    "weight": 109
                },
                {
                    "itemid": 7,
                    "length": 6,
                    "width": 4,
                    "height": 1,
                    "weight": 119
                },
                {
                    "itemid": 8,
                    "length": 9,
                    "width": 3,
                    "height": 3,
                    "weight": 80
                },
                {
                    "itemid": 9,
                    "length": 6,
                    "width": 5,
                    "height": 3,
                    "weight": 133
                },
                {
                    "itemid": 10,
                    "length": 7,
                    "width": 2,
                    "height": 1,
                    "weight": 130
                },
                {
                    "itemid": 11,
                    "length": 9,
                    "width": 3,
                    "height": 1,
                    "weight": 158
                },
                {
                    "itemid": 12,
                    "length": 7,
                    "width": 1,
                    "height": 1,
                    "weight": 91
                },
                {
                    "itemid": 13,
                    "length": 10,
                    "width": 1,
                    "height": 1,
                    "weight": 103
                },
                {
                    "itemid": 14,
                    "length": 4,
                    "width": 5,
                    "height": 2,
                    "weight": 93
                }
            ]
        }

#Path to the output json file
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
output_file = parent_dir + "/Output/output1.json"

if os.path.exists(output_file):
    with open(output_file, 'r') as json_file:
        data = json.load(json_file)
else:
    data = {"Outputs":[]}

#packing_3d function returns a json which contains the coordinates of the items to be placed inside the truck
item_arrangements = packing_3d(data_input)

new_item_arrangements = json.loads(item_arrangements)

# print(new_item_arrangements)

new_output = {
                "item_arrangements":new_item_arrangements
            }

data["Outputs"].append(new_output)

with open(output_file, 'w') as json_file:
    json.dump(data, json_file, indent=5)

# print(type(item_arrangements))

#calling visualise function which displays the output of 3d packing
visualise(item_arrangements,data_input["truck"])
