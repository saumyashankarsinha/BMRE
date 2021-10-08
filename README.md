# BMRE
Bounded-Memory Runtime Enforcer.

Runtime Enforcement (RE) is a monitoring technique to ensure that a system obeys a set of formal requirements (properties). RE employs an enforcer (a safety wrapper for the system) which modifies the (untrustworthy) output by performing actions such as delaying (by storing/buffering into its internal memory) and suppressing events, when needed. In usual RE mechanisms, the internal memory of the enforcer is considered to be unbounded/infinite. But in a real situation, the enforcer has a bounded internal memory. So, this work studies RE with a bounded buffer, i.e., it talks about how the enforcer tackles the situation when the buffer
is bounded/finite. The general schema is shown in the figure below where σ is the sequence of events given as input to the enforcer and o is the transformed output that is correct with respect to property φ.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/bme.png)

The bounded-memory enforcer is implemented in Python. The functionality is divided into two modules 
- DFA (contained in Automata.py) and  
- Enforcer (contained in Enforcer.py)  modules. 

The DFA module contains all the functionalities related to defining the automaton and operations on the automaton. The Enforcer module implements the bounded-memory enforcer. 


The enforcer method in the module Enforcer is invoked with an automaton defining the property (described in the intended format using the  DFA module), a positive integer specifying the buffer size, and a sequence of events.


The performance of the Python implementation of bounded-memory enforcer is evaluated using some example properties. Its performance is also compared against the ideal (unbounded) enforcer. The example properties are located in the Examples folder.


The overall architecture will be added in some time. 


*HOW TO RUN*

goto Bounded_Memory_RE/Examples

open terminal in Examples

run: python "give path of GeneratePassword.py file"

