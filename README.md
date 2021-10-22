# BMRE
Bounded-Memory Runtime Enforcer.

This repository contains additional material for the work titled "Bounded-Memory Runtime Enforcer". The bounded-memory runtime enforcement is a monitoring technique to ensure that a system obeys a set of formal requirements (properties) by employing an enforcer (a safety wrapper for the system) which modifies the (untrustworthy) output by performing actions such as delaying (by storing/buffering into its internal memory) and suppressing events, when needed. For storing the events, the enforcer is equipped with a buffer/internal memory which is bounded in this work to represent the general/real scenarios.


<!-- 
Runtime Enforcement (RE) is a monitoring technique to ensure that a system obeys a set of formal requirements (properties). RE employs an enforcer (a safety wrapper for the system) which modifies the (untrustworthy) output by performing actions such as delaying (by storing/buffering into its internal memory) and suppressing events, when needed. In usual RE mechanisms, the internal memory of the enforcer is considered to be unbounded/infinite. But in a real situation, the enforcer has a bounded internal memory. So, this work studies RE with a bounded buffer, i.e., it talks about how the enforcer tackles the situation when the buffer
is bounded/finite. The general schema is shown in the figure below where σ is the sequence of events given as input to the enforcer and o is the transformed output that is correct with respect to property φ.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/bme.png)
-->
## Contents
The contents of the repository is organized as follows: The BMRE repository contains three directories, the *Source* directory (containing the major implementation functions), the *ExampleScenario* directory (containing some examples which has been used to evaluate the performance of the enforcer), and the *Images* directory (containing the illustrative images).
- The Source directory contains source files
  - Automata.py which contains all the functionalities related to defining the automaton and operations on the automaton;
  - Enforcer.py which implements the bounded-memory enforcer;
  - EnforcerEval.py which evaluates our enforcer with respect to the ideal enforcer.
- The ExampleScenario directory contains four example scenarios contained in the following directories, which have been used for evaluating performances:
  - Logging_AV
  - ManualMode_AV
  - CriticalSectionProblem 
  - Lock
  
## Example Properties
#### Autonomous Vehicle: An autonomous vehicle (AV ) or a self-driving car is a vehicle that is capable of sensing its environment and moving safely with little or no human intervention. They rely on sensors, actuators, complex algorithms, machine learning systems, and powerful processors to execute software. Autonomous vehicles create and maintain a map of their surroundings based on a variety of sensors situated in different parts of the vehicle. Sophisticated software processes all the sensory input, plots a path, and sends instructions to the car’s actuators, which control acceleration, braking, and steering. Hard-coded rules, obstacle avoidance algorithms, predictive modeling, and object recognition help the software follow traffic rules and navigate obstacles.

Let us consider two example scenarios in autonomous vehicles for measuring the performance of our bounded-memory runtime enforcer.
 
1. Logging in AV: The first example scenario, used to evaluate the performance of our enforcer, contained in the Logging_AV directory, is related to logging of steering commands in Autonomous Vehicle (AV) required for simulations in the lab for future autonomous functions. The path planning steering commands like Move Left, Move Right, Move Forward, and Stop are logged for better testing and validation solutions, each time it is issued. However, due to memory constraints in AV, the data (event) is logged to a remote location. But, logging each event, every time it is issued, to a remote location is difficult. Thus, let’s consider the requirement, “*Logging of path planning steering commands should be done, when the vehicle reaches a Stop state*”, on the remote logging application to manage the overhead. Below figure presents the automaton of the proposed property. Location Start is the initial and Stop is the only accepting location, which when reached, starts the logging of steering commands. Thus, the enforcer for the above property must buffer the steering commands into a buffer without logging it to a remote location, until Stop command is issued. Once it issues a Stop command, it can “flush” its buffer to a remote location. The performance summary of this example scenario is included in the Logging_AV directory.
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/Logging_AV.png" width="250" height="250">
</p>

2. Switching to manual driving mode in autonomous vehicle: The second example scenario, used to evaluate the performance of our enforcer, contained in the ManualMode_AV directory is related to switching a vehicle driving in an autonomous driving mode to a manual driving mode in Autonomous Vehicles. According to the present inventions, when the driver presses the “manual” mode button to switch a vehicle driving from autonomous driving mode to a manual driving mode, the vehicle looks for certain conditions, whose satisfaction will switch the mode. These conditions can be:
  - Checking whether a driver's hand is holding a steering wheel,
  - Checking whether the driver's foot is placed on a brake pedal,
  - Checking whether the driver's gaze is facing forward.
  
Thus, let’s consider the property, “*Upon pressing of the manual mode button, the switching of manual driving mode from autonomous driving mode will be done if all the above three conditions are satisfied i.e., if the driver's hand is holding the steering wheel, his foot is on the brake pedal and his gaze is facing forward then only the mode is switched”*. Below figure presents the automaton of the proposed property, where the condition “driver's hand is holding the steering wheel” is denoted by event A, “driver's foot is placed on a brake pedal” is denoted by event B and “driver's gaze is facing forward” is denoted by event C. The performance summary of this example scenario is included in the ManualMode_AV directory.

<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/ManualMode_AV.png" width="250" height="250">
</p>

#### Concurrency is the ability of different parts or units of a program, algorithm and resources to be executed/used at the same time, without affecting the final outcome. Each hardware/software component is designed to operate correctly, i.e., to obey or to meet certain consistency rules. Concurrent use of shared resources can be a source of indeterminacy leading to issues such as deadlocks, and resource starvation.

Let us consider two example scenarios related to concurrency for measuring the performance of our bounded-memory runtime enforcer.

1. Critical Section Problem: The third example scenario, used to evaluate the performance of our enforcer, contained in the CriticalSectionProblem directory is related to critical section problem in operating systems. In concurrent programming, concurrent accesses to shared resources can lead to unexpected or erroneous behavior, so parts of the program where the shared resource is accessed ( i.e., critical section) need to be protected in ways that avoid concurrent access. It cannot be executed by more than one process at a time. So, one can write a simple property as, “*If a process wishes to enter the critical section, it must first execute the try section and wait until it acquires access to the critical section. After the process has executed its critical section and is finished with the shared resources, it can release them for other processes’ use.*”  Below figure presents the automaton of the proposed property. For the above property, every process’s program can be partitioned into five sections, resulting in five states. Program execution cycles through these four states in the order specified in the property. So, when a process wants to execute in a critical section and issues these operation requests, it executes in those operation request sections. Once the property is satisfied, (terminating with a done message; issue of done message indicates the consent of releasing of resources and the changes reflected to all) everything from buffer is flushed out and the system is ready for new set of requests. The performance summary of this example scenario is included in the CriticalSectionProblem directory.
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/CriticalSectionProblem.png" width="250" height="250">
</p> 

2. Lock: The fourth example scenario, used to evaluate the performance of our enforcer, contained in the Lock directory is related to concurrency control in transactions. Concurrency control techniques are used to ensure that the Isolation property of concurrently executing transactions is maintained. There are different concurrency control protocols e.g. lock based protocol. A lock is a variable associated with a data item that describes a status of data item with respect to possible operation that can be applied to it. They synchronize the access by concurrent transactions to the database items. Let us consider a specific requirement on the database system, “*For database items {A, B}, any transaction accessing both A and B must access A before accessing B.*” Below figure presents the automaton of the proposed property. So the data items {A, B} are released by a transaction when a commit happens, until then all operations are buffered. So, if the lock requests comes in such a way that the property is not satisfied, then these requests are buffered and lock is not acquired, but when requests comes which results in satisfaction of the above concurrency property then lock is acquired on the data items, and the buffer is flushed for new set of requests. The performance summary of this example scenario is included in the Lock directory.
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/Lock.png" width="250" height="250">
</p> 

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
