import os
import subprocess
os.chdir("src/draw-engine")
subprocess.run("python3 install.py".split(), input=input("Engine Path: ").encode("utf-8"))
if os.path.isdir("../../bin/draw-engine") == False:
    os.mkdir("../../bin/draw-engine")
os.rename("draw-engine", "../../bin/draw-engine/draw-engine")
os.rename("_internal", "../../bin/draw-engine/_internal")