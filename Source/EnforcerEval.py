
##imports########################################################################################
import Automata
import collections
import itertools 
from itertools import islice
import time

#### Function to pre-compute emptiness check for each state in the given automaton ###############
def computeEmptinessDict(autC):
    dictEnf = {}
    for state in autC.Q:
        autC.makeInit(state) 
        if autC.isEmpty():
            dictEnf[state] = True
        else:
            dictEnf[state] = False
    return dictEnf

#### Function to compute substring of sigmaC by removing smallest cycle in sigmaC ###############
def computes_substring(iterable, n,automata,k):
	cleanedBuffer=[]
	automata.reset(k)
	p1=k
	for i in range (len(iterable)-n): #0, 1, 2, 3, 4, 5
		element=list(islice(iterable[i:], 0, 1+n, 1))	
		for j in range(n+1):
			p2=automata.step1(element[j])
			if(j==0):
				p3=p2
		if(p2==p1):
			cleanedBuffer.extend(iterable[i+n+1:])#cleanedBuffer+iterable[i+n+1:]
			return [n+1,cleanedBuffer];   
		else:
			cleanedBuffer.append(element[0])
		p1=p3
		automata.makeInit(p3)
		automata.reset(p1)

#### Function returning cleaned sigmaC #########################################################
def clean(sigmaC,phiautomata,maxBuffer,k,event):
	yn=None
	for i in range(len(sigmaC)) :
		if(yn == None):
			yn=computes_substring(list(sigmaC),i,phiautomata,k) #compute\_substring    # list() tc is o(n)
			if(i==0 and yn == None):
				for t in sigmaC:
					q_q = phiautomata.d(k, t)
				if phiautomata.d(q_q, event) == q_q:
					return sigmaC
	if(yn!=None):
		yn=yn[1:]
		yn = list(itertools.chain(*yn))
		yn.append(event)
		return yn    

#### Bounded Memory Enforcer function to compute the output sequence sigmaS incrementally #######
def enforcer(phi, sigma,maxBuffer): 
        
	#if maxBuffer < len(phi.Q):
	#		print('your buffer is not of reasonable size')
	#		exit() 
	global estart
	global eend
	global y
	y=0
	global sum
	sum=0
	sigmaC = collections.deque([] * maxBuffer, maxlen=maxBuffer)
	sigmaS=[]
	q=phi.q0
	dictEnf = computeEmptinessDict(phi)
	phi.q0=q
	m=q
	estart = time.time()
	for event in sigma:
		t=q
		q = phi.d(q, event)
		if phi.F(q):
			Final=True
		else:
			Final=False
		if Final == True:
            		for a in sigmaC:
                		sigmaS.append(a)
            		sigmaS.append(event)
            		sigmaC= []
            		t=q
		else:
			if dictEnf[q] == True:
				q=t
			else:
				t=q
				clean_start=0
				clean_end=0
				clean_start = time.time()
				if len(sigmaC) >=maxBuffer:	## len tc is o(n)
					
					phi.q0=m
					k=phi.q0		
					for t in sigmaS:
						k=phi.d(k, t)
					y=y+1
					sigmaC1=clean(sigmaC,phi,maxBuffer,k,event)
					if sigmaC1==100:
						break
					else:
						sigmaC=sigmaC1
					clean_end = time.time()
					sum=sum+clean_end-clean_start
				else:
					sigmaC.append(event)              		
	eend = time.time()					
	#print("output sequence is "+ str(sigmaS))#comment this while running GeneratePasswordPerformanceEval.py
	return sigmaS

	 
#### Ideal Enforcer function to compute the output sequence sigmaS incrementally ##########
def idealenforcer(phi, sigma):
    global istart
    global iend
    isigmaC= []
    isigmaS=[]
    ip=phi.q0
    dictEnf = computeEmptinessDict(phi)
    istart = time.time()
    for event in sigma:
        a=ip
        ip=phi.step1(event)
        if phi.F(ip):
                Final=True
                a=ip
        else:
                Final=False
        if Final == True:
                for a in isigmaC:
                	isigmaS.append(a)
                isigmaS.append(event)
                isigmaC= []
        else:
        	if dictEnf[ip] == True:
                	ip=a
        	else:
                	isigmaC.append(event)
                	a=ip

    iend = time.time()  
    #print("output sequence is "+ str(isigmaS))##comment this while running GeneratePasswordPerformanceEval.py
    return isigmaS
