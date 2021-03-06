from ui import *
from tests import *

bp=Board('player')
bc=Board('computer')
ai=MoveAlgorithm()
g=Game(bp,bc,ai)
ui=UI(g)
ui.start()

if __name__ == '__main__':
    unittest.main()