#										safety- property

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


# phi for safety property with 4 states
phi1 = Automata.DFA(
    # Input alphabets
    ['a', 'b'],
    # states
    ['q0', 'q1', 'q2', 'q3'],
    'q0',
    lambda q: q in ['q0', 'q1','q2'],
    lambda q, a: {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q1',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q2',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3',

    }[(q, a)]
)


input_sizes_taken =[10,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
df = pd.DataFrame()

for i in input_sizes_taken: 
	print('input size= '+ str(i))
	s1=''.join(chr(random.randint(97,98)) for i in range(i)) 


	eAvgTime = []
	iAvgTime = []
	clean_time = []
	for j in range(100): # 100 iterations
		Enforcer.enforcer(copy.copy(phi1), s1, 4)  #phi1_4 is for no of states  # 10 is buffer size
		eAvgTime.append(Enforcer.eend-Enforcer.estart)
		clean_time.append(Enforcer.sum)
		##########################
		Enforcer.idealenforcer(copy.copy(phi1), s1)
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
	
df.to_csv('states4.csv',mode='a')	


#
#
#
#









