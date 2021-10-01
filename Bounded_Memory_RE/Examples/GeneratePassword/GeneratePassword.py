#######imports########################################
import sys
sys.path.append("../")
import Enforcer
import Automata
import copy
import random
import numpy
import time
import pandas as pd 
######################################################


# phi for Generate_Password with 4 states
phi1_4 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q2', 'q0', 'q1', 'q3'],
    'q0',
    lambda q: q in ['q2'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q1',
        ('q0', 'c'): 'q1',
        ('q0', '1'): 'q3',
        ('q0', '2'): 'q3',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q1',
        ('q1', 'c'): 'q1',
        ('q1', '1'): 'q2',
        ('q1', '2'): 'q2',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q3',
        ('q2', 'c'): 'q3',
        ('q2', '1'): 'q2',
        ('q2', '2'): 'q2',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3',
        ('q3', 'c'): 'q3',
        ('q3', '1'): 'q3',
        ('q3', '2'): 'q3',

    }[(q, a)]
)

# phi for Generate_Password with 6 states
phi1_6 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q4', 'q0', 'q1', 'q2','q3','q5'],
    'q0',
    lambda q: q in ['q4'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q2',
        ('q0', 'c'): 'q3',
        ('q0', '1'): 'q5',
        ('q0', '2'): 'q5',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q1',
        ('q1', 'c'): 'q1',
        ('q1', '1'): 'q4',
        ('q1', '2'): 'q4',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2',
        ('q2', 'c'): 'q2',
        ('q2', '1'): 'q4',
        ('q2', '2'): 'q4',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3',
        ('q3', 'c'): 'q3',
        ('q3', '1'): 'q4',
        ('q3', '2'): 'q4',
	('q4', 'a'): 'q5',
        ('q4', 'b'): 'q5',
        ('q4', 'c'): 'q5',
        ('q4', '1'): 'q4',
        ('q4', '2'): 'q4',
	('q5', 'a'): 'q5',
        ('q5', 'b'): 'q5',
        ('q5', 'c'): 'q5',
        ('q5', '1'): 'q5',
        ('q5', '2'): 'q5',
    }[(q, a)]
)

# phi for Generate_Password with 10 states
phi1_10 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q4','q5','q6','q0', 'q1', 'q2','q3','q7','q8','q9'],
    'q0',
    lambda q: q in ['q4','q5','q6'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q2',
        ('q0', 'c'): 'q3',
        ('q0', '1'): 'q9',
        ('q0', '2'): 'q9',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q1',
        ('q1', 'c'): 'q1',
        ('q1', '1'): 'q4',
        ('q1', '2'): 'q4',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2',
        ('q2', 'c'): 'q2',
        ('q2', '1'): 'q5',
        ('q2', '2'): 'q5',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3',
        ('q3', 'c'): 'q3',
        ('q3', '1'): 'q6',
        ('q3', '2'): 'q6',
	('q4', 'a'): 'q7',
        ('q4', 'b'): 'q7',
        ('q4', 'c'): 'q7',
        ('q4', '1'): 'q4',
        ('q4', '2'): 'q4',
	('q5', 'a'): 'q8',
        ('q5', 'b'): 'q8',
        ('q5', 'c'): 'q8',
        ('q5', '1'): 'q5',
        ('q5', '2'): 'q5',
	('q6', 'a'): 'q9',
        ('q6', 'b'): 'q9',
        ('q6', 'c'): 'q9',
        ('q6', '1'): 'q6',
        ('q6', '2'): 'q6',
	('q7', 'a'): 'q7',
        ('q7', 'b'): 'q7',
        ('q7', 'c'): 'q7',
        ('q7', '1'): 'q7',
        ('q7', '2'): 'q7',
	('q8', 'a'): 'q8',
        ('q8', 'b'): 'q8',
        ('q8', 'c'): 'q8',
        ('q8', '1'): 'q8',
        ('q8', '2'): 'q8',
	('q9', 'a'): 'q9',
        ('q9', 'b'): 'q9',
        ('q9', 'c'): 'q9',
        ('q9', '1'): 'q9',
        ('q9', '2'): 'q9',
    }[(q, a)]
)

print("input sequence is aabbc12")
Enforcer.enforcer(copy.copy(phi1_4), ['a', 'a', 'b','b',  'c', '1', '2'], 4)  #phi1_4 is for no of states  # 4 is buffer size
		
#
#
#
#
