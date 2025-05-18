import maya.cmds as cmds

# Enable the render layer:
cmds.editRenderLayerGlobals(currentRenderLayer="Shadow_Pokok")
cmds.setAttr("Shadow_Pokok.renderable", 1)

# Disable the render layer:
cmds.editRenderLayerGlobals(currentRenderLayer="Shadow_Pokok")
cmds.setAttr("Shadow_Pokok.renderable", 0)

# layer overide and edit:
cmds.editRenderLayerGlobals(currentRenderLayer="LightRay_Globe")
cmds.editRenderLayerAdjustment("Ring_Unmatte.matteAlpha")
cmds.setAttr ("Ring_Unmatte.matteAlpha", 1)


# select visibility_ctrl
select -r YonB_RS:visibility_ctrl ;
cmds.ls 

# select mesh outliner and subdivide
select -add Biker_Alien_RS1:Rifle_Papa_RS:Blaster_Gun_G ;
select -add Biker_Alien_RS1:Parang_Papa_RSRNfosterParent1 ;
select -add Biker_Alien_RS1:Papa_Biker_G ;
displaySmoothness -divisionsU 3 -divisionsV 3 -pointsWire 16 -pointsShaded 4 -polygonObject 3;

# export selection
ExportSelection;
file -force -options "v=0;" -typ "mayaAscii" -pr -es "V:/PAPA/Work/Render/PAPA_Movie/REEL_03/4. EXT. KACHAX CABIN SWAMP AREA - DAY/PAPA_Chapter_03_4_Sh045/char.ma";


# select visibility_ctrl (M), geometry High and break connection
select -r YonB_RS:visibility_ctrl ;
setAttr "YonB_RS:visibility_ctrl.Geometry" 0;
setAttr "YonB_RS:visibility_ctrl.Geometry" 1;
CBdeleteConnection "YonB_RS:visibility_ctrl.Geometry";



# ----------------------------------------------------------------- #

# Python equivalent of the MEL commands above
# MEL: # select visibility_ctrl
# Python:
cmds.select("YonB_RS:visibility_ctrl", replace=True)
print(cmds.ls(selection=True))  # Equivalent to cmds.ls

# MEL: # select mesh outliner and subdivide
# Python:
cmds.select(
    [
        "Biker_Alien_RS1:Rifle_Papa_RS:Blaster_Gun_G",
        "Biker_Alien_RS1:Parang_Papa_RSRNfosterParent1",
        "Biker_Alien_RS1:Papa_Biker_G",
    ],
    add=True,
)
cmds.displaySmoothness(
    divisionsU=3,
    divisionsV=3,
    pointsWire=16,
    pointsShaded=4,
    polygonObject=3,
)

# MEL: # export selection
# Python:
file_path = "V:/PAPA/Work/Render/PAPA_Movie/REEL_03/4. EXT. KACHAX CABIN SWAMP AREA - DAY/PAPA_Chapter_03_4_Sh045/char.ma"
cmds.file(
    force=True,
    options="v=0;",
    type="mayaAscii",
    preserveReferences=True,
    exportSelected=True,
    filename=file_path,
)
print(f"Exported selected objects to: {file_path}")

# MEL: # select visibility_ctrl (M), geometry High and break connection
# Python:
cmds.select("YonB_RS:visibility_ctrl", replace=True)
cmds.setAttr("YonB_RS:visibility_ctrl.Geometry", 0)
cmds.setAttr("YonB_RS:visibility_ctrl.Geometry", 1)
try:
    cmds.CBdeleteConnection("YonB_RS:visibility_ctrl.Geometry")
    print("Broke connection for YonB_RS:visibility_ctrl.Geometry")
except RuntimeError as e:
    print(f"Warning: Could not break connection for YonB_RS:visibility_ctrl.Geometry. Error: {e}")

# Disable the render layer (from your Python example):
cmds.editRenderLayerGlobals(currentRenderLayer="Shadow_Pokok")
cmds.setAttr("Shadow_Pokok.renderable", 0)
print("Disabled renderable for Shadow_Pokok render layer.")

# Layer override and edit (from your Python example):
cmds.editRenderLayerGlobals(currentRenderLayer="LightRay_Globe")
cmds.editRenderLayerAdjustment("Ring_Unmatte.matteAlpha")
cmds.setAttr("Ring_Unmatte.matteAlpha", 1)
print("Set Ring_Unmatte.matteAlpha to 1 in LightRay_Globe render layer.")

select -r char:Papazola_RS:button2 ;
sets -e -forceElement char:Papazola_RS:rsMaterial19SG;

REM --- Execute Python Script ---
echo Running Python script: "%python_script%"
"%mayapy_executable%" "%python_script%" "%scene_file%"

REM --- Check for Errors in Python Script (Optional) ---
if errorlevel 1 (
    echo Error occurred during Python script execution. Aborting render.
    exit /b 1
)