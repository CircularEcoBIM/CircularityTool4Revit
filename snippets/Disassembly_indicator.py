
import json

parameters = IN[0]
# parameters = [[3,2,0,1],[2,3,1,0],[4,4,2,0]]

values = json.loads(IN[1])

# turn into list of lists:
if not isinstance(parameters[0], list):
    parameters = [parameters] 

dfd_ind = []

for el in parameters:
    if not el[0] or el[0] > 5:
        el[0] = 5
    d1 = values["Connection type"][str(int(el[0]))]
    
    if not el[1] or el[1] > 4:
        el[1] = 4
    d2 = values["Connection accessibility"][str(int(el[1]))]
    
    if not el[2] or el[2] > 3:
        el[2] = 3
    d3 = values["Crossings"][str(int(el[2]))]

    if not el[3] or el[3] > 4:
        el[3] = 4
    d4 = values["Form containment"][str(int(el[3]))]

    dfd_ind.append([d1,d2,d3,d4])

OUT = dfd_ind