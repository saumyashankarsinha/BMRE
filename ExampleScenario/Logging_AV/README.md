## How to run:
The automata is provided in the below intended format:

<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/phi_Logging_AV.png">
</p> 
Then the enforcer method of the Enforcer.py is called as shown in the below figure, which takes three arguments: an above automaton defining the property, a positive integer specifying the buffer size, and a sequence of events.
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/call_to_Enforcer_Logging_AV.png">
</p>

**In order to run the example with the above automata to see the output of the enforcer:**
> go to BMRE

> open terminal in BMRE

> run *python "give path of Output.py file"*

The output is shown as follows:
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/output_Logging_AV.png">
</p> 


**In order to run the example to compare the performance of our enforcer with the ideal one:**
> go to BMRE

> open terminal in BMRE

> run *python "give path of Performance.py file"*

<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/Logging_AV_Performance.png">
</p> 
<!-- 
The bounded-memory enforcer is implemented in Python. The functionality is divided into two modules :
- DFA (contained in Automata.py) module- which contains all the functionalities related to defining the automaton and operations on the automaton;
- Enforcer (contained in Enforcer.py) module- which implements the bounded-memory enforcer
-->
 
<!-- 
## Example Properties
To illustrate the Bounded-memory Runtime Enforcement, some example properties are located in the ExampleScenario folder. We here present one of the example property.

1. Generate Password- Consider a scenario where an application generates passwords for a system, using characters and digits. Let us suppose that the generated password should meet a specific requirement which is, *“The password should start with one or more characters and end with one or more digits”*. The password is valid only if this required format condition holds. The automaton in the below figure defines this requirement φ. Let us suppose the alphabets and digits provided are {a, b, c} and {1, 2} respectively. The enforcer for φ must buffer all the characters without generating an authentic password for the user, until atleast one digit is received. Once it receives a digit, it can “flush” its buffer and provide the password.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/password.png)
-->
- [ ] The overall architecture will be added in some time :tada:
