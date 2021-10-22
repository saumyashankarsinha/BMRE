#######imports########################################
import sys
import os.path
sys.path.append("../")
from pathlib import Path
sourcedir=Path(__file__).resolve().parent.parent.parent
sourcedir=os.path.join(sourcedir, 'Source')
sys.path = [sourcedir] + sys.path
import EnforcerEval
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
    
    
# Performance Evaluation
sample_string1 = 'ab'
sample_string2 = ["c"]

_sum = 100000 #length of input seq

input_sizes_taken =[10,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
df = pd.DataFrame()

for i in input_sizes_taken: 
	print('input size= '+ str(i))
	rnd_array = [i-2, 2]
	s1=result = ''.join((random.choice(sample_string1)) for i in range(rnd_array[0]))  
	s2=''.join(random.choice(sample_string2) for j in range(rnd_array[1])) 
	eAvgTime = []
	iAvgTime = []
	clean_time = []
	for j in range(100): # 100 iterations
		EnforcerEval.enforcer(copy.copy(phi), s1+s2, 10) 
		eAvgTime.append(EnforcerEval.eend-EnforcerEval.estart)
		clean_time.append(EnforcerEval.sum)
		##########################
		EnforcerEval.idealenforcer(copy.copy(phi), s1+s2)
		iAvgTime.append(EnforcerEval.iend-EnforcerEval.istart)
	esum=0
	isum=0
	clean_sum=0
	for k in range(100):#range(0, 1):
		esum=esum+eAvgTime[k]
		isum=isum+iAvgTime[k]
		clean_sum=clean_sum+clean_time[k]
	print('BME= '+str(esum/100))
	#print('BME per event= '+str((esum/100)/i))
	print('number clean= '+str(EnforcerEval.y))
	print('time clean= '+str(clean_sum/100))
	print('t1-t2= '+str((esum/100)-(clean_sum/100)))

	print('ideal= '+str(isum/100))
	print('ideal per event= '+str((isum/100)/i))



	dict = {'input length': i, 'total online time for ideal': str(isum/100), 'average time per event for ideal': str((isum/100)/i), 'clean #':EnforcerEval.y, 'total online time for BME(T1)':esum/100, 'total time clean(T2)':clean_sum/100, 'T1-T2':str((esum/100)-(clean_sum/100))} 
	df1 = pd.DataFrame(dict, index=[0])
	df= df.append(df1)
	print (".........................................................")

#writing to a file	
df.to_csv('Logging_ManualMode_AV_Performance.csv',mode='a')	


#
#
#
#
