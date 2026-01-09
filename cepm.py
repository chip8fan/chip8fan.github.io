import json
import sys
import os
import shutil
if len(sys.argv) < 2:
    sys.argv.append("help")
os.chdir(os.path.dirname(os.path.realpath(__file__)).split("_internal")[0])
data = json.load(open("packages.json"))
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
    for file in os.listdir(os.getcwd() + "/bin"):
        print(file)
elif sys.argv[1] == "remove":
    if len(sys.argv) < 3:
        print("cepm remove [package_name]")
        sys.exit()
    os.remove(f"bin/{sys.argv[2]}")
    os.remove(f"src/{sys.argv[2]}.zip")
    shutil.rmtree(f"src/{sys.argv[2]}")
elif sys.argv[1] == "remove-all":
    if os.path.isdir("bin"):
        shutil.rmtree("bin")
    if os.path.isdir("src"):
        shutil.rmtree("src")
    os.mkdir("bin")
    os.mkdir("src")
elif sys.argv[1] == "update-package-list":
    os.remove("packages.json")
    os.system("wget https://raw.githubusercontent.com/chip8fan/chip8fan.github.io/refs/heads/main/packages.json")
elif sys.argv[1] == "help":
    file = open("cepm.py")
    lines = [line.rstrip().split('"')[1].split('"')[0] for line in file if "sys.argv[1] ==" in line]
    file.close()
    lines.pop()
    print("Options:")
    for line in lines:
        print(line)