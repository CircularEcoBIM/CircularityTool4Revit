# Copyright (c) 2022 CircularEcoBIM, authors: Artur Tomczak <artomczak@gmail.com>, Ana Mestre <amestre@3drivers.pt >, Joana Fernandes <joanabfernandes@tecnico.ulisboa.pt>
# This file is part of CircularEcoBIM.


import json

translator = json.loads(IN[0])
# translator = json.loads( open(".\data\Material_mapping.json", "r").read() )
revit_names = IN[1]
# revit_names = [['C30/35','Galvanised steel','xyz'],['oak']]

# turn into list of lists:
if not isinstance(revit_names[0], list):
    revit_names = [revit_names] 

# TODO add pattern for steel /S\d\d\d/gi and concrete /C\d\d\/\d\d/gi

# to lower case:
for key, val in translator.items():
    low_val = []
    for x in val:
        low_val.append(x.lower())
    translator[key] = low_val 

# match names:
result_map = []
for list in revit_names:
    inner_list = []
    for name in list:
        match = False

        # look for direct match:
        for key, val in translator.items():
            if name.lower() in val:
                match = key
                break

        # consider parts of name:
        if not match:
            for key, val in translator.items():
                for v in val:
                    if v in name.lower():
                        match = key
                        break
                    else:
                        continue
                    break

        if match:
            inner_list.append(match)
        else:
            inner_list.append('Uncategorized')
    result_map.append(inner_list)

OUT = result_map

# check correctness:
# desired_map = [['Concrete','Steel','Uncategorized'],['Timber']]
# result=[]
# desired_map_flat = [elem for sublist in desired_map for elem in sublist]
# result_map_flat = [elem for sublist in result_map for elem in sublist]

# for i in range(len(result_map_flat)):
#     if result_map_flat[i] == desired_map_flat[i]:
#         result.append(True)
#     else:
#         result.append(False)
# print(result_map)
# print(result)
