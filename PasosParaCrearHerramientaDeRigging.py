# Obtener la seleccion del usuario
# Verificar si hay o no hay seleccion
# Verificar la seleccion 
# Enviar mensaje de warning

# Si hay seleccion, obtener la cantidad total de joints en la cadena

# Crear un control para cada joing
# Orientar el control en el eje x
# Freezear y limpiar historial del control
# crear un grupo offset para cada control
# Emparentar el control a su offset

# Obtener la posicion de cada joint
# mover el offset a la posicion del joint
# Orientar el offset con la orientacion del joint
# Parent contraint del control al joint

# Emparentar el offset del control siguiente con el anterior


import maya.cmds as cmds

selected = cmds.ls(selection = True)
if len(selected)==0:
    cmds.warning("No has seleccionado ningun objeto, selecciona un objeto")
elif len(selected)>1:
    cmds.warning("Por favor selecciona SOLO UN objeto")
else:
    if cmds.objectType(selected[0])!="joint":
        cmds.warning("Por favor selecione un joint")
    else:
        cmds.select(selected[0], hi=True)
        all_joints = cmds.ls(selection=True)
        joints_number = len(all_joints)
        
        control_list = []
        offset_list = []
        
        for i in range (joints_number-1):
            control = cmds.circle(name=all_joints[i]+"_ctrl") 
            cmds.rotate(0,90,0, control[0])
            cmds.scale(2,2,2, control[0])
            
            cmds.makeIdentity(apply=True)
            cmds.DeleteHistory()
            
            offset_grp = cmds.group(name = control[0]+"_offset", empty=True)
            cmds.parent(control[0], offset_grp)
            
            joint_position = cmds.xform(all_joints[i], query=True, translation=True, worldSpace=True)
            cmds.xform(offset_grp, translation=joint_position)
            
            orient_cons = cmds.orientConstraint(all_joints[i], offset_grp)
            cmds.delete(orient_cons)
            
            cmds.parentConstraint(control[0],all_joints[i])
            
            control_list.append(control[0])
            offset_list.append(offset_grp)
        for i in range(joints_number-2):
            cmds.parent(offset_list[i+1], control_list[i])
            