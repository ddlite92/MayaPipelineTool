import sys
import os
import time
import subprocess

"""
- PathSaveFiles
- 
"""

PathSaveFiles = "V:\PAPA\Work\Render\PAPA_Movie\REEL_01\3. INT. KOLUMPO TRAIN STATION - DAY\PAPA_Chapter_01_03_sh001a\watchfolder"


def sumbit2deadline():
    FileName = "maya_job_info"
    JobInfo = PathSaveFiles + FileName + ".job"
    FileName = "maya_plugin_info"
    JobPlugIn = PathSaveFiles + FileName + ".job"
    FileName = "PAPA_Chapter_01_03_sh001a_RENDER"
    JobFile = PathSaveFiles + FileName + ".ma"
    command = "deadlinecommand" + " " + JobInfo + " " + JobPlugIn + " " + JobFile
    subprocess.run(command)

sumbit2deadline()