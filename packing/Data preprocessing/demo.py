import os
import json

path = os.getcwd()
parent = os.path.dirname(path)
input_file = parent + "/Input_dataset/input1.json"

with open(input_file, 'r') as json_file:
    data = json.load(json_file)
