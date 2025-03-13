import os
import sys
import subprocess
import time
import datetime
import re

# B = {}
def modification_date_time(file_name):
    time = os.path.getmtime(file_name)
    return datetime.datetime.fromtimestamp(time)


"""Configure blend files"""
blendfiles = []
patern = ""
for current_dir, _, files in os.walk("."):
    for f in sorted(files):
        if (
            not f.endswith(".blend1")
            and not ".2021" in f
            and not ".2022" in f
            and not ".2023" in f
        ):
            f_relpath = os.path.join(current_dir, f)
            f_abspath = os.path.abspath(f_relpath)
            blendfiles.append(f_abspath)

print("------------")


"""Script for running Second"""
for blendfile in sorted(blendfiles):
    if sys.platform.startswith("win32"):
        ''''win_remove_beauty = (
            'C:\\blender\\blender.exe -b "%s"' % blendfile + " -y -P adjust_BG.py"
        )'''
        win_cgru = 'C:\\blender\\blender.exe -b "%s"' % blendfile + " -y -P cgru_submit.py"
        # win_render = 'C:\\blender\\blender.exe -b "%s"' % blendfile + " -y -P settings.py"
        # subprocess.run(r'C:\WINDOWS\system32\cmd.exe /C "%s"' % win_remove_beauty)
        subprocess.run(r'C:\WINDOWS\system32\cmd.exe /C "%s"' % win_cgru)

    elif sys.platform.startswith("linux"):
        '''adjust_CH = (
            '/opt/cgru/software_setup/start_blender.sh -b "%s"' % blendfile
            + " -y -P adjust_CH.py "
        )'''
        cgru = (
            '/opt/cgru/software_setup/start_blender.sh -b "%s"' % blendfile
            + " -y -P cgru_submit.py "
        )

        subprocess.run(cgru, shell=True)
        # print(command)

