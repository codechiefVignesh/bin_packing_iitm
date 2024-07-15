# Software requirements
Windows OS with:

1. python 3.11.0
2. pip above 9.1
3. Microsoft Visual Studio Enterprise 2022
4. Microsoft Visual Studio Community 2022 Preview 2 or above
5. numpy and pandas
6. Google ortools
7. matplotlib
8. Virtual Studio C++ redistributable

# Steps to include the library

* Clone the repo into the folder where you are working
```
git clone https://github.com/codechiefVignesh/bin_packing_iitm.git
```
* How to import the package and use it?
1. 3D container packing
```
from packing_3d import main
packing = main.packing_3d
print(packing(truck_dim,items))
```
The packing function takes two arguments one is the truck dimensions 
and second one is the list of all the items with their details.

2. 3D visualisation of the container packing
```
from visualisation import visualise
item_arrangements = packing_3d(truck_dim,items)
visualise(item_arrangements,truck_dim)
```
The visualise function takes two arguments one is the output from the 
previous packing_3d package and other is the truck dimensions.