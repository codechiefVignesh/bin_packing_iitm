import ast

# Read input file
with open('input.txt', 'r') as file:
    input_data = file.read()

# Parse input data
trucks_and_items = input_data.split('\n\n')
print(trucks_and_items)
parsed_data = []

for truck_and_items in trucks_and_items:
    truck_lines = truck_and_items.strip().split('\n')
    truck_info = ast.literal_eval(truck_lines[0].split(': ')[1])
    items_info = ast.literal_eval(truck_lines[1].split(': ')[1])
    parsed_data.append((truck_info, items_info))

# Import packing_3d function from main.py
from main import packing_3d

# Open output file
with open('output.txt', 'w') as output_file:
    # Iterate over parsed data and run the packing_3d function
    for truck_info, items_info in parsed_data:
        truck_dim = {"dimensions": truck_info[0], "maximum_capacity": truck_info[1]}
        items_dict = {
            "itemid": [item[0] for item in items_info],
            "length": [item[1][0] for item in items_info],
            "width": [item[1][1] for item in items_info],
            "height": [item[1][2] for item in items_info],
            "weight": [item[2] for item in items_info],
            "value": [1 for item in items_info],  # Assuming value is the same as weight
        }
        result = packing_3d(truck_dim, items_dict)
        output_file.write(f"Truck {truck_info[0]} results:\n")
        output_file.write(str(result) + "\n\n")
