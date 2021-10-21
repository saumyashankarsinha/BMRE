# BMRE
Bounded-Memory Runtime Enforcer.

This repository contains additional material for the work titled "Bounded-Memory Runtime Enforcer". The bounded-memory runtime enforcement is a monitoring technique to ensure that a system obeys a set of formal requirements (properties) by employing an enforcer (a safety wrapper for the system) which modifies the (untrustworthy) output by performing actions such as delaying (by storing/buffering into its internal memory) and suppressing events, when needed. For storing the events, the enforcer is equipped with a buffer/internal memory which is bounded in this work to represent the general/real scenarios.


<!-- 
Runtime Enforcement (RE) is a monitoring technique to ensure that a system obeys a set of formal requirements (properties). RE employs an enforcer (a safety wrapper for the system) which modifies the (untrustworthy) output by performing actions such as delaying (by storing/buffering into its internal memory) and suppressing events, when needed. In usual RE mechanisms, the internal memory of the enforcer is considered to be unbounded/infinite. But in a real situation, the enforcer has a bounded internal memory. So, this work studies RE with a bounded buffer, i.e., it talks about how the enforcer tackles the situation when the buffer
is bounded/finite. The general schema is shown in the figure below where σ is the sequence of events given as input to the enforcer and o is the transformed output that is correct with respect to property φ.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/bme.png)
-->
## Contents
The contents of the repository is organized as follows: The BMRE repository contains three directories, the *Source* directory (containing the major implementation functions), the *Example Scenario* directory (containing some examples which has been used to evaluate the performance of the enforcer), and the *Image* directory (containing the illustrative images).
- The Source directory contains source files
  - Automata.py which contains all the functionalities related to defining the automaton and operations on the automaton;
  - Enforcer.py which implements the bounded-memory enforcer;
  - EnforcerEval.py which evaluates our enforcer with respect to the ideal enforcer.
- The Example Scenario directory contains four example scenarios contained in the following directories:
  - Logging_AV
  - ManualMode_AV
  - CriticalSectionProblem 
  - Lock
  
## Example Properties
1. Logging in AV: The first example scenario, used to evaluate the performance of our enforcer, contained in the Logging_AV directory, is related to logging of steering commands in Autonomous Vehicle (AV) required for simulations in the lab for future autonomous functions. The path planning steering commands like Move Left, Move Right, Move Forward, and Stop are logged for better testing and validation solutions, each time it is issued. However, due to memory constraints in AV, the data (event) is logged to a remote location. But, logging each event, every time it is issued, to a remote location is difficult. Thus, let’s consider the requirement, “Logging of path planning steering commands should be done, when the vehicle reaches a Stop state”, on the remote logging application to manage the overhead. Below figure presents the automaton of the proposed property.


The bounded-memory enforcer is implemented in Python. The functionality is divided into two modules :
- DFA (contained in Automata.py) module- which contains all the functionalities related to defining the automaton and operations on the automaton;
- Enforcer (contained in Enforcer.py) module- which implements the bounded-memory enforcer

The enforcer method in the module Enforcer takes three arguments, which are: an automaton defining the property (described in the intended format using the  DFA module), a positive integer specifying the buffer size, and a sequence of events.
> Enforcer.enforcer(copy.copy(phi1_4), ['a', 'a', 'b', 'b', 'c', '1', '2'], 4)  

 phi1_4 is the automata defining the property to be enforced; ['a', 'a', 'b', 'b', 'c', '1', '2'] is the sequence of events; and 4 is buffer size in the above call to the enforcer in line number 152 of GeneratePassword.py. It computes the output sequence (the transformed output which is correct with respect to property φ) incrementally.

## Example Properties
To illustrate the Bounded-memory Runtime Enforcement, some example properties are located in the ExampleScenario folder. We here present one of the example property.

1. Generate Password- Consider a scenario where an application generates passwords for a system, using characters and digits. Let us suppose that the generated password should meet a specific requirement which is, *“The password should start with one or more characters and end with one or more digits”*. The password is valid only if this required format condition holds. The automaton in the below figure defines this requirement φ. Let us suppose the alphabets and digits provided are {a, b, c} and {1, 2} respectively. The enforcer for φ must buffer all the characters without generating an authentic password for the user, until atleast one digit is received. Once it receives a digit, it can “flush” its buffer and provide the password.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/password.png)

*How to run:*
> go to Bounded_Memory_RE/ExamplesScenario

> open terminal in ExamplesScenario

> run *python "give path of GeneratePassword.py file"*

- [ ] The overall architecture will be added in some time :tada:
