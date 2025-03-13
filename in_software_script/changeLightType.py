def change_light_type_and_settings(light_names):
     """
     Changes the light type to spot, sets intensity to 21, exposure to 1,
     and disables the visible shape for the specified lights.
     """
 
     for light_name in light_names:
         if cmds.objExists(light_name):
             # Change the light type to areaLight
            try:
                cmds.setAttr(light_name + "Shape" + ".lightType", 0)  # 2 corresponds to areaLight
            except RuntimeError as e:
                print(f"Error changing light type: {e}")
                return
 
                # Set intensity and exposure
                cmds.setAttr(light_name + ".intensity", 21)
                cmds.setAttr(light_name + ".exposure", 1)
    
                # Disable visible shape
                cmds.setAttr(light_name + ".displayHandle", 0)
                cmds.setAttr(light_name + ".areaVisibleInRender", 0)
    
                print(f"Updated settings for '{light_name}'.")
         else:
             print(f"Warning: Light '{light_name}' not found.")
 
 # Example usage:
light_names = ["Point_1", "Point_3", "Point_4", "Point_5", "Point_6", "Point_7", "Point_8", "Point_9", "Point_10", "Point_11"]  # Add your light names here
change_light_type_and_settings(light_names)