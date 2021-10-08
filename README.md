# BMRE
Bounded-Memory Runtime Enforcer.

Runtime Enforcement (RE) is a monitoring technique to ensure that a system obeys a set of formal requirements (properties). RE employs an enforcer (a safety wrapper for the system) which modifies the (untrustworthy) output by performing actions such as delaying (by storing/buffering into its internal memory) and suppressing events, when needed. In usual RE mechanisms, the internal memory of the enforcer is considered to be unbounded/infinite. But in a real situation, the enforcer has a bounded internal memory. So, this work studies RE with a bounded buffer, i.e., it talks about how the enforcer tackles the situation when the buffer
is bounded/finite. The general schema is shown in the figure below where σ is the sequence of events given as input to the enforcer and o is the transformed output that is correct with respect to property φ.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/bme.png)

The bounded-memory enforcer is implemented in Python. The functionality is divided into two modules :
- DFA (contained in Automata.py) module- which contains all the functionalities related to defining the automaton and operations on the automaton;
- Enforcer (contained in Enforcer.py) module- which implements the bounded-memory enforcer

The enforcer method in the module Enforcer takes three arguments, which are: an automaton defining the property (described in the intended format using the  DFA module), a positive integer specifying the buffer size, and a sequence of events.
> Enforcer.enforcer(copy.copy(phi1_4), ['a', 'a', 'b', 'b', 'c', '1', '2'], 4)  

 phi1_4 is the automata defining the property to be enforced; ['a', 'a', 'b', 'b', 'c', '1', '2'] is the sequence of events; and 4 is buffer size in the above call to the enforcer in line number 152 of GeneratePassword.py. It computes the output sequence (the transformed output which is correct with respect to property φ) incrementally.

## Example Properties
To illustrate the Bounded-memory Runtime Enforcement, some example properties are located in the Examples folder. We here present three example properties.

1. Generate Password- Consider a scenario where an application generates passwords for a system, using characters and digits. Let us suppose that the generated password should meet a specific requirement which is, *“The password should start with one or more characters and end with one or more digits”*. The password is valid only if this required format condition holds. The automaton in the below figure defines this requirement φ. Let us suppose the alphabets and digits provided are {a, b, c} and {1, 2} respectively. The enforcer for φ must buffer all the characters without generating an authentic password for the user, until atleast one digit is received. Once it receives a digit, it can “flush” its buffer and provide the password.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/password.png)

*How to run:*
> go to Bounded_Memory_RE/Examples
> open terminal in Examples
> run *python "give path of GeneratePassword.py file"*


The overall architecture will be added in some time. 


*HOW TO RUN*

goto Bounded_Memory_RE/Examples

open terminal in Examples

run: python "give path of GeneratePassword.py file"

