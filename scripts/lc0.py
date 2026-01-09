import os
os.chdir(f"src/lc0")
os.system("./build.sh")
os.rename("build/release/lc0", f"../../bin/lc0")