import os
import shutil
import platform
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
if platform.system() == 'Linux':
    os.system(f"echo 'export PATH=\"{os.path.dirname(os.path.realpath(__file__)).split("/_internal")[0]}:$PATH\"' > ~/.bashrc")
    os.system(f"echo 'export PATH=\"{os.path.dirname(os.path.realpath(__file__)).split("_internal")[0]}/bin:$PATH\"' >> ~/.bashrc")
    os.system(f"source ~/.bashrc")
elif platform.system() == 'Darwin':
    os.system(f"echo 'export PATH=\"{os.path.dirname(os.path.realpath(__file__)).split("/_internal")[0]}:$PATH\"' > ~/.zshrc")
    os.system(f"echo 'export PATH=\"{os.path.dirname(os.path.realpath(__file__)).split("_internal")[0]}/bin:$PATH\"' >> ~/.zshrc")
    os.system(f"echo 'export PATH=\"/opt/homebrew/bin:$PATH\"' >> ~/.zshrc")
    os.system(f"source ~/.zshrc")