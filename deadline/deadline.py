import os
import sys
import subprocess
import re
import subprocess

def submit_job(scene_file, start_frame, end_frame, output_folder):
    command = f"%DEADLINE_PATH%\deadlinecommand submitJob -plugin \"mayabatch.exe\" -frames \"{start_frame}-{end_frame}\" -name \"{scene_file}\" -priority 100 -inputFile \"{scene_file}\" -outputFile \"{output_folder}/{scene_file}\""
    subprocess.call(command, shell=True)

# Specify the file path, start frame, end frame, and output folder
scene_file = f"V:\PAPA\Work\Render\PAPA_Movie\REEL_01\3. INT. KOLUMPO TRAIN STATION - DAY\PAPA_Chapter_01_03_sh021a\PAPA_Chapter_01_03_sh021a_RENDER.ma"
start_frame = 101
end_frame = 101
output_folder = f"V:\PAPA\Output\3_OutputRender\PAPA_Movie\REEL_01\3. INT. KOLUMPO TRAIN STATION - DAY\PAPA_Chapter_01_03_sh019a\test"

submit_job(scene_file, start_frame, end_frame, output_folder)


"""

def submit_job(scene_file, start_frame, end_frame):
    # Replace with your desired Deadline command-line arguments
    command = f"deadlinecommand submitJob -name \"{scene_file}\" -plugin \"mayabatch.exe\" -frames \"{start_frame}-{end_frame}\" -priority 51 -outputFile \"V:\PAPA\Output\3_OutputRender\PAPA_Movie\REEL_01\3. INT. KOLUMPO TRAIN STATION - DAY\PAPA_Chapter_01_03_sh019a\test\""
    subprocess.call(command, shell=True)

# Replace with your scene files and their corresponding frame ranges
scene_files = [
    ("V:\PAPA\Work\Render\PAPA_Movie\REEL_01\3. INT. KOLUMPO TRAIN STATION - DAY\PAPA_Chapter_01_03_sh021a\PAPA_Chapter_01_03_sh021a_RENDER.ma", 101, 101),
    ("V:\PAPA\Work\Render\PAPA_Movie\REEL_01\3. INT. KOLUMPO TRAIN STATION - DAY\PAPA_Chapter_01_03_sh021\PAPA_Chapter_01_03_sh021_RENDER.ma", 101, 101),
    ("V:\PAPA\Work\Render\PAPA_Movie\REEL_01\3. INT. KOLUMPO TRAIN STATION - DAY\PAPA_Chapter_01_03_sh022b\PAPA_Chapter_01_03_sh022b_RENDER.ma", 101, 101)
]

for scene_file, start_frame, end_frame in scene_files:
    submit_job(scene_file, start_frame, end_frame)

"""