### Overview
This demo code demonstrates the working of 3D packing and visualization of items in a truck. It uses a sample input of item data and truck dimensions to generate the coordinates of packed items and visualize the packing arrangement.

### Detailed explanation
##### Import Statements
```
from packing_3d import packing_3d
# from packing_3d_tight import packing_3d  # Uncomment this line for tight packing
from visualise_3d_packing_json import visualise
import os
import json
import time
```
* packing_3d: Function to perform normal packing.
* packing_3d_tight: Function to perform tight packing (commented out).
* visualise: Function to visualize the 3D packing.
* os: Module for interacting with the operating system and managing files
* json: Module for working with JSON data.
* time: Module for measuring execution time.
##### Initial Setup
```
start = time.time()
```
* start: Records the start time for measuring execution time.
##### Sample Input Data
```
data_input = {
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
        # Add more items here
    ]
}
```
* data_input: Dictionary containing truck dimensions and a list of items to be packed.
##### Output File Path
```
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
output_file = parent_dir + "/Output/output1.json"
```
* current_dir: Gets the current working directory.
* parent_dir: Gets the parent directory of the current working directory.
* output_file: Defines the path to the output JSON file.
##### Loading Existing Output Data
```
if os.path.exists(output_file):
    with open(output_file, 'r') as json_file:
        data = json.load(json_file)
else:
    data = {"Outputs":[]}
```
* Checks if the output file exists. If it does, loads the existing data; otherwise, initializes an empty dictionary.
##### Packing Items
```
item_arrangements = packing_3d(data_input)
new_item_arrangements = json.loads(item_arrangements)
```
* item_arrangements: Calls the packing_3d function to get the packed item coordinates.
* new_item_arrangements: Parses the JSON string returned by packing_3d.
##### Storing Output Data
```
new_output = {
    "item_arrangements": new_item_arrangements
}
data["Outputs"].append(new_output)

with open(output_file, 'w') as json_file:
    json.dump(data, json_file, indent=5)
```
* new_output: Creates a new dictionary with the item arrangements.
* Appends the new output to the existing data.
* Writes the updated data back to the output file.
##### Execution Time
```
end = time.time()
print(f"Time taken: {end - start} seconds")
```
* end: Records the end time for measuring execution time.
* Prints the time taken for the entire process.
##### Visualization
```
visualise(item_arrangements, data_input["truck"])
```
* Calls the visualise function to display the 3D packing arrangement.

### Note:
Here for the executing the demo we have created three different files for each type of the input.
* demo.py is for packing_3d and packing_3d_tight
* demo2.py is for packing_3d_fragility and fragility_packing
* demo3.py is for multiple_destination which is still pending. 
