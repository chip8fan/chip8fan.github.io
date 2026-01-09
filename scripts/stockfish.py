import os
os.chdir(f"src/stockfish/src")
os.system("make build")
os.rename("stockfish", f"../../../bin/stockfish")