from flask import Flask,request
from packing_3d_tight import packing_3d
from fragility_packing import packing_3d_fragility

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

# Route for 3D packing without fragility considerations
@app.route("/packing3d",methods=['POST'])
def packing3d():
    # Extract truck data from the request form
    truck = {
        "length":int(request.form["truck_length"]),
        "width":int(request.form["truck_width"]),
        "height":int(request.form["truck_height"]),
        "maximum_capacity":int(request.form["truck_maximum_capacity"])
    }
    print(truck)

    itemName = "item"
    j = "0"
    current_item = itemName + j
    i = 0

    items = []

    # Loop to extract all items data from the request form
    try:

        while(request.form[current_item + "_id"]):
            item = {
                "itemid":int(request.form[current_item + "_id"]),
                "length":int(request.form[current_item + "_length"]),
                "width":int(request.form[current_item + "_width"]),
                "height":int(request.form[current_item + "_height"]),
                "weight":int(request.form[current_item + "_weight"])
            }

            items.append(item)

            i += 1

            current_item = itemName + str(i)
    except:
        print(items)
        print("Data collected")        

    input_data = {
        "truck":truck,
        "items":items
    }

    # Call the packing function and return the output
    output_data = packing_3d(input_data)

    return output_data

# Route for 3D packing with fragility considerations
@app.route("/packing3d_fragility",methods=['POST'])
def packing3d_fragility():
    # Extract truck data from the request form
    truck = {
        "length":int(request.form["truck_length"]),
        "width":int(request.form["truck_width"]),
        "height":int(request.form["truck_height"]),
        "maximum_capacity":int(request.form["truck_maximum_capacity"])
    }
    print(truck)

    itemName = "item"
    j = "0"
    current_item = itemName + j
    i = 0

    items = []

    # Loop to extract all items data from the request form
    try:

        while(request.form[current_item + "_id"]):
            item = {
                "itemid":int(request.form[current_item + "_id"]),
                "length":int(request.form[current_item + "_length"]),
                "width":int(request.form[current_item + "_width"]),
                "height":int(request.form[current_item + "_height"]),
                "weight":int(request.form[current_item + "_weight"]),
                "fragility":int(request.form[current_item + "_fragility"])
            }

            items.append(item)

            i += 1

            current_item = itemName + str(i)
    except:
        print(items)
        print("Data collected")        

    input_data = {
        "truck":truck,
        "items":items
    }

    # Call the fragility packing function and return the output
    output_data = packing_3d_fragility(input_data)

    return output_data



if __name__ == '__main__':
    app.run(debug=True)

