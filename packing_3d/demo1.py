from main import packing_3d
from visualisation import visualise

truck_dim = {"dimensions":(12,8,5),"maximum_capacity":400}
items = {"itemid":[1,2,3,4,5,6,7,8],"length":[11,5,12,10,2,10,12,10],"width":[2,4,5,7,4,1,7,5],"height":[1,2,2,1,2,5,2,1],"weight":[48,9,6,2,33,13,29,49],"value":[1,1,1,1,1,1,1,1]}

item_arrangements = packing_3d(truck_dim,items)
print(item_arrangements)
visualise(item_arrangements,truck_dim)

