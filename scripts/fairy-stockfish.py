import os
os.chdir("src/Fairy-Stockfish/src")
os.system("make build")
os.rename("stockfish", "../../../bin/fairy-stockfish")