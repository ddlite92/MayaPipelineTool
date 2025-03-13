import maya.cmds as cmds

def change_obj_to_att():
    """
    Changes the selected light to an area light with the specified settings.
    """

    # Get selected light
    selected_obj = cmds.ls(selection=True)

    if not selected_obj:
        print("No spotlights selected.")
        return

    for obj in selected_obj:
        # Change light type to area light

        # Set intensity and exposure
        #cmds.setAttr(obj + ".refl_roughness", 0.75)
        cmds.setAttr(obj + ".displayMode", 0)  


change_obj_to_att()

'''
import maya.cmds as cmds

# Change the proxy file:
cmds.setAttr("Desolated_Road_Final:redshiftProxy111.fileName", "path/to/new/proxy.rs", type="string")

# Set display mode to "Preview Mesh":
cmds.setAttr("Desolated_Road_Final:redshiftProxy111.displayMode", 1)

# Set display percentage to 50%:
cmds.setAttr("Desolated_Road_Final:redshiftProxy111.displayPercentage", 50)

# Set material mode to "From Scene (assigned to placeholder)":
cmds.setAttr("Desolated_Road_Final:redshiftProxy111.materialMode", 1)

'''

'''
# def change_obj_to_att():

# Get selected light
selected_obj = cmds.ls(selection=True)

if not selected_obj:
    print("No spotlights selected.")
    return

selected_obj = cmds.ls(selection=True)
for obj in selected_obj:
    cmds.setAttr(obj + ".translate", 3, 3, 3)
    cmds.setAttr(obj + ".scale", 20, 20, 20)
    cmds.setAttr(obj + ".color", 1, 1, 0.3)
    cmds.setAttr(obj + ".intensity", 5)
    cmds.setAttr(obj + ".exposure", 0)
    cmds.setAttr(obj + ".areaBidirectional", 0)
    cmds.setAttr(obj + "Shape" + ".lightType", 1) 
    cmds.setAttr(obj + ".areaSpread", 1)
    cmds.setAttr(obj + ".SAMPLINGOVERRIDES_shadowSamplesScale", 100)
    cmds.setAttr(obj + ".aovLightGroup", "", type="string")
    cmds.editRenderLayerGlobals(currentRenderLayer="BG_Sim")
    cmds.editRenderLayerAdjustment(obj + ".intensity")
    cmds.editRenderLayerAdjustment(obj + ".areaBidirectional")   
    cmds.editRenderLayerAdjustment(obj + ".normalize")
    cmds.editRenderLayerAdjustment(obj + ".normalize", remove=True)
    area_spread = cmds.getAttr(obj + ".areaSpread")
    print(f"{obj}.areaSpread: {area_spread}")     

# change_obj_to_att()  


selected_obj = cmds.ls(selection=True)
for obj in selected_obj:
    cmds.setAttr(obj + ".aovLightGroup", "Ball_LIGHT", type="string")


'''