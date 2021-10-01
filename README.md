# BMRE
Bounded-Memory Runtime Enforcer.

The bounded-memory enforcer is implemented in Python. The functionality is divided into two modules DFA (contained in Automata.py) and  Enforcer (contained in Enforcer.py)  modules. The DFA module contains all the functionalities related to defining the automaton and operations on the automaton. The Enforcer module implements the bounded-memory enforcer. 


The enforcer method in the module Enforcer is invoked with an automaton defining the property (described in the intended format using the  DFA module), a positive integer specifying the buffer size, and a sequence of events.


The performance of the Python implementation of bounded-memory enforcer is evaluated using some example properties. Its performance is also compared against the ideal (unbounded) enforcer. The example properties are located in the Examples folder.


The overall architecture will be added in some time. 


HOW TO RUN-
	goto Bounded_Memory_RE/Examples
	open terminal in Examples
	run python "give path of GeneratePassword.py file"
