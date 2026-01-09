import os
import shutil
if os.path.isdir("_internal"):
    shutil.rmtree("_internal")
    os.remove("cepm")
os.system("pyinstaller cepm.py")
os.chdir("dist/cepm")
os.system("mv * ../..")
os.chdir("../..")
shutil.rmtree("build")
shutil.rmtree("dist")
os.remove("cepm.spec")