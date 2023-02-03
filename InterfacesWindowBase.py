import maya.cmds as cmds

# INTERFACE

window_name = "rigg_tool"
window_title = "Simple Rigg by RooWiki"
window_w = 200
window_h = 200

def create_window(): 
    if cmds.window(window_name, query=True, exists=True):
        cmds.deleteUI(window_name)
    cmds.window(window_name)
    cmds.window(window_name, edit=True, w=window_w, h=window_h, title=window_title)
    
    cmds.columnLayout("main_colum", w=window_w, h=window_h)
    cmds.rowLayout("row_layout", w=window_w, nc=6)
    
    cmds.button()


    
    cmds.showWindow(window_name)
    
create_window()