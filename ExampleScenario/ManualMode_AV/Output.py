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
    ['AllReceived', 'start', 'AReceived', 'BReceived', 'CReceived', 'ABReceived', 'BCReceived', 'CAReceived', 'dead'],
    'start',
    lambda q: q in ['AllReceived'],
    lambda q, a: {
        ('start', 'a'): 'AReceived',
        ('start', 'b'): 'BReceived',
        ('start', 'c'): 'CReceived',
        ('AReceived', 'a'): 'AReceived',
        ('AReceived', 'b'): 'ABReceived',
        ('AReceived', 'c'): 'CAReceived',
        ('BReceived', 'a'): 'ABReceived',
        ('BReceived', 'b'): 'BReceived',
        ('BReceived', 'c'): 'BCReceived',
        ('CReceived', 'a'): 'CAReceived',
        ('CReceived', 'b'): 'BCReceived',
        ('CReceived', 'c'): 'CReceived',
        ('ABReceived', 'a'): 'ABReceived',
        ('ABReceived', 'b'): 'ABReceived',
        ('ABReceived', 'c'): 'AllReceived',
        ('BCReceived', 'a'): 'AllReceived',
        ('BCReceived', 'b'): 'BCReceived',
        ('BCReceived', 'c'): 'BCReceived',
        ('CAReceived', 'a'): 'CAReceived',
        ('CAReceived', 'b'): 'AllReceived',
	('CAReceived', 'c'): 'CAReceived',
	('AllReceived', 'a'): 'dead',
        ('AllReceived', 'b'): 'dead',
        ('AllReceived', 'c'): 'dead',
        ('dead', 'a'): 'dead',
        ('dead', 'b'): 'dead',
        ('dead', 'c'): 'dead',
    }[(q, a)]
)

print("input sequence is aaaaabbbbbccc")
Enforcer.enforcer(copy.copy(phi), ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c'], 9)  
		
#
#
#
#
