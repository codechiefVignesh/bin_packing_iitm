import random
import json
import os

def generate_truck_data(length, width, height, maximum_capacity):
    truck = {
        "length":length,
        "width":width,
        "height":height,
        "maximum_capacity":maximum_capacity
    }

    return truck

def generate_item_data(itemid, length, width, height, maximum_capacity, no_items, no_locations):
    item = {
        "itemid":itemid,
        "length":random.randint(1,length//2),
        "width":random.randint(1,width//2),
        "height":random.randint(1,height//2),
        "weight":random.randint(1,maximum_capacity // no_items),
        "location":random.randint(1,no_locations)
    }

    return item

def generate_test_cases(truck_dimensions, truck_weight_capacity, num_items, no_locations):
    truck_data = generate_truck_data( *truck_dimensions, truck_weight_capacity)
    items_data = [generate_item_data(i, *truck_dimensions, truck_weight_capacity, num_items, no_locations) for i in range(num_items)]

    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    file_name = parent_dir + "/Input_dataset/input2.json"

    if os.path.exists(file_name):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {"testcases":[]}

    new_test_case = {
        "truck":truck_data,
        "items":items_data
    }

    data["testcases"].append(new_test_case)

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    truck_spec_1 = ((12, 6, 4), 400)
    num_items_1 = 10
    num_locations_1 = 5

    generate_test_cases( *truck_spec_1, num_items_1, num_locations_1)

    truck_spec_2 = ((15, 10, 6), 900)
    num_items_2 = 15
    num_locations_2 = 5

    generate_test_cases( *truck_spec_2, num_items_2, num_locations_2)

if __name__ == "__main__":
    main()