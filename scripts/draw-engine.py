import os
import subprocess
import shutil
os.chdir("src/draw-engine")
subprocess.run("python3 install.py".split(), input=input("Engine Path: ").encode("utf-8"))
if os.path.isdir("../../bin/draw-engine"):
    shutil.rmtree("../../bin/draw-engine")
os.mkdir("../../bin/draw-engine")
os.rename("draw-engine", "../../bin/draw-engine/draw-engine")
os.rename("_internal", "../../bin/draw-engine/_internal")
subprocess.run("python3 install_fast.py".split(), input=input("Engine Path: ").encode("utf-8"))
if os.path.isdir("../../bin/drawmaster"):
    shutil.rmtree("../../bin/drawmaster")
os.mkdir("../../bin/drawmaster")
os.rename("drawmaster", "../../bin/drawmaster/drawmaster")
os.rename("_internal", "../../bin/drawmaster/_internal")