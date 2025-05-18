import os
import json
import subprocess

def export_render_settings_standalone(maya_file_path, output_dir):
    """
    Exports the scene file path, filename, start frame, and end frame
    from a Maya file to a JSON file using mayapy.

    Args:
        maya_file_path (str): The full path to the Maya (.ma or .mb) file.
        output_dir (str): The directory where the JSON file will be saved.
    """
    output_filename = os.path.splitext(os.path.basename(maya_file_path))[0] + "_render_info.json"
    output_filepath = os.path.join(output_dir, output_filename)

    maya_file_path_raw = maya_file_path.replace("\\", "\\\\")
    output_filepath_raw = output_filepath.replace("\\", "\\\\")

    mayapy_command = [
        "mayapy",
        "-c",
        f"""
import maya.standalone
maya.standalone.initialize(name='python')
import maya.cmds as cmds
import json
import os

scene_path = r'{maya_file_path_raw}';
if not cmds.file(query=True, exists=True):
    print(f"Error (mayapy): Scene file not found: {{scene_path}}")
    maya.standalone.uninitialize()
    exit()

filename = os.path.basename(scene_path)
start_frame = int(cmds.playbackOptions(query=True, minTime=True))
end_frame = int(cmds.playbackOptions(query=True, maxTime=True))

data = {{
    "file_path": scene_path,
    "filename": filename,
    "start_frame": start_frame,
    "end_frame": end_frame
}};

try:
    with open(r'{output_filepath_raw}', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Success (mayapy): Wrote to C:\\\\Users\\\\MON177\\\\Pictures\\\\SS_Dd\\\\Script\\\\ScriptPY\\\\Monsta\\\\Maya\\\\deadline\\\\submission\\\\Maya\\\\Scripts\\\\temp_maya_export\\\\{os.path.basename(output_filepath_raw)}")
except Exception as e:
    print(f"Error (mayapy) writing JSON: {{e}}")

maya.standalone.uninitialize()
"""
    ]

    try:
        result = subprocess.run(mayapy_command, capture_output=True, text=True, check=True)
        if result.stderr and "Qt WebEngine" not in result.stderr:
            print(f"mayapy had errors for {maya_file_path}:")
            print(result.stderr)
        print(result.stdout) # Print stdout for more info
        print(result.stderr) # Print stderr for more info
        print(f"Successfully attempted export for: {maya_file_path} -> {output_filepath}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing mayapy for {maya_file_path}:")
        print(f"Command: {e.cmd}")
        print(f"Return Code: {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("Error: 'mayapy' executable not found.")

def process_directory(directory_path, output_directory):
    """
    Processes all Maya files containing 'render' in the given directory.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    print(f"Processing directory: {directory_path}")
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path) and item.lower().endswith(('.ma', '.mb')) and "render" in item.lower():
            export_render_settings_standalone(item_path, output_directory)
        elif os.path.isdir(item_path):
            print(f"Skipping subdirectory: {item_path}")

if __name__ == "__main__":
    maya_directory_root = r"V:\PAPA\Work\Render\PAPA_Movie\REEL_01\16. FLASHBACK - INT. POWER STATION - DAY"
    output_directory = r"C:\Users\MON177\Pictures\SS_Dd\Script\ScriptPY\Monsta\Maya\deadline\submission\Maya\Scripts\temp_maya_export"  # You'll need this for the actual export

    if not os.path.exists(output_directory):
        os.makedirs(output_directory) #create the directory

    specific_folders = [
        "PAPA_Chapter_01_016_sh030",
        "PAPA_Chapter_01_016_sh031a",
        # Add other folders back if needed
    ]

    for folder in specific_folders:
        folder_path = os.path.join(maya_directory_root, folder)
        if os.path.isdir(folder_path):
            process_directory(folder_path, output_directory)
        else:
            print(f"Warning: Folder not found: {folder_path}")