# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import glob
import os
import shutil


def get_viprint3d_filamentprofile(filename, sep, num_seps):
    blocks = filename.split(sep)
    if len(blocks) == int(num_seps+1):
        return filename
    else:
        return False


def transfer_profile_by_name(src_location, material, profile_filename, target_location):
    try:
        for ending in [".json", ".info"]:
            if os.path.exists(os.path.join(src_location, profile_filename+ending)):
                shutil.copy2(os.path.join(src_location, profile_filename+ending),
                             os.path.join(target_location, material, profile_filename+ending))
        return 1
    except Exception as e:
        print(
            f"Failed copying filepath: {os.path.join(orca_filament_main_path,new_profile+ending)} to location: {os.path.join(git_main_path,material,new_profile+ending)}")
        return 0


git_main_path = r"C:\Git\viprint3d_public\bambulab_X1C_filament_profiles"
orca_filament_main_path = r"C:\Users\wagne\AppData\Roaming\OrcaSlicer\user\3471617518\filament"

material_folders = [el for el in os.listdir(
    git_main_path) if el.startswith("Material_")]

materials = {material_name.split("_")[-1]: {}
             for material_name in material_folders}

# Notation: Material - Colorcode - Nozzlediameter - Brand
num_seperators = 3
seperator = "-"

# Search orca folder for materials
profiles = list(set([d.split(".")[0] for d in os.listdir(orca_filament_main_path) if os.path.isfile(
    os.path.join(orca_filament_main_path, d)) and get_viprint3d_filamentprofile(d, seperator, num_seperators)]))

# Create material folders if not exist
materials = list(set([profile.split(seperator)[0] for profile in profiles]))
for material_folder_path in [os.path.join(git_main_path, material.strip()) for material in materials]:
    if not os.path.exists(material_folder_path):
        os.makedirs(material_folder_path)

buff = [transfer_profile_by_name(orca_filament_main_path, profile_filename.split(
    seperator)[0].strip(), profile_filename, git_main_path) for profile_filename in profiles]
print(f"Copyed {sum(buff)} of {len(profiles)} profiles found.")
