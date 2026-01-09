import os
os.chdir("src/meson")
os.system("python3 packaging/create_zipapp.py")
os.rename("meson.pyz", "../../bin/meson")