import maya.cmds as cmds
import os

def export_selected_as_alembic_to_scene_folder_named():
    """
    Exports the currently selected object(s) as an Alembic cache to the same
    folder as the currently open Maya scene file, using the time slider's
    start and end frames for the export range. The Alembic file will be
    named after the selected object(s) and include the start and end frames.
    If multiple objects are selected, the filename will be based on the
    first selected object.
    """
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("No objects selected for export.")
        return

    scene_path = cmds.file(query=True, sceneName=True)
    if not scene_path:
        cmds.warning("Scene not saved. Please save your scene first.")
        return

    scene_folder = os.path.dirname(scene_path)

    # Get the start and end frames from the time slider
    start_frame = int(cmds.playbackOptions(query=True, minTime=True))
    end_frame = int(cmds.playbackOptions(query=True, maxTime=True))

    # Use the name of the first selected object as the base filename
    object_name = selection[0]
    output_filename = f"{object_name}_{start_frame}_{end_frame}.abc"
    # output_filename = f"{object_name}.abc"
    # output_filename = f"CAM_{start_frame}_{end_frame}.abc"
    # output_path = os.path.join(scene_folder, output_filename).replace('\\', '/')
    fxBlender_path = os.path.join(scene_folder, 'FX_BLENDER', output_filename).replace('\\', '/')
    dome_path = os.path.join(scene_folder, 'FX_BLENDER', 'DOME', output_filename).replace('\\', '/')
    core_path = os.path.join(scene_folder, 'FX_BLENDER', 'CORE', output_filename).replace('\\', '/')
    transform_path = os.path.join(scene_folder, 'FX_BLENDER', 'TRANSFORMATION', output_filename).replace('\\', '/')

    root_nodes = ""
    for item in selection:
        root_nodes += f" -root |{item}"

    # Build the AbcExport command with the dynamic output filename and time range
    abc_command_dome = f'-frameRange {start_frame} {end_frame} -dataFormat ogawa{root_nodes} -file "{dome_path}"'
    abc_command_core = f'-frameRange {start_frame} {end_frame} -dataFormat ogawa{root_nodes} -file "{core_path}"'
    abc_command_transform = f'-frameRange {start_frame} {end_frame} -dataFormat ogawa{root_nodes} -file "{transform_path}"'
    abc_command_fxBlender = f'-frameRange {start_frame} {end_frame} -dataFormat ogawa{root_nodes} -file "{fxBlender_path}"'

    try:
        cmds.AbcExport(jobArg=abc_command_dome)
        cmds.AbcExport(jobArg=abc_command_core)
        cmds.AbcExport(jobArg=abc_command_transform)
        cmds.AbcExport(jobArg=abc_command_fxBlender)
        print(f"Successfully exported '{object_name}' (frames {start_frame}-{end_frame}) to:")
        print(f"  - DOME: {dome_path}")
        print(f"  - CORE: {core_path}")
        print(f"  - TRANSFORMATION: {transform_path}")
    except Exception as e:
        cmds.error(f"Error during Alembic export: {e}")

export_selected_as_alembic_to_scene_folder_named()

# Example usage:
# 1. Set the desired start and end frames in your Maya time slider.
# 2. Select the camera or object you want to export in the Maya viewport.
# 3. Run this script.


