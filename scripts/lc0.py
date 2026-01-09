import os
os.chdir("src/lc0")
os.system("./build.sh")
os.rename("build/release/lc0", "../../bin/lc0")