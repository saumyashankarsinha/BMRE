#march 22

#######imports########################################
import sys
import os.path
sys.path.append("../")
from pathlib import Path
sourcedir=Path(__file__).resolve().parent.parent.parent
sourcedir=os.path.join(sourcedir, 'Source')
sys.path = [sourcedir] + sys.path
import Enforcer
import EnforcerEval
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

# phi for Generate_Password with 5 states
phi1_5 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q2', 'q0', 'q1', 'q3','q4'],
    'q0',
    lambda q: q in ['q3'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q1',
        ('q0', 'c'): 'q1',
        ('q0', '1'): 'q4',
        ('q0', '2'): 'q4',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q2',
        ('q1', '1'): 'q4',
        ('q1', '2'): 'q4',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2',
        ('q2', 'c'): 'q2',
        ('q2', '1'): 'q3',
        ('q2', '2'): 'q3',
        ('q3', 'a'): 'q4',
        ('q3', 'b'): 'q4',
        ('q3', 'c'): 'q4',
        ('q3', '1'): 'q3',
        ('q3', '2'): 'q3',
        ('q4', 'a'): 'q4',
        ('q4', 'b'): 'q4',
        ('q4', 'c'): 'q4',
        ('q4', '1'): 'q4',
        ('q4', '2'): 'q4',
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
        ('q0', 'b'): 'q1',
        ('q0', 'c'): 'q1',
        ('q0', '1'): 'q5',
        ('q0', '2'): 'q5',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q2',
        ('q1', '1'): 'q5',
        ('q1', '2'): 'q5',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q3',
        ('q2', 'c'): 'q3',
        ('q2', '1'): 'q5',
        ('q2', '2'): 'q5',
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


# phi for Generate_Password with 7 states
phi1_7 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q4','q5','q6','q0', 'q1', 'q2','q3'],
    'q0',
    lambda q: q in ['q5'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q1',
        ('q0', 'c'): 'q1',
        ('q0', '1'): 'q6',
        ('q0', '2'): 'q6',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q2',
        ('q1', '1'): 'q6',
        ('q1', '2'): 'q6',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q3',
        ('q2', 'c'): 'q3',
        ('q2', '1'): 'q6',
        ('q2', '2'): 'q6',
        ('q3', 'a'): 'q4',
        ('q3', 'b'): 'q4',
        ('q3', 'c'): 'q4',
        ('q3', '1'): 'q6',
        ('q3', '2'): 'q6',
	('q4', 'a'): 'q4',
        ('q4', 'b'): 'q4',
        ('q4', 'c'): 'q4',
        ('q4', '1'): 'q5',
        ('q4', '2'): 'q5',
	('q5', 'a'): 'q6',
        ('q5', 'b'): 'q6',
        ('q5', 'c'): 'q6',
        ('q5', '1'): 'q5',
        ('q5', '2'): 'q5',
	('q6', 'a'): 'q6',
        ('q6', 'b'): 'q6',
        ('q6', 'c'): 'q6',
        ('q6', '1'): 'q6',
        ('q6', '2'): 'q6',
    }[(q, a)]
)


# phi for Generate_Password with 8 states
phi1_8 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q4','q5','q6','q0', 'q1', 'q2','q3','q7'],
    'q0',
    lambda q: q in ['q6'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q1',
        ('q0', 'c'): 'q1',
        ('q0', '1'): 'q7',
        ('q0', '2'): 'q7',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q2',
        ('q1', '1'): 'q7',
        ('q1', '2'): 'q7',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q3',
        ('q2', 'c'): 'q3',
        ('q2', '1'): 'q7',
        ('q2', '2'): 'q7',
        ('q3', 'a'): 'q4',
        ('q3', 'b'): 'q4',
        ('q3', 'c'): 'q4',
        ('q3', '1'): 'q7',
        ('q3', '2'): 'q7',
	('q4', 'a'): 'q5',
        ('q4', 'b'): 'q5',
        ('q4', 'c'): 'q5',
        ('q4', '1'): 'q7',
        ('q4', '2'): 'q7',
	('q5', 'a'): 'q5',
        ('q5', 'b'): 'q5',
        ('q5', 'c'): 'q5',
        ('q5', '1'): 'q6',
        ('q5', '2'): 'q6',
	('q6', 'a'): 'q7',
        ('q6', 'b'): 'q7',
        ('q6', 'c'): 'q7',
        ('q6', '1'): 'q6',
        ('q6', '2'): 'q6',
	('q7', 'a'): 'q7',
        ('q7', 'b'): 'q7',
        ('q7', 'c'): 'q7',
        ('q7', '1'): 'q7',
        ('q7', '2'): 'q7',
    }[(q, a)]
)

# phi for Generate_Password with 9 states
phi1_9 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q4','q5','q6','q0', 'q1', 'q2','q3','q7','q8'],
    'q0',
    lambda q: q in ['q7'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q1',
        ('q0', 'c'): 'q1',
        ('q0', '1'): 'q8',
        ('q0', '2'): 'q8',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q2',
        ('q1', '1'): 'q8',
        ('q1', '2'): 'q8',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q3',
        ('q2', 'c'): 'q3',
        ('q2', '1'): 'q8',
        ('q2', '2'): 'q8',
        ('q3', 'a'): 'q4',
        ('q3', 'b'): 'q4',
        ('q3', 'c'): 'q4',
        ('q3', '1'): 'q8',
        ('q3', '2'): 'q8',
	('q4', 'a'): 'q5',
        ('q4', 'b'): 'q5',
        ('q4', 'c'): 'q5',
        ('q4', '1'): 'q8',
        ('q4', '2'): 'q8',
	('q5', 'a'): 'q6',
        ('q5', 'b'): 'q6',
        ('q5', 'c'): 'q6',
        ('q5', '1'): 'q8',
        ('q5', '2'): 'q8',
	('q6', 'a'): 'q6',
        ('q6', 'b'): 'q6',
        ('q6', 'c'): 'q6',
        ('q6', '1'): 'q7',
        ('q6', '2'): 'q7',
	('q7', 'a'): 'q8',
        ('q7', 'b'): 'q8',
        ('q7', 'c'): 'q8',
        ('q7', '1'): 'q7',
        ('q7', '2'): 'q7',
	('q8', 'a'): 'q8',
        ('q8', 'b'): 'q8',
        ('q8', 'c'): 'q8',
        ('q8', '1'): 'q8',
        ('q8', '2'): 'q8',
    }[(q, a)]
)





# phi for Generate_Password with 10 states
phi1_10 = Automata.DFA(
    # Input alphabets
    ['a', 'b', 'c', '1', '2'],
    # states
    ['q4','q5','q6','q0', 'q1', 'q2','q3','q7','q8','q9'],
    'q0',
    lambda q: q in ['q8'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q1',
        ('q0', 'c'): 'q1',
        ('q0', '1'): 'q9',
        ('q0', '2'): 'q9',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q2',
        ('q1', '1'): 'q9',
        ('q1', '2'): 'q9',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q3',
        ('q2', 'c'): 'q3',
        ('q2', '1'): 'q9',
        ('q2', '2'): 'q9',
        ('q3', 'a'): 'q4',
        ('q3', 'b'): 'q4',
        ('q3', 'c'): 'q4',
        ('q3', '1'): 'q9',
        ('q3', '2'): 'q9',
	('q4', 'a'): 'q5',
        ('q4', 'b'): 'q5',
        ('q4', 'c'): 'q5',
        ('q4', '1'): 'q9',
        ('q4', '2'): 'q9',
	('q5', 'a'): 'q6',
        ('q5', 'b'): 'q6',
        ('q5', 'c'): 'q6',
        ('q5', '1'): 'q9',
        ('q5', '2'): 'q9',
	('q6', 'a'): 'q7',
        ('q6', 'b'): 'q7',
        ('q6', 'c'): 'q7',
        ('q6', '1'): 'q9',
        ('q6', '2'): 'q9',
	('q7', 'a'): 'q7',
        ('q7', 'b'): 'q7',
        ('q7', 'c'): 'q7',
        ('q7', '1'): 'q8',
        ('q7', '2'): 'q8',
	('q8', 'a'): 'q9',
        ('q8', 'b'): 'q9',
        ('q8', 'c'): 'q9',
        ('q8', '1'): 'q8',
        ('q8', '2'): 'q8',
	('q9', 'a'): 'q9',
        ('q9', 'b'): 'q9',
        ('q9', 'c'): 'q9',
        ('q9', '1'): 'q9',
        ('q9', '2'): 'q9',
    }[(q, a)]
)





#Generate_Password
mylist = ["1", "2"]
_sum = 100000 #length of input seq

input_sizes_taken =[10000]#,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
df = pd.DataFrame()

for i in input_sizes_taken: 
	print('input size= '+ str(i));print('states=phi1_10')
	rnd_array = [i-2, 2]
	s1=''.join(chr(random.randint(97,99)) for i in range(rnd_array[0])) 
	s2=''.join(random.choice(mylist) for j in range(rnd_array[1])) 

	eAvgTime = []
	iAvgTime = []
	clean_time = []
	for j in range(100): # 100 iterations
		EnforcerEval.enforcer(copy.copy(phi1_10), s1+s2, 10)  
		eAvgTime.append(EnforcerEval.eend-EnforcerEval.estart)
		clean_time.append(EnforcerEval.sum)
		EnforcerEval.idealenforcer(copy.copy(phi1_10), s1+s2)
		iAvgTime.append(EnforcerEval.iend-EnforcerEval.istart)
	esum=0
	isum=0
	clean_sum=0
	for k in range(100):#range(0, 1):
		esum=esum+eAvgTime[k]
		isum=isum+iAvgTime[k]
		clean_sum=clean_sum+clean_time[k]
	print('ideal= '+str(isum/100))
	print('number clean= '+str(EnforcerEval.y))
	print('time clean= '+str(clean_sum/100))
	print('BME= '+str(esum/100))
	print('t1-t2= '+str((esum/100)-(clean_sum/100)))	
	print('ideal per event= '+str((isum/100)/i))



	dict = {'input length': i,'states': 'phi1_10', 'total online time for ideal': str(isum/100), 'average time per event for ideal': str((isum/100)/i), 'clean #':EnforcerEval.y, 'total online time for BME(T1)':esum/100, 'total time clean(T2)':clean_sum/100, 'T1-T2':str((esum/100)-(clean_sum/100))} 
	df1 = pd.DataFrame(dict, index=[0])
	df= df.append(df1)
	print (".........................................................")
	
df.to_csv('file3.csv',mode='a')	


#
#
#
#
