import os
import shutil
from subprocess import call

TARGET_DIR = "./target"

if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)

