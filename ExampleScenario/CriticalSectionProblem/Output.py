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
    ['t', 'c', 'd'],
    # states
    ['Executed', 'Idle', 'Trying', 'CriticalSection', 'Error'],
    'Idle',
    lambda q: q in ['Executed'],
    lambda q, a: {
        ('Idle', 't'): 'Trying',
        ('Idle', 'c'): 'Error',
        ('Idle', 'd'): 'Error',
        ('Trying', 't'): 'Trying',
        ('Trying', 'c'): 'CriticalSection',
        ('Trying', 'd'): 'Error',
        ('CriticalSection', 't'): 'Trying',
        ('CriticalSection', 'c'): 'Error',
        ('CriticalSection', 'd'): 'Executed',
        ('Executed', 't'): 'Error',
        ('Executed', 'c'): 'Error',
        ('Executed', 'd'): 'Error',
        ('Error', 't'): 'Error',
        ('Error', 'c'): 'Error',
        ('Error', 'd'): 'Error',
    }[(q, a)]
)

print("input sequence is tttttttcd")
Enforcer.enforcer(copy.copy(phi), ['t', 't', 't', 't', 't', 't', 't', 'c', 'd'], 5)  
		
#
#
#
#
