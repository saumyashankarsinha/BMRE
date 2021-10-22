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


 
    
    
# Performance Evaluation
sample_string1 = 'rlf'
sample_string2 = ["s"]

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
df.to_csv('Logging_AV_Performance.csv',mode='a')	


#
#
#
#
