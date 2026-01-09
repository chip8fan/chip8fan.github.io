import os
os.chdir("src/Stockfish/src")
os.system("make build")
os.rename("stockfish", "../../../bin/stockfish")