import json
import sys
import os
import shutil
os.chdir(os.path.dirname(os.path.realpath(__file__)).split("_internal")[0])
data = json.load(open("packages.json"))
if sys.argv[1] == "install":
    os.chdir("src")
    if len(sys.argv) == 3:
        os.system(f"gh release download --archive zip --clobber -R {str(data[sys.argv[2]]).split('https://github.com/')[1]}")
    elif len(sys.argv) == 4:
        os.system(f"gh release download {sys.argv[3]} --clobber --archive zip -R {str(data[sys.argv[2]]).split('https://github.com/')[1]}")
    most_recent_zip = None
    most_recent_time = 0
    for zip in os.scandir(os.getcwd()):
        if zip.name.endswith(".zip"):
            modified_time = zip.stat().st_mtime_ns
            if modified_time > most_recent_time:
                most_recent_time = modified_time
                most_recent_zip = zip.name
    if os.path.isdir(most_recent_zip.replace(".zip", "")):
        shutil.rmtree(most_recent_zip.replace(".zip", ""))
    os.system(f"unzip {most_recent_zip}")
    os.chdir("..")
    os.system(f"python3 scripts/{sys.argv[2]}.py {most_recent_zip}")
elif sys.argv[1] == "install-dev":
    os.chdir("src")
    directory = str(data[sys.argv[2]]).split("/")[-1]
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    os.system(f"git clone {data[sys.argv[2]]}.git")
    os.chdir("..")
    os.system(f"python3 scripts/{sys.argv[2]}.py {directory}")
elif sys.argv[1] == "list-versions":
    os.system(f"gh release list --limit {sys.maxsize} -R {str(data[sys.argv[2]]).split('https://github.com/')[1]}")
elif sys.argv[1] == "list-all":
    for key in json.load(open("packages.json")):
        print(key)
elif sys.argv[1] == "list-installed":
    for file in os.listdir(os.getcwd() + "/bin"):
        print(file)
elif sys.argv[1] == "remove":
    os.remove(f"bin/{sys.argv[2]}")
    os.remove(f"src/{sys.argv[2]}.zip")
    shutil.rmtree(f"src/{sys.argv[2]}")
elif sys.argv[1] == "remove-all":
    shutil.rmtree("bin")
    shutil.rmtree("src")
    os.mkdir("bin")
    os.mkdir("src")