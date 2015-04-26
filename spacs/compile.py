import os
import shutil

SOURCE_PY = "./src"
SOURCE_WWW = "./www"
TARGET_DIR = "./target"
TARGET_WWW = "./target/www"

# Clean up last compile
if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)

# Make target folder
#os.mkdir(TARGET_DIR)

# Copy Files Across
shutil.copytree(SOURCE_PY, TARGET_DIR)
shutil.copytree(SOURCE_WWW, TARGET_WWW)
