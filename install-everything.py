import os
import json
os.system("python3 install.py")
for key in json.load(open("packages.json")):
    os.system(f"cepm install-dev {key}")
os.system("cepm remove-all")