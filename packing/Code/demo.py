#This is a demo code demonstrates the working of the 3d packing and visuailistion of the same.

#The below line imports normal packing function
# from packing_3d import packing_3d

#The below line import tight packing function which will give better results
from packing_3d_tight import packing_3d
from visualise_3d_packing_json import visualise
import os
import json
import time

start = time.time()

#This is an example of sample input data which we have generated using the dataGen1.py file 
data_input ={
            "truck": {
                "length": 16,
                "width": 10,
                "height": 6,
                "maximum_capacity": 3000
            },
            "items": [
                {
                    "itemid": 0,
                    "length": 2,
                    "width": 5,
                    "height": 2,
                    "weight": 108
                },
                {
                    "itemid": 1,
                    "length": 2,
                    "width": 3,
                    "height": 2,
                    "weight": 75
                },
                {
                    "itemid": 2,
                    "length": 4,
                    "width": 1,
                    "height": 1,
                    "weight": 92
                },
                {
                    "itemid": 3,
                    "length": 3,
                    "width": 2,
                    "height": 2,
                    "weight": 78
                },
                {
                    "itemid": 4,
                    "length": 7,
                    "width": 4,
                    "height": 3,
                    "weight": 89
                },
                {
                    "itemid": 5,
                    "length": 7,
                    "width": 4,
                    "height": 1,
                    "weight": 113
                },
                {
                    "itemid": 6,
                    "length": 7,
                    "width": 3,
                    "height": 1,
                    "weight": 44
                },
                {
                    "itemid": 7,
                    "length": 1,
                    "width": 5,
                    "height": 1,
                    "weight": 45
                },
                {
                    "itemid": 8,
                    "length": 2,
                    "width": 4,
                    "height": 1,
                    "weight": 49
                },
                {
                    "itemid": 9,
                    "length": 7,
                    "width": 5,
                    "height": 2,
                    "weight": 92
                },
                {
                    "itemid": 10,
                    "length": 3,
                    "width": 3,
                    "height": 2,
                    "weight": 72
                },
                {
                    "itemid": 11,
                    "length": 3,
                    "width": 4,
                    "height": 3,
                    "weight": 30
                },
                {
                    "itemid": 12,
                    "length": 5,
                    "width": 2,
                    "height": 2,
                    "weight": 119
                },
                {
                    "itemid": 13,
                    "length": 2,
                    "width": 5,
                    "height": 1,
                    "weight": 26
                },
                {
                    "itemid": 14,
                    "length": 8,
                    "width": 3,
                    "height": 1,
                    "weight": 37
                },
                {
                    "itemid": 15,
                    "length": 3,
                    "width": 4,
                    "height": 1,
                    "weight": 2
                },
                {
                    "itemid": 16,
                    "length": 3,
                    "width": 1,
                    "height": 3,
                    "weight": 31
                },
                {
                    "itemid": 17,
                    "length": 1,
                    "width": 2,
                    "height": 3,
                    "weight": 58
                },
                {
                    "itemid": 18,
                    "length": 2,
                    "width": 3,
                    "height": 1,
                    "weight": 27
                },
                {
                    "itemid": 19,
                    "length": 8,
                    "width": 2,
                    "height": 3,
                    "weight": 67
                },
                {
                    "itemid": 20,
                    "length": 3,
                    "width": 4,
                    "height": 1,
                    "weight": 1
                },
                {
                    "itemid": 21,
                    "length": 2,
                    "width": 5,
                    "height": 1,
                    "weight": 7
                },
                {
                    "itemid": 22,
                    "length": 4,
                    "width": 4,
                    "height": 1,
                    "weight": 60
                },
                {
                    "itemid": 23,
                    "length": 4,
                    "width": 1,
                    "height": 1,
                    "weight": 39
                },
                {
                    "itemid": 24,
                    "length": 6,
                    "width": 5,
                    "height": 1,
                    "weight": 85
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

end = time.time()

print(f"Time taken: {end-start}seconds")

#calling visualise function which displays the output of 3d packing
visualise(item_arrangements,data_input["truck"])
