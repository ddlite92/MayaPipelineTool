import maya.cmds as cmds

def set_roughness(roughness_value):
    """Sets the roughness of the selected objects' materials."""

    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        print("No objects selected.")
        return

    for obj in selected_objects:
        # Get the shape node
        shapes = cmds.listRelatives(obj, shapes=True)
        if not shapes:
            continue
        shape = shapes[0]

        # Get the shading group
        shading_grps = cmds.listConnections(shape, type='shadingEngine')
        if not shading_grps:
            continue
        shading_grp = shading_grps[0]

        # Get the material
        materials = cmds.listConnections(shading_grp + ".surfaceShader")
        if not materials:
            continue
        material = materials[0]

        # Set the roughness attribute
        try:
            # Assuming the attribute is named "roughness"
            cmds.setAttr(material + ".refl_roughness", roughness_value) 
            print(f"Set roughness to {roughness_value} for material {material} on object {obj}")
        except Exception as e:
            print(f"Error setting roughness for {material} on {obj}: {e}")

# Example usage:
new_roughness = 0.5  # Replace with the desired roughness value
set_roughness(new_roughness)