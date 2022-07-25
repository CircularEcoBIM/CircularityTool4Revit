
revit_materials = IN[0]

# turn into list of lists:
if not isinstance(revit_materials[0], list):
    revit_materials = [revit_materials] 


OUT = True