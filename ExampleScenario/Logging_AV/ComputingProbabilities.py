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
import csv
import math
import matplotlib.pyplot as plt



# phi for Generate_Password with 5 states
phi = Automata.DFA(
    # Input alphabets
    ['R', 'L', 'F', 'S'],
    # states
    ['stop', 'start', 'right', 'left', 'forward'],
    'start',
    lambda q: q in ['stop'],
    lambda q, a: {
        ('start', 'R'): 'right',
        ('start', 'L'): 'left',
        ('start', 'F'): 'forward',
        ('start', 'S'): 'stop',
        ('right', 'R'): 'right',
        ('right', 'L'): 'left',
        ('right', 'F'): 'forward',
        ('right', 'S'): 'stop',
        ('left', 'R'): 'right',
        ('left', 'L'): 'left',
        ('left', 'F'): 'forward',
        ('left', 'S'): 'stop',
        ('forward', 'R'): 'right',
        ('forward', 'L'): 'left',
        ('forward', 'F'): 'forward',
        ('forward', 'S'): 'stop',
        ('stop', 'R'): 'right',
        ('stop', 'L'): 'left',
        ('stop', 'F'): 'forward',
        ('stop', 'S'): 'stop',
    }[(q, a)]
)




#function for calculating probability of taking transitions (na,nn,aa,an) 
def CalProbab(phi, sigma):
    nn=0;na=0;an=0;aa=0;
    fromS=phi.q0
    for event in sigma:
        toS=phi.step1(event)
        if phi.F(fromS) and phi.F(toS):
            aa=aa+1
            fromS=toS
        elif (phi.F(fromS) ) and (not phi.F(toS)):
            an=an+1
            fromS=toS
        elif (not phi.F(fromS)) and phi.F(toS):
            na=na+1
            fromS=toS
        elif (not phi.F(fromS)) and (not phi.F(toS)):
            nn=nn+1
            fromS=toS   
    #print(str(aa)+"	"+str(an)+"	"+str(na)+"	"+str(nn)+"	")
    #changing probabilities s.t. an+aa=1 and nn+na=1
    pan=((an*100)/(an+aa))/100
    paa=((aa*100)/(an+aa))/100
    pna=((na*100)/(na+nn))/100
    pnn=((nn*100)/(na+nn))/100
    #print(str(paa)+"	"+str(pan)+"	"+str(pna)+"	"+str(pnn)+"	")
    return pnn, pna, pan, paa
    
 
 
# computing N(size of buffer) for which probability is close to 1      
def Compute_N(n,alpha):    #n is how many times, u want to compute N, so that we can select the largest N out of it 
	all_N=[] #all N we got after 1000 iterations would be stored in this list
	for iteration in range(n):  #100  
		# generating random input trace of size 10000
		alphabets= 'RLFS' 
		inputtrace = ''.join((random.choice(alphabets)) for x in range(10000));  #print("input trace: ", inputtrace)  

		#calling function for calculating probability of taking transitions (na,nn,aa,an) 
		pnn, pna, pan, paa = CalProbab(copy.copy(phi), inputtrace)
		print(str(paa)+"	"+str(pan)+"	"+str(pna)+"	"+str(pnn)+"	")
		#computing N(size of buffer) for which probability is close to 1    
		a=1
		s0=1+(pan/pna)
		"""
		for N in range(1, 270):
			for k in range(2, N):
				a= a + (pan * pow(pnn, k-2))	
			print("N= "+str(N)+"	probability= "+str(a/s0))	
			if ((a/s0)>alpha):
				N=N-1
				all_N.append(N)
				break		
		"""
		k=2
		while 1: #while 1:
		    list1=[]
		    a= a + (pan * pow(pnn, k-2))
		    print("N= "+str(k)+"	probability= "+str(a/s0))
		    list1.append(k);list1.append(a/s0)
		    with open('/home/iit/Documents/BMRE.git/trunk/ExampleScenario/Logging_AV/graph.csv', 'a', newline='') as file:
			    writer = csv.writer(file)
			    writer.writerow(list1)
		    if ((a/s0)>alpha):
                        #k=k-1
                        all_N.append(k)
                        break	
		    else:
                        k=k+1
	print(max(all_N)) 
	return max(all_N)





#calling enforcers with N to see if (output of bounded = output of unbounded)
def enforcers(n,alpha,n_clean): #n_clean indicates how many times u want to run the experiment to get an avg over clean
	no_of_times_clean_called=[]
	for i in range(n_clean):
		print("...............................	i="+str(i))
		alphabets= 'RLFS'; test_input = ''.join((random.choice(alphabets)) for x in range(1000)); #print(test_input) # generating random input trace of size 10000
		O_bounded = EnforcerEval.enforcer(copy.copy(phi), test_input, Compute_N(n, alpha)) 	# running bounded enforcer
		O_ideal = EnforcerEval.idealenforcer(copy.copy(phi), test_input)	# running ideal enforcer
		#print('O_bounded= '+str(O_bounded))
		#print('O_ideal= '+str(O_ideal))
		if O_bounded==O_ideal:
			print("equal")
		else:
			print("not equal")
		print('number clean= '+str(EnforcerEval.y))
		no_of_times_clean_called.append(EnforcerEval.y)

	print(sum(no_of_times_clean_called)/n_clean) #179 times on an avg clean is called

	
enforcers(1,0.99,1)
#10 is how many times, u want to compute N, so that we can select the largest N out of it
# 99 is the probability specified
#10 is how many times u want to run the experiment to get an avg over clean
#
#
#






#
#
#
