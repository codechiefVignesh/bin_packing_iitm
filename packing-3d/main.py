from ortools.sat.python import cp_model
from io import StringIO
import pandas as pd
import numpy as np

#---------------------------------------------------
# data
#---------------------------------------------------

def packing_3d(truck_dim,items):
    data = '''
    itemid    length   width   height  weight  value  
    1           11       2       1       48      1    
    2            5       4       2       9       1    
    3           12       5       2        6      1    
    4           10       7       1        2      1    
    5            2       4       2       33      1    
    6           10       1       5       13      1    
    7           12       7       2       29      1    
    8           10       5       1       49      1    
    '''

    df = pd.read_table(StringIO(data), sep='\s+')
    print("Input data")
    print(df)

    L = 12
    W = 8
    H = 5
    M = 400

    print(f"Truck's Dimension Length:{L} Width:{W} Height:{H} Maximum Capacity:{M}")

    #---------------------------------------------------
    # derived data
    # expand to individual items
    #---------------------------------------------------

    l0 = df["length"].to_numpy()
    b0 = df['width'].to_numpy()
    h0 = df['height'].to_numpy()
    w0 = df['weight'].to_numpy()
    v0 = df['value'].to_numpy()
    indx0 = np.arange(np.size(l0))

    n = len(l0)
    print(f"Number of individual items: {n}")

    #---------------------------------------------------
    # create rotated items
    # by duplicating
    #---------------------------------------------------

    # six possible rotation of a 3d object
    l_rot = np.concatenate((l0, l0, b0, b0, h0, h0))
    w_rot = np.concatenate((b0, h0, l0, h0, b0, l0))
    h_rot = np.concatenate((h0, b0, h0, l0, l0, b0))


    wr = np.tile(w0, 6)
    vr = np.tile(v0, 6)
    indxr = np.tile(indx0, 6)
    itemid = np.tile(df['itemid'].to_numpy(), 6)

    nr = 6 * n
    print(f"Number of individual items (after adding rotations): {nr}")

    #---------------------------------------------------
    # or-tools model
    #---------------------------------------------------

    model = cp_model.CpModel()

    #
    # variables
    #

    # u[i] : item i is used
    u = [model.NewBoolVar(f"u{i}") for i in range(nr)]


    # x[i], y[i], z[i] : location of item i
    x = [model.NewIntVar(0, L, f"x{i}") for i in range(nr)]
    y = [model.NewIntVar(0, W, f"y{i}") for i in range(nr)]
    z = [model.NewIntVar(0, H, f"z{i}") for i in range(nr)]

    # l[i], w[i], h[i] : dimensions of item i
    lx = [model.NewIntVar(0, L, f"lx{i}") for i in range(nr)]
    ly = [model.NewIntVar(0, W, f"ly{i}") for i in range(nr)]
    lz = [model.NewIntVar(0, H, f"lz{i}") for i in range(nr)]

    # x2[i], y2[i], z2[i] : upper limit of interval variable
    x2 = [model.NewIntVar(0, L, f"x2{i}") for i in range(nr)]
    y2 = [model.NewIntVar(0, W, f"y2{i}") for i in range(nr)]
    z2 = [model.NewIntVar(0, H, f"z2{i}") for i in range(nr)]

    # interval variables
    xival = [model.NewIntervalVar(x[i], lx[i], x2[i], f"xival{i}") for i in range(nr)]
    yival = [model.NewIntervalVar(y[i], ly[i], y2[i], f"yival{i}") for i in range(nr)]
    zival = [model.NewIntervalVar(z[i], lz[i], z2[i], f"zival{i}") for i in range(nr)]


    #
    # constraints
    #
    # The main idea here is: if an item is not selected, make its
    # length, width, and height zero.

    # u[i] = 0  ==> lx[i]=ly[i]=lz[i]=0
    # u[i] = 1  ==> lx[i]=l_rot[i], ly[i]=w_rot[i], lz[i]=h_rot[i]
    for i in range(nr):
        model.Add(lx[i] == l_rot[i] * u[i])
        model.Add(ly[i] == w_rot[i] * u[i])
        model.Add(lz[i] == h_rot[i] * u[i])

    # only one of the six possible rotations can be used
    for i in range(n):
        model.Add(sum(u[i + j * n] for j in range(6)) <= 1)

    # no overlap in 3D.
    for i in range(nr):
        for j in range(i+1,nr):
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

            model.AddBoolOr([c1,c2,c3,c4,c5,c6])


    # extra: this constraint helps performance enormously
    model.Add(sum([l_rot[i] * w_rot[i] * h_rot[i] * u[i] for i in range(nr)]) <= L * W * H)

    # weight constraint
    model.Add(sum([wr[i] * u[i] for i in range(nr)]) <= M)

    # objective
    model.Maximize(sum([u[i] * l_rot[i] * w_rot[i] * h_rot[i] for i in range(nr)]))

    # print("check5")

    #
    # solve model
    #
    solver = cp_model.CpSolver()
    # log does not work inside a Jupyter notebook
    # print("check5a")
    solver.parameters.log_search_progress = True
    solver.parameters.num_search_workers = 8
    # print("check5b")
    rc = solver.Solve(model)   
    # print("check5c")
    print(f"return code:{rc}")
    print(f"status:{solver.StatusName()}")
    print()
    print(solver.ResponseStats())
    print()

    # print("check6")
    #
    # report solution
    #
    if rc == cp_model.OPTIMAL or rc == cp_model.FEASIBLE:
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
            'value': [vr[i] for i in used],
            'weight': [wr[i] for i in used],
            'itemid': [itemid[i] for i in used]
        })
        print(df)
        return df
    else:
        return "Error finding the solution"