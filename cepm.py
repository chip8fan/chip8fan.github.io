import json
import sys
import os
import shutil
import requests
if len(sys.argv) < 2:
    sys.argv.append("help")
os.chdir(os.path.dirname(os.path.realpath(__file__)).split("_internal")[0])
data = json.load(open("packages.json"))
if os.path.isdir("bin") == False:
    os.mkdir("bin")
if os.path.isdir("src") == False:
    os.mkdir("src")
if sys.argv[1] == "install":
    os.chdir("src")
    if len(sys.argv) < 3:
        print("cepm install [package_name]")
        sys.exit()
    directory = str(data[sys.argv[2]]).split("/")[-1]
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    os.system(f"git clone {data[sys.argv[2]]}.git")
    os.chdir("..")
    os.system(f"python3 scripts/{sys.argv[2]}.py")
elif sys.argv[1] == "list-all":
    for key in json.load(open("packages.json")):
        print(key)
elif sys.argv[1] == "list":
    for file in os.listdir(os.getcwd() + "/src"):
        if file.lower() != ".ds_store":
            print(file.lower())
elif sys.argv[1] == "remove":
    if len(sys.argv) < 3:
        print("cepm remove [package_name]")
        sys.exit()
    if os.path.isfile(f"bin/{sys.argv[2]}"):
        os.remove(f"bin/{sys.argv[2]}")
    elif os.path.isdir(f"bin/{sys.argv[2]}"):
        shutil.rmtree(f"bin/{sys.argv[2]}")
    if os.path.isdir(f"src/{sys.argv[2]}"):
        shutil.rmtree(f"src/{sys.argv[2]}")
elif sys.argv[1] == "remove-all":
    if os.path.isdir("bin"):
        shutil.rmtree("bin")
    if os.path.isdir("src"):
        shutil.rmtree("src")
    os.mkdir("bin")
    os.mkdir("src")
elif sys.argv[1] == "update":
    with open("packages.json", "wb") as package_list:
        package_list.write(requests.get("https://raw.githubusercontent.com/chip8fan/chip8fan.github.io/refs/heads/main/packages.json").content)
    for key in json.load(open("packages.json")):
        with open(f"scripts/{key}.py", "wb") as script:
            script.write(requests.get(f"https://raw.githubusercontent.com/chip8fan/chip8fan.github.io/refs/heads/main/scripts/{key}.py").content)
elif sys.argv[1] == "help":
    file = open("cepm.py")
    lines = [line.rstrip().split('"')[1].split('"')[0] for line in file if "sys.argv[1] ==" in line]
    file.close()
    lines.pop()
    print("Options:")
    for line in lines:
        print(line)