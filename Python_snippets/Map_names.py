
revit_names = IN[0]
# revit_names = [['C30/35','Galvanised steel','xyz'],['oak']]

# turn into list of lists:
if not isinstance(revit_names[0], list):
    revit_names = [revit_names] 

translator={
    'Concrete':['Concrete','C20/25','C25/30','C30/35','C40/50','reinforced','RC','aerated','pre-cast','in-situ','/C\d\d\/\d\d/gi'],
    'Steel':['Steel','alloy','S235','S275','S355','S420'],
    'Timber':['Timber','plywood','softwood','oak','pine','wood','lumber','MDF','OSB','parquet','laminate'],
    'Glass':['Glass','Glazing'],
    'Stone':['Stone','granite','limestone','marble ','slate'],
    'Ceramic':['Ceramic','Tile'],
    'Cement':['Cement','screed','fibre cement','CEM','Portland'],
    'AggregateSand':['Aggregate','Sand'],
    'Aluminium':['Aluminium'],
    'Asphalt':['Asphalt'],
    'Bitumen':['Bitumen'],
    'Clay':['Clay','Brick'],
    'Composites':['Composites'],
    'Copper':['Copper'],
    'Insulation':['Insulation','XPS','EPS','ETICS'],
    'Iron':['Iron'],
    'Lime':['Lime'],
    'Linoleum':['Linoleum'],
    'MandE':['MandE'],
    'Misc':['Misc'],
    'Paint':['Paint'],
    'Paper':['Paper','cardboard'],
    'Plaster':['Plaster','Gypsum','gypsumboard','plasterboard'],
    'Plastics':['Plastics','PVC','acrylic'],
    'Rubber':['Rubber'],
    'Sealants_adhesives_coatings':['Sealants_adhesives_coatings'],
    'Soil':['Soil'],
    'Vinyl':['Vinyl'],
    'Zinc':['Zinc'],
    'Uncategorised':['Uncategorised'],
}
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
