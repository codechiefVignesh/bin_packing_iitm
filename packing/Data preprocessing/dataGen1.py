#generates input data for the 3d packing

import random
import os

def generate_test_case(truck_dimensions, truck_weight_capacity, num_items):
    # Unpack truck dimensions
    truck_length, truck_width, truck_height = truck_dimensions
    
    # List to store generated items
    items = []
    
    for i in range(1, num_items + 1):
        # Generate random dimensions within the truck's dimensions
        length = random.randint(1, truck_length)
        width = random.randint(1, truck_width)
        height = random.randint(1, truck_height)
        
        # Generate random weight ensuring the item is not too heavy
        weight = random.randint(1, truck_weight_capacity // num_items )
        
        # Append the generated item to the list
        items.append((i, (length, width, height), weight))
    
    return {"truck": (truck_dimensions, truck_weight_capacity), "items": items}

def append_test_case_to_file(test_case, file_name):
    with open(file_name, 'a') as f:
        truck = test_case["truck"]
        items = test_case["items"]
        
        f.write(f"Truck: {truck}\n")
        f.write("Items:[")
        for item in range(len(items)):
            f.write(f"{items[item]}")
            if item!=len(items) - 1:
                f.write(",")
            
        f.write("]\n\n")  # Add a blank line between test cases

# Define truck specifications and number of items
truck_spec_1 = ((18, 10, 5), 4000)
num_items_1 = 25

truck_spec_2 = ((20, 12, 6), 5000)
num_items_2 = 30

# Generate test cases
test_case_1 = generate_test_case(*truck_spec_1, num_items_1)
test_case_2 = generate_test_case(*truck_spec_2, num_items_2)

# Write test cases to text files
# Getting the path of the input dataset folder
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
file_name = parent_dir + "/Input_dataset/test_case_1.txt"
print(file_name)
append_test_case_to_file(test_case_1, file_name)
append_test_case_to_file(test_case_2, file_name)

print(f"Test cases appended to '{file_name}'")