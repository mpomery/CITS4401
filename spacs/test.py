import os
import shutil
from subprocess import call

SOURCE_PY = "./src"
TARGET_DIR = "./target"
TEST_DIR = "./tests"

def clean_target_folder():
    # Clean up last compile
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    
    # Copy Files Across
    shutil.copytree(SOURCE_PY, TARGET_DIR)

for file in os.listdir(TEST_DIR):
    print(file)
    clean_target_folder()
    shutil.copyfile(TEST_DIR + "/" + file, TARGET_DIR + "/" + file)
    os.chdir(TARGET_DIR)
    os.system("python " + file)
    os.chdir("../")