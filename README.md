# BMRE
Bounded-Memory Runtime Enforcer.
The bounded-memory enforcer is implemented in Python. The functionality is divided into two modules DFA (contained in Automata.py) and  Enforcer (contained in Enforcer.py)  modules. The DFA module contains all the functionalities related to defining the automaton and operations on the automaton. The Enforcer module implements the bounded-memory enforcer. 
The enforcer method in the module Enforcer is invoked with an automaton, defining the property, described in the intended format using the  DFA module, a positive integer specifying the buffer size, a sequence of events.
The performance of the Python implementation of bounded-memory enforcer is evaluated using some example properties based on real applications. Its performance is also compared against the ideal (unbounded) enforcer. One of the example property is provided in GeneratePassword.py located in Examples folder.
The overall architecture will be added in some time. 
