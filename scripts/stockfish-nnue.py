import os
import sys
directory = sys.argv[1].split(".zip")[0]
os.chdir(f"src/{directory}/src")
os.system("make build")
os.rename("stockfish", f"../../../bin/{directory}")