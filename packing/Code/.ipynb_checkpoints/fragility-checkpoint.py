from ortools.sat.python import cp_model
from io import StringIO
import pandas as pd
import numpy as np
import json

def packing_3d(data):
    try:
        #---------------------------------------------------
        # Input data format
        #---------------------------------------------------
        truck_data = data["truck"]
        items = data["items"]

        df = pd.DataFrame.from_dict(items)
        
        L = truck_data["length"]
        W = truck_data["width"]
        H = truck_data["height"]
        M = truck_data["maximum_capacity"]

        #---------------------------------------------------
        # Derived data from the items
        # Extract the length, width, height, weight, and fragility of every item.
        # Here value represents the priority of the items
        #---------------------------------------------------

        l0 = df["length"].to_numpy()
        b0 = df['width'].to_numpy()
        h0 = df['height'].to_numpy()
        w0 = df['weight'].to_numpy()
        f0 = df['fragility'].to_numpy()

        n = len(l0)

        #----------------------------------------------------------------------------------------------------------------
        # Creating duplicate items dimensions and properties to represent all 6 possible rotations of the item in 3D space.
        # For each item we are creating its duplicates which will represent all its other rotations. 
        #----------------------------------------------------------------------------------------------------------------

        # six possible rotations of a 3D object
        l_rot = np.concatenate((l0, l0, b0, b0, h0, h0))
        w_rot = np.concatenate((b0, h0, l0, h0, b0, l0))
        h_rot = np.concatenate((h0, b0, h0, l0, l0, b0))

        # Duplicating the weights, heights, fragility, and itemid for each item.
        wr = np.tile(w0, 6)
        fr = np.tile(f0, 6)
        itemid = np.tile(df['itemid'].to_numpy(), 6)

        nr = 6 * n

        #------------------------------------------------------------------------------------------------
        # or-tools model
        #------------------------------------------------------------------------------------------------

        model = cp_model.CpModel()

        # variables
        
        # Representing each item in an array u where 0 represents it is taken and 1 represents it is not.
        # u[i]: item i is used (0/1) 
        u = [model.NewBoolVar(f"u{i}") for i in range(nr)]

        # Here x,y,z are arrays representing the starting coordinates of each item in the array u.
        # x[i], y[i], z[i]: location of item i (The starting corner of the item)
        x = [model.NewIntVar(0, L, f"x{i}") for i in range(nr)]
        y = [model.NewIntVar(0, W, f"y{i}") for i in range(nr)]
        z = [model.NewIntVar(0, H, f"z{i}") for i in range(nr)]

        # Here lx, ly, and lz represent the length, width, and height of each item in the array u.
        # lx[i], ly[i], lz[i]: dimensions of item i
        lx = [model.NewIntVar(0, L, f"lx{i}") for i in range(nr)]
        ly = [model.NewIntVar(0, W, f"ly{i}") for i in range(nr)]
        lz = [model.NewIntVar(0, H, f"lz{i}") for i in range(nr)]

        # Here x2, y2, and z2 represent the opposite coordinates of each item in the array u.
        # x2[i], y2[i], z2[i]: upper limit of interval variable (the opposite corner of the item)
        x2 = [model.NewIntVar(0, L, f"x2{i}") for i in range(nr)]
        y2 = [model.NewIntVar(0, W, f"y2{i}") for i in range(nr)]
        z2 = [model.NewIntVar(0, H, f"z2{i}") for i in range(nr)]

        # Here xival, yival, and zival are called interval variables.
        # Each line creates a list of interval variables xival, 
        # where each interval starts at x[i], has a length of lx[i], ends at x2[i], and is named xival{i}.
        xival = [model.NewIntervalVar(x[i], lx[i], x2[i], f"xival{i}") for i in range(nr)]
        yival = [model.NewIntervalVar(y[i], ly[i], y2[i], f"yival{i}") for i in range(nr)]
        zival = [model.NewIntervalVar(z[i], lz[i], z2[i], f"zival{i}") for i in range(nr)]

        #-----------------------------------------------------------------------------------------------
        # CONSTRAINTS
        #-----------------------------------------------------------------------------------------------
        
        # The main idea here is: if an item is not selected, make its length, width, and height zero.
        # This is done only to reduce the resource usage.

        # u[i] = 0  ==> lx[i] = ly[i] = lz[i] = 0
        # u[i] = 1  ==> lx[i] = l_rot[i], ly[i] = w_rot[i], lz[i] = h_rot[i]



        for i in range(nr):
            model.Add(lx[i] == l_rot[i] * u[i])
            model.Add(ly[i] == w_rot[i] * u[i])
            model.Add(lz[i] == h_rot[i] * u[i])

        # only one of the six possible rotations can be used
        # It is checking only one item is selected from the 6 possible rotations of an object.
        for i in range(n):
            model.Add(sum(u[i + j * n] for j in range(6)) <= 1)

        # no overlap in 3D
        # Here we are writing conditions for two 3D cuboids to not overlap each other in the 3D space.
        # Condition: All the coordinates of one corner of the cuboid shouldn't lie inside the other cuboid. 
        for i in range(nr):
            for j in range(i + 1, nr):
                c1 = model.NewBoolVar("c1")
                c2 = model.NewBoolVar("c2")
                c3 = model.NewBoolVar("c3")
                c4 = model.NewBoolVar("c4")
                c5 = model.NewBoolVar("c5")
                c6 = model.NewBoolVar("c6")

                model.Add(x2[i] <= x[j]).OnlyEnforceIf(c1)
                model.Add(x2[j] <= x[i]).OnlyEnforceIf(c2)
                model.Add(y2[i] <= y[j]).OnlyEnforceIf(c3)
                model.Add(y2[j] <= y[i]).OnlyEnforceIf(c4)
                model.Add(z2[i] <= z[j]).OnlyEnforceIf(c5)
                model.Add(z2[j] <= z[i]).OnlyEnforceIf(c6)

                model.AddBoolOr([c1, c2, c3, c4, c5, c6])

        # fragility constraint

        
        for i in range(nr):
            weight_above = model.NewIntVar(0, M, f"weight_above{i}")
            total_weight_above = []
            for j in range(nr):
                if i != j:
                    above = model.NewBoolVar(f"above_{i}_{j}")
                    model.Add(x[j] < x2[i]).OnlyEnforceIf(above)
                    model.Add(x2[j] > x[i]).OnlyEnforceIf(above)
                    model.Add(y[j] < y2[i]).OnlyEnforceIf(above)
                    model.Add(y2[j] > y[i]).OnlyEnforceIf(above)
                    model.Add(z[j] >= z2[i]).OnlyEnforceIf(above)
                    model.Add(z[j] < z2[i] + h_rot[i]).OnlyEnforceIf(above)

                    # Add the weight of item j to total weight above item i
                    total_weight_above.append(wr[j] * above)
            
            # Sum all the weights above and constrain it by the fragility of item i
            model.Add(weight_above == sum(total_weight_above))
            model.Add(weight_above <= fr[i])
            
            # Ensure weight_above does not exceed fragility of item i
            # model.Add(weight_above <= fr[i])


        # extra: this constraint helps performance enormously (space constraints)
        # The constraint ensures that the total volume of the selected items does not exceed the volume of the container. 
        model.Add(sum([l_rot[i] * w_rot[i] * h_rot[i] * u[i] for i in range(nr)]) <= L * W * H)

        # weight constraint
        # The constraint ensures that the total weight of the selected items does not exceed the maximum capacity of the container
        model.Add(sum([wr[i] * u[i] for i in range(nr)]) <= M)

        # objective
        # This is our model objective to maximize the container space by packing as many items as possible.
        model.Maximize(sum([u[i] * l_rot[i] * w_rot[i] * h_rot[i] for i in range(nr)]))

        # solve model
        # creates an instance of the CpSolver class. This solver will be used to find a solution to the constraint 
        # programming model defined in the model.
        solver = cp_model.CpSolver()
        
        # sets the number of parallel workers (or threads) that the solver will use. By setting it to 8, we are 
        # instructing the solver to use 8 parallel workers. This can help speed up the solving process for complex problems.
        solver.parameters.num_search_workers = 8

        # calls the solve method on the solver to solve the model. 
        # The result of the solve method is stored in the status variable.
        status = solver.Solve(model)

        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            used = {i for i in range(nr) if solver.Value(u[i]) == 1}
            df = pd.DataFrame({
                'x': [solver.Value(x[i]) for i in used],
                'y': [solver.Value(y[i]) for i in used],
                'z': [solver.Value(z[i]) for i in used],
                'length': [l_rot[i] for i in used],
                'width': [w_rot[i] for i in used],
                'height': [h_rot[i] for i in used],
                'x2': [solver.Value(x2[i]) for i in used],
                'y2': [solver.Value(y2[i]) for i in used],
                'z2': [solver.Value(z2[i]) for i in used],
                'weight': [wr[i] for i in used],
                'itemid': [itemid[i] for i in used]
            })
            output = df.to_json(orient='records')
            return output
        else:
            return "Error finding the solution"

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error in finding the solution"
