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
    ['a', 'b', 'c'],
    # states
    ['Released','Unlocked', 'Alocked', 'Blocked', 'Error'],
    'Unlocked',
    lambda q: q in ['Released'],
    lambda q, a: {
        ('Unlocked', 'a'): 'Alocked',
        ('Unlocked', 'b'): 'Error',
        ('Unlocked', 'c'): 'Error',
        ('Alocked', 'a'): 'Alocked',
        ('Alocked', 'b'): 'Blocked',
        ('Alocked', 'c'): 'Released',
        ('Blocked', 'a'): 'Blocked',
        ('Blocked', 'b'): 'Blocked',
        ('Blocked', 'c'): 'Released',
        ('Released', 'a'): 'Error',
        ('Released', 'b'): 'Error',
        ('Released', 'c'): 'Error',
        ('Error', 'a'): 'Error',
        ('Error', 'b'): 'Error',
        ('Error', 'c'): 'Error',
    }[(q, a)]
)

print("input sequence is aaaabbbbc")
Enforcer.enforcer(copy.copy(phi), ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c'], 5)  
		
#
#
#
#
