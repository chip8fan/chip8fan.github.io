import os
os.chdir("src/fairy-stockfish/src")
os.system("make build")
os.rename("stockfish", "../../../bin/fairy-stockfish")