import os
import shutil

def copy_files(src, dest, files):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for f in files:
        shutil.copy2(os.path.join(src, f), dest)