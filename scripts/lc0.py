import os
import sys
import shutil
directory = sys.argv[1].split(".zip")[0]
if os.path.isdir(f"src/{directory}/libs"):
    os.chdir(f"src/{directory}/libs")
    shutil.rmtree("lczero-common")
    os.system("git clone https://github.com/LeelaChessZero/lczero-common.git")
    os.chdir("..")
else:
    os.chdir(f"src/{directory}")
os.system("./build.sh")
os.rename("build/release/lc0", f"../../bin/{directory}")