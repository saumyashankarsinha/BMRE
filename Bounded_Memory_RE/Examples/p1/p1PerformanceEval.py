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
p1_3 = Automata.DFA(
    ['0', '1'],
    ['q1', 'q0', 'q2'],
    'q0',
    lambda q: q in ['q1'],
    lambda q, a: {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1', 
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q2',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q2',
    }[(q, a)]
)
p1_6 = Automata.DFA(
    ['0', '1'],
    ['q1', 'q2', 'q4', 'q0','q3','q5'],
    'q0',
    lambda q: q in ['q1', 'q2', 'q4'],
    lambda q, a: {
        ('q0', '0'): 'q3',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q5',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q5',
        ('q3', '0'): 'q0',
        ('q3', '1'): 'q4',
        ('q4', '0'): 'q2',
        ('q4', '1'): 'q5',
        ('q5', '0'): 'q5',
        ('q5', '1'): 'q5', 
    }[(q, a)]
)
p1_9 = Automata.DFA(
    ['0', '1'],
    ['q1', 'q2', 'q4', 'q7','q0','q3','q5','q6','q8'],
    'q0',
    lambda q: q in ['q2'],
    lambda q, a: {
        ('q0', '0'): 'q3',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q5',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q5',
        ('q3', '0'): 'q0',
        ('q3', '1'): 'q4',
        ('q4', '0'): 'q2',
        ('q4', '1'): 'q5',
        ('q5', '0'): 'q5',
        ('q5', '1'): 'q5',
        ('q6', '0'): 'q3',
        ('q6', '1'): 'q7',
        ('q7', '0'): 'q7',
        ('q7', '1'): 'q8',
        ('q8', '0'): 'q8',
        ('q8', '1'): 'q8',
    }[(q, a)]
)

# Policy-P1= exactly one 1
mylist0 = ["0"]
mylist1 = ["1"]
input_sizes_taken =[10,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
df = pd.DataFrame()#_sum = 9	#length of input seq
n = 2

for i in input_sizes_taken: 

	print('input size= '+ str(i))
	rnd_array = [i-2, 2]
	#rnd_array = numpy.random.multinomial(_sum, numpy.ones(n)/n, size=1)[0]
	s1=''.join(random.choice(mylist0) for i in range(rnd_array[0])) 
	s2=''.join(random.choice(mylist1) for j in range(rnd_array[1])) 
	#print s1
	#print s2
	#print s1+s2

	eAvgTime = []
	iAvgTime = []
	clean_time = []
	for j in range(100): # 100 iterations
		Enforcer.enforcer(copy.copy(p1_3), s1+s2, 3)  #p1_3 is for no of states  # 3 is buffer size
		eAvgTime.append(Enforcer.eend-Enforcer.estart)
		clean_time.append(Enforcer.sum)
		##########################
		Enforcer.idealenforcer(copy.copy(p1_3), s1+s2)
		iAvgTime.append(Enforcer.iend-Enforcer.istart)
	esum=0
	isum=0
	clean_sum=0
	for k in range(100):#range(0, 1):
		esum=esum+eAvgTime[k]
		isum=isum+iAvgTime[k]
		clean_sum=clean_sum+clean_time[k]
	print('BME= '+str(esum/100))
	#print('BME per event= '+str((esum/100)/i))
	print('number clean= '+str(Enforcer.y))
	print('time clean= '+str(clean_sum/100))
	print('t1-t2= '+str((esum/100)-(clean_sum/100)))

	print('ideal= '+str(isum/100))
	print('ideal per event= '+str((isum/100)/i))



	dict = {'input length': i, 'total online time for ideal': str(isum/100), 'average time per event for ideal': str((isum/100)/i), 'clean #':Enforcer.y, 'total online time for BME(T1)':esum/100, 'total time clean(T2)':clean_sum/100, 'T1-T2':str((esum/100)-(clean_sum/100))} 
	df1 = pd.DataFrame(dict, index=[0])
	df= df.append(df1)
	print (".........................................................")
	
df.to_csv('states9.csv',mode='a')	











