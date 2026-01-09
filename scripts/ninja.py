import os
os.chdir("src/ninja")
os.system("python3 configure.py --bootstrap")
os.rename("ninja", "../../bin/ninja")