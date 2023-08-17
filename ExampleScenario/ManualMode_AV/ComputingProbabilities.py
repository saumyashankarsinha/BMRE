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
    print(str(aa)+"	"+str(an)+"	"+str(na)+"	"+str(nn)+"	")
    #changing probabilities s.t. an+aa=1 and nn+na=1
    try:
    	pan=((an*100)/(an+aa))/100
    except ZeroDivisionError:
    	pan=0
    try:    	
    	paa=((aa*100)/(an+aa))/100
    except ZeroDivisionError:
    	paa=0
    try:    	
    	pna=((na*100)/(na+nn))/100    	
    except ZeroDivisionError:
    	pna=0
    try:
    	pnn=((nn*100)/(na+nn))/100
    except ZeroDivisionError:
    	pnn=0
    #print(str(paa)+"	"+str(pan)+"	"+str(pna)+"	"+str(pnn)+"	")
    return pnn, pna, pan, paa
    
 
 
# computing N(size of buffer) for which probability is close to 1      
def Compute_N(n,alpha):    #n is how many times, u want to compute N, so that we can select the largest N out of it 
	all_N=[] #all N we got after 1000 iterations would be stored in this list
	for iteration in range(n):  #100  
		# generating random input trace of size 10000
		alphabets= 'abc' 
		inputtrace = ''.join((random.choice(alphabets)) for x in range(1000));  #print("input trace: ", inputtrace)  
		
		#calling function for calculating probability of taking transitions (na,nn,aa,an) 
		pnn, pna, pan, paa = CalProbab(copy.copy(phi), inputtrace)
		print(str(paa)+"	"+str(pan)+"	"+str(pna)+"	"+str(pnn)+"	")
		#computing N(size of buffer) for which probability is close to 1    
		a=1
		#s0=1+(pan/pna)
		try:
    			s0=1+(pan/pna)
		except ZeroDivisionError:
			s0=1
		k=2
		while 1: #while 1:
		    list1=[]
		    a= a + (pan * pow(pnn, k-2))
		    print("N= "+str(k)+"	probability= "+str(a/s0))
		    list1.append(k);list1.append(a/s0)	
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
		# generating random input trace of size 1000
		sample_string = ["a","b","c"]
		input_trace=result = ''.join((random.choice(sample_string)) for i in range(1000))  
		#print(input_trace)

		O_bounded = EnforcerEval.enforcer(copy.copy(phi), input_trace, Compute_N(n, alpha)) 	# running bounded enforcer
		O_ideal = EnforcerEval.idealenforcer(copy.copy(phi), input_trace)	# running ideal enforcer
		if O_bounded==O_ideal:
			print("equal")
		else:
			print("not equal")
		print('number clean= '+str(EnforcerEval.y))
		no_of_times_clean_called.append(EnforcerEval.y)

	print(sum(no_of_times_clean_called)/n_clean) #179 times on an avg clean is called


	
	

#Compute_N(1,0.9)
enforcers(1,0.9,1)
#10 is how many times, u want to compute N, so that we can select the largest N out of it
# 99 is the probability specified
#10 is how many times u want to run the experiment to get an avg over clean
#
#
#
#
#
#
