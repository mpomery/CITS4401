import os
import shutil
from subprocess import call
import sys
import sqlite3
import string

SOURCE_PY = "./src"
SOURCE_WWW = "./www"
TARGET_DIR = "./target"
TARGET_WWW = "./target/www"
TEST_DIR = "./tests"

def usage():
    print("Make Script for SPACS")
    print("")
    print("Default/Error Behaviour: clean")
    print("")
    print("Options:")
    print("\tclean - clean up last build")
    print("\tcompile - create a build for deployment")
    print("\ttest - run all the tests over the application")
    print("\tdatabase - build a new database")
    print("\tpopulate - build a new database and populate it")

def clean_target_dir():
    # Clean up last compile
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)

def populate_target_dir():
    # Copy Files Across
    shutil.copytree(SOURCE_PY, TARGET_DIR)
    shutil.copytree(SOURCE_WWW, TARGET_WWW)
    build_database()

def build_database():
    pass

def populate_database():
    pass

# Clean up last compile
if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)

#Check for arguments
if len(sys.argv) != 2:
    usage()
    sys.exit(1)

if string.lower(sys.argv[1]) == "test":
    for file in os.listdir(TEST_DIR):
        print(file)
        clean_target_dir()
        populate_target_dir()
        populate_database()
        shutil.copyfile(TEST_DIR + "/" + file, TARGET_DIR + "/" + file)
        os.chdir(TARGET_DIR)
        os.system("python " + file)
        os.chdir("../")
elif string.lower(sys.argv[1]) == "compile":
    populate_target_dir()
elif string.lower(sys.argv[1]) == "database":
    build_database()
elif string.lower(sys.argv[1]) == "populate":
    build_database()
    populate_database()
else:
    print("Command not recognized. Cleaning up instead")

