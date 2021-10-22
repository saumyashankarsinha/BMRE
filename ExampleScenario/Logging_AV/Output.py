#######imports########################################
import sys
import os.path
sys.path.append("../")
from pathlib import Path
sourcedir=Path(__file__).resolve().parent.parent.parent
sourcedir=os.path.join(sourcedir, 'Source')
sys.path = [sourcedir] + sys.path
import Enforcer
import Automata
import copy
import random
import numpy
import time
import pandas as pd 





phi = Automata.DFA(
    # Input alphabets
    ['r', 'l', 'f', 's'],
    # states
    ['stop', 'start', 'right', 'left', 'forward', 'dead'],
    'start',
    lambda q: q in ['stop'],
    lambda q, a: {
        ('start', 'r'): 'right',
        ('start', 'l'): 'left',
        ('start', 'f'): 'forward',
        ('start', 's'): 'stop',
        ('right', 'r'): 'right',
        ('right', 'l'): 'left',
        ('right', 'f'): 'forward',
        ('right', 's'): 'stop',
        ('left', 'r'): 'right',
        ('left', 'l'): 'left',
        ('left', 'f'): 'forward',
        ('left', 's'): 'stop',
        ('forward', 'r'): 'right',
        ('forward', 'l'): 'left',
        ('forward', 'f'): 'forward',
        ('forward', 's'): 'stop',
        ('stop', 'r'): 'dead',
        ('stop', 'l'): 'dead',
        ('stop', 'f'): 'dead',
        ('stop', 's'): 'dead',
	('dead', 'r'): 'dead',
        ('dead', 'l'): 'dead',
        ('dead', 'f'): 'dead',
        ('dead', 's'): 'dead',
    }[(q, a)]
)

print("input sequence is rrllffs")
Enforcer.enforcer(copy.copy(phi), ['r', 'r', 'r', 'l', 'l', 'l', 'f', 'f', 'f', 's'], 6)  
		
#
#
#
#
