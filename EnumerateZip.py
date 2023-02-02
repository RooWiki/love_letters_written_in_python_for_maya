## Enumerate, zip
control_list = ["ctrol_1","ctrol_2","ctrol_3","ctrol_4","ctrol_5","ctrol_6"]
jnt_list = ["jnt_1","jnt_2","jnt_3","jnt_4","jnt_5","jnt_6"]
grp_list = ["grp_1","grp_2","grp_3","grp_4","grp_5","grp_6"]

index = 0
for ctrl in control_list:
    print (ctrl, jnt_list[index], grp_list[index])
    index+=1
##
    
for index, obj in enumerate(control_list):        ## Es un For, pero   Recorriendo una lista   
    print (obj, jnt_list[index], grp_list[index])

##

for var in zip(control_list, jnt_list, grp_list): ## Es un For, pero   Emparejar variables
    print(var)
    
    
for ctrl, jnt, grp in zip(control_list, jnt_list, grp_list): ## Es un For, pero   Emparejar variables en diferentes listas
    print(ctrl, jnt, grp)
    
##