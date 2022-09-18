# Copyright (c) 2022 CircularEcoBIM, authors: Artur Tomczak <artomczak@gmail.com>, Ana Mestre <amestre@3drivers.pt >, Joana Fernandes <joanabfernandes@tecnico.ulisboa.pt>
# This file is part of CircularEcoBIM.


from copy import deepcopy

original_materials = IN[0]
materials = IN[1]
volumes = IN[2]
steel_concrete_ratio = IN[3]

new_materials = deepcopy(materials)
org_materials = deepcopy(original_materials)
new_volumes = deepcopy(volumes)

for i in range(len(materials)):
    for j in range(len(materials[i])):
        if materials[i][j] == "Concrete":
            new_volumes[i][j] = volumes[i][j] * (1-steel_concrete_ratio)
            if "Steel" in materials[i]:
                steel_id = materials[i].index("Steel")
                new_volumes[i][steel_id] = volumes[i][j]*steel_concrete_ratio
            else:
                new_materials[i].append("Steel")
                new_volumes[i].append(volumes[i][j]*steel_concrete_ratio)
                org_materials[i].append("<added Steel>")

OUT = [new_materials, new_volumes, org_materials]