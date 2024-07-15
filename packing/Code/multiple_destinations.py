from ortools.linear_solver import pywraplp
import pandas as pd
import numpy as np
import json

def packing_3d(data):
    # Input data format
    truck_data = data["truck"]
    items = data["items"]

    df = pd.DataFrame.from_dict(items)
    
    L = truck_data["length"]
    W = truck_data["width"]
    H = truck_data["height"]
    M = truck_data["maximum_capacity"]

    # Derived data from the items
    l0 = df["length"].to_numpy()
    b0 = df['width'].to_numpy()
    h0 = df['height'].to_numpy()
    w0 = df['weight'].to_numpy()
    loc0 = df["location"].to_numpy()

    n = len(l0)

    # Creating duplicate items dimensions and properties to represent all 6 possible rotations of the item in 3D space.
    l_rot = np.concatenate((l0, l0, b0, b0, h0, h0))
    w_rot = np.concatenate((b0, h0, l0, h0, b0, l0))
    h_rot = np.concatenate((h0, b0, h0, l0, l0, b0))

    wr = np.tile(w0, 6)
    itemid = np.tile(df['itemid'].to_numpy(), 6)
    loc = np.tile(loc0, 6)

    nr = 6 * n

    # MIP model
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variables
    u = [solver.BoolVar(f"u{i}") for i in range(nr)]
    x = [solver.IntVar(0, L, f"x{i}") for i in range(nr)]
    y = [solver.IntVar(0, W, f"y{i}") for i in range(nr)]
    z = [solver.IntVar(0, H, f"z{i}") for i in range(nr)]
    lx = [solver.IntVar(0, L, f"lx{i}") for i in range(nr)]
    ly = [solver.IntVar(0, W, f"ly{i}") for i in range(nr)]
    lz = [solver.IntVar(0, H, f"lz{i}") for i in range(nr)]
    x2 = [solver.IntVar(0, L, f"x2{i}") for i in range(nr)]
    y2 = [solver.IntVar(0, W, f"y2{i}") for i in range(nr)]
    z2 = [solver.IntVar(0, H, f"z2{i}") for i in range(nr)]

    # Constraints
    for i in range(nr):
        solver.Add(lx[i] == l_rot[i] * u[i])
        solver.Add(ly[i] == w_rot[i] * u[i])
        solver.Add(lz[i] == h_rot[i] * u[i])

    for i in range(n):
        solver.Add(solver.Sum([u[i + j * n] for j in range(6)]) <= 1)

    for i in range(nr):
        for j in range(i+1, nr):
            solver.Add(x2[i] <= x[j] + (1 - u[i]) * L + (1 - u[j]) * L)
            solver.Add(x2[j] <= x[i] + (1 - u[i]) * L + (1 - u[j]) * L)
            solver.Add(y2[i] <= y[j] + (1 - u[i]) * W + (1 - u[j]) * W)
            solver.Add(y2[j] <= y[i] + (1 - u[i]) * W + (1 - u[j]) * W)
            solver.Add(z2[i] <= z[j] + (1 - u[i]) * H + (1 - u[j]) * H)
            solver.Add(z2[j] <= z[i] + (1 - u[i]) * H + (1 - u[j]) * H)

    for i in range(nr):
        for j in range(i + 1, nr):
            if loc[i] < loc[j]:
                solver.Add(x2[j] <= x[i])
                solver.Add(z2[j] <= z[i])
            elif loc[i] > loc[j]:
                solver.Add(x2[i] <= x[j])
                solver.Add(z2[i] <= z[j])

    solver.Add(solver.Sum([l_rot[i] * w_rot[i] * h_rot[i] * u[i] for i in range(nr)]) <= L * W * H)
    solver.Add(solver.Sum([wr[i] * u[i] for i in range(nr)]) <= M)

    solver.Maximize(solver.Sum([u[i] * l_rot[i] * w_rot[i] * h_rot[i] for i in range(nr)]))

    # Solve model
    status = solver.Solve()

    # Report solution
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        used = [i for i in range(nr) if u[i].solution_value() == 1]
        df_result = pd.DataFrame({
            'x': [x[i].solution_value() for i in used],
            'y': [y[i].solution_value() for i in used],
            'z': [z[i].solution_value() for i in used],
            'length': [l_rot[i] for i in used],
            'width': [w_rot[i] for i in used],
            'height': [h_rot[i] for i in used],
            'x2': [x2[i].solution_value() for i in used],
            'y2': [y2[i].solution_value() for i in used],
            'z2': [z2[i].solution_value() for i in used],
            'weight': [wr[i] for i in used],
            'itemid': [itemid[i] for i in used],
            'location':[loc[i] for i in used]
        })
        output = df_result.to_json(orient='records')
        print(df_result)
        return output
    else:
        return "Error finding the solution"