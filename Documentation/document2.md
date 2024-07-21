### Overview
The packing_3d_fragility function solves a 3D bin packing problem with an additional constraint on item fragility using Google's OR-Tools. The goal is to maximize the utilization of a truck's space by efficiently packing items of varying dimensions, weights, and fragility levels. This function allows for the rotation of items and ensures that constraints such as weight capacity, no-overlap, and fragility are maintained.

### Detailed Explanation

The whole code is same except the part in the constraints. To see that got to [Basic packing](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document1.md).

##### Fragility Constraints
```
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

            total_weight_above.append(wr[j] * above)
    
    model.Add(weight_above == sum(total_weight_above))
    model.Add(weight_above <= fr[i])
```
* Ensures that the total weight of items above a fragile item does not exceed its fragility limit.

### Note:
In addition to basic packing of the items we have included a file called fragility_packing. The main difference between the two is that one is only run once but the fragility_packing one is runned multiple times by reducing the dimensions of the container. The fragility_packing gives somewhat better result than the packing_3d_fragility code.

Next go to [Visualisation](https://github.com/codechiefVignesh/bin_packing_iitm/blob/main/Documentation/document3.md).
