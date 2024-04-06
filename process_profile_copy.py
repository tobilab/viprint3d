# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import glob
import os
import sys
import shutil

git_mainlocation = r""+os.environ["GIT_VIPRINT3D_MAINLOCATION"]
git_main_path = r""+os.path.join(git_mainlocation,"bambulab_X1C_process_profiles")
orca_process_main_path = r""+os.environ["ORCA_PROCESS_PROFILES_FOLDER"]

def get_process_folder(filename):
    if not " - 0" in filename:
        return "Community and Tests"
    blocks = filename.split("-")
    return blocks[0].strip()


def transfer_profile_by_name(src_location, process_subfolder, profile_filename, target_location):
    try:
        for ending in [".json", ".info"]:
            full_old_path = os.path.join(src_location, profile_filename+ending)
            if os.path.exists(full_old_path):
                full_new_path = os.path.join(target_location, process_subfolder, profile_filename+ending)
                shutil.copy2(full_old_path,full_new_path)
        return 1
    except Exception as e:
        print(f"Failed copying filepath: {full_old_path} to location: {full_new_path}")
        return 0



# Search orca folder for process profiles
profiles = list(set([f.replace(".json","").replace(".info","") for f in os.listdir(orca_process_main_path)]))

# Create process material folders if not exist
materials = list(set([get_process_folder(profile) for profile in profiles]))

# Create material folders
for material_folder_path in [os.path.join(git_main_path, material.strip()) for material in materials]:
    if not os.path.exists(material_folder_path):
        os.makedirs(material_folder_path)

# Copy files
buff = [transfer_profile_by_name(orca_process_main_path, get_process_folder(profile_filename), profile_filename, git_main_path) for profile_filename in profiles]
print(f"Copyed {sum(buff)} of {len(profiles)} profiles found.")
