import os
import sys
import subprocess
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer

"""
# files = ['path/to/file1.ma'. '/path/to/file2.ma'.....]

# files = ['C:/Users/MON177/Pictures/SS_Dd/Script/ScriptPY/Monsta/Maya/screen_169a.ma', 'C:/Users/MON177/Pictures/SS_Dd/Script/ScriptPY/Monsta/Maya/screen_170.ma']

viewCmds.getSelection(name='BG')
# real work goes here, this is dummy
cmds.polyCube()  

"""
cmds.file('C:/Users/MON177/Pictures/SS_Dd/Script/ScriptPY/Monsta/Maya/screen_169a.ma', open=True, force=True)
cmds.workspace(r"C:\Users\MON177\Desktop\SH001e", openWorkspace=True)
cmds.loadPlugin('redshift')
current_layer = cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ) # Register the currently active render layer
cmds.editRenderLayerGlobals(currentRenderLayer='BG') # step to render layer
cmds.file(save=True)
# cmds.editRenderLayerGlobals(currentRenderLayer=current_layer) # Step back to the renderlayer you had active before running the script

maya.standalone.uninitialize()

