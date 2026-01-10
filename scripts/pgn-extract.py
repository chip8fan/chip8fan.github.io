import os
os.chdir("src/pgn-extract")
os.system("make")
os.rename("pgn-extract", "../../bin/pgn-extract")