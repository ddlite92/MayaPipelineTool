import maya.cmds as cmds

# Enable the render layer:
cmds.editRenderLayerGlobals(currentRenderLayer="Shadow_Pokok")
cmds.setAttr("Shadow_Pokok.renderable", 1)

# Disable the render layer:
cmds.editRenderLayerGlobals(currentRenderLayer="Shadow_Pokok")
cmds.setAttr("Shadow_Pokok.renderable", 0)


# run w/o open
'''
import maya.cmds as cmds

# Your script code here (e.g., to modify a scene file)
cmds.file("path/to/your/scene.ma", open=True, force=True)

# ... your commands to modify the scene ...
cmds.file(save=True, force=True)

'''