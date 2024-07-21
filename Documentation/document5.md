### Overview
This Flask application provides endpoints for 3D packing of items in a truck. It includes routes for both normal packing and packing with fragility considerations.

### Detailed Explaination
##### Import Statements
```
from flask import Flask, request
from packing_3d_tight import packing_3d
from fragility_packing import packing_3d_fragility
```
* Flask and request from flask: Flask is a micro web framework for Python. request is used to handle incoming request data.
* packing_3d: Function for normal 3D packing.
* packing_3d_fragility: Function for 3D packing with fragility considerations.
##### Flask App Initialization
```
app = Flask(__name__)
```
* app: Initializes a Flask application.
##### Home Route
```
@app.route("/")
def home():
    return "Hello"
```
* Defines the home route that returns a simple "Hello" message.
##### Route for 3D Packing Without Fragility Considerations
```
@app.route("/packing3d", methods=['POST'])
def packing3d():
    truck = {
        "length": int(request.form["truck_length"]),
        "width": int(request.form["truck_width"]),
        "height": int(request.form["truck_height"]),
        "maximum_capacity": int(request.form["truck_maximum_capacity"])
    }
    print(truck)

    itemName = "item"
    j = "0"
    current_item = itemName + j
    i = 0

    items = []

    try:
        while request.form[current_item + "_id"]:
            item = {
                "itemid": int(request.form[current_item + "_id"]),
                "length": int(request.form[current_item + "_length"]),
                "width": int(request.form[current_item + "_width"]),
                "height": int(request.form[current_item + "_height"]),
                "weight": int(request.form[current_item + "_weight"])
            }
            items.append(item)
            i += 1
            current_item = itemName + str(i)
    except:
        print(items)
        print("Data collected")

    input_data = {
        "truck": truck,
        "items": items
    }

    output_data = packing_3d(input_data)
    return output_data
```
* truck: Extracts truck dimensions and maximum capacity from the POST request form.
* items: Loops through the request form to extract item data, adding each item to the items list.
* input_data: Combines truck and item data into a single dictionary.
* Calls packing_3d with the input data and returns the output.
##### Route for 3D Packing With Fragility Considerations
```
@app.route("/packing3d_fragility", methods=['POST'])
def packing3d_fragility():
    truck = {
        "length": int(request.form["truck_length"]),
        "width": int(request.form["truck_width"]),
        "height": int(request.form["truck_height"]),
        "maximum_capacity": int(request.form["truck_maximum_capacity"])
    }
    print(truck)

    itemName = "item"
    j = "0"
    current_item = itemName + j
    i = 0

    items = []

    try:
        while request.form[current_item + "_id"]:
            item = {
                "itemid": int(request.form[current_item + "_id"]),
                "length": int(request.form[current_item + "_length"]),
                "width": int(request.form[current_item + "_width"]),
                "height": int(request.form[current_item + "_height"]),
                "weight": int(request.form[current_item + "_weight"]),
                "fragility": int(request.form[current_item + "_fragility"])
            }
            items.append(item)
            i += 1
            current_item = itemName + str(i)
    except:
        print(items)
        print("Data collected")

    input_data = {
        "truck": truck,
        "items": items
    }

    output_data = packing_3d_fragility(input_data)
    return output_data
```
* truck: Extracts truck dimensions and maximum capacity from the POST request form.
* items: Loops through the request form to extract item data, including fragility, adding each item to the items list.
* input_data: Combines truck and item data into a single dictionary.
* Calls packing_3d_fragility with the input data and returns the output.
##### Main Block
```
if __name__ == '__main__':
    app.run(debug=True)
```
* Starts the Flask application in debug mode when the script is run directly.
#### Summary
This Flask application provides two endpoints:

* '/packing3d': For normal 3D packing of items without considering fragility.
* '/packing3d_fragility': For 3D packing of items with fragility considerations.
The application extracts truck and item data from POST request forms, processes the data using the respective packing functions, and returns the packing arrangement as a JSON response.

Note: 
We have tested our code using [postman](https://www.postman.com/downloads/).
* Sample form data input:
  ![Postman Request](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/images/postman-request.png "Postman-Request")
* Sample response:
  ![Postman Response](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/images/postman-response.png "Postman-Response")
