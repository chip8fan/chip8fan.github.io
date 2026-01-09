import os
os.chdir("src/stockfish/src")
os.system("make build")
os.rename("stockfish", "../../../bin/stockfish")