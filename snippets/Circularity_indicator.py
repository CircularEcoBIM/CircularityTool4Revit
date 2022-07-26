
elements = IN[0]

# turn into list of lists:
if not isinstance(elements[0], list):
    elements = [elements] 

result = []

volumes = [el[4] for el in elements]

#replace nans with -1
volumes = [-1 if x == '' else x for x in volumes]

max_volume = max(volumes)

for v in volumes:
    if v>0:
        result.append(v/max_volume)
    else:
        result.append(-1)

# OUT = result
OUT = result