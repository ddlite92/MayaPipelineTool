import maya.cmds as cmds

def change_light_to_area():
    """
    Changes the selected light to an area light with the specified settings.
    """

    # Get selected light
    selected_lights = cmds.ls(selection=True)

    if not selected_lights:
        print("No spotlights selected.")
        return

    for light in selected_lights:
        # Change light type to area light
        #cmds.setAttr(light + "Shape" + ".lightType", 0)  # 2 represents area light

        # Set intensity and exposure
        cmds.setAttr(light + ".intensity", 21) 
        cmds.setAttr(light + ".SAMPLINGOVERRIDES_shadowSamplesScale", 10)
        cmds.setAttr(light + ".reflectionRayContributionScale", 1)
        #cmds.setAttr(light + ".exposure", 1)

        # Set area shape to sphere
        #cmds.setAttr(light + ".areaShape", 2)  # 1 represents sphere

        # Disable visible shape
        #cmds.setAttr(light + ".displayHandle", 0)
        #cmds.setAttr(light + ".areaVisibleInRender", 0)


change_light_to_area()