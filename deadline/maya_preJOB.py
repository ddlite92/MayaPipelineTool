import maya.cmds as cmds
import os

def control_render_layers(enable_layers=None, disable_layers=None):
    """
    Enables or disables legacy render layers based on layer names.
    Writes the available layers to a text file.

    Args:
        enable_layers (list, optional): List of layer names to enable.
        disable_layers (list, optional): List of layer names to disable.
    """

    # Get the Maya scene file path
    scene_file = cmds.file(query=True, sceneName=True)
    if not scene_file:
        print("Error: Scene file not saved. Cannot determine location.")
        return

    # Get the directory of the scene file
    scene_dir = os.path.dirname(scene_file)

    # Get a list of all legacy render layers
    all_layers = cmds.ls(type="renderLayer")

    # Write the available layers to a text file
    output_file = os.path.join(scene_dir, "render_layers.txt")
    with open(output_file, "w") as f:
        f.write("Available Legacy Render Layers:\n")
        for layer in all_layers:
            f.write(f"  - {layer}\n")

    print(f"Available render layers written to: {output_file}")

    if enable_layers:
        for layer in enable_layers:
            if layer in all_layers:
                cmds.editRenderLayerGlobals(currentRenderLayer=layer)
                cmds.setAttr(layer + ".renderable", True)
                print(f"Enabled render layer: {layer}")
            else:
                print(f"Warning: Layer '{layer}' not found.")

    if disable_layers:
        for layer in disable_layers:
            if layer in all_layers:
                cmds.editRenderLayerGlobals(currentRenderLayer=layer)
                cmds.setAttr(layer + ".renderable", False)
                print(f"Disabled render layer: {layer}")
            else:
                print(f"Warning: Layer '{layer}' not found.")

# Example Usage (Modify as needed)
# enable_layers = ["character_layer", "environment_layer"]
# disable_layers = ["debug_layer", "wireframe_layer"]

# control_render_layers(enable_layers=enable_layers, disable_layers=disable_layers)