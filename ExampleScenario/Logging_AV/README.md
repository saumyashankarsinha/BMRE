## Logging steering commands in AV:
Property:
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/Logging_AV.png">
</p>
The output of the enforcer when input taken is "rrllffs":
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/output_Logging_AV.png">
</p> 

Evaluation of performance of bounded enforcer against ideal/ubbounded enforcer:
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/Logging_AV_Performance.png">
</p> 
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/Logging_AV_Performance_csv.png">
</p> 

Note: The columns of the above performance evaluation table represent the length of the input sequence, total (online) time taken by the ideal/unbounded enforcer, average time taken by the ideal enforcer per event, number of times clean function is invoked by the bounded enforcer, total (online) time taken by the bounded enforcer, total time spent in cleaning the buffer, and time taken by the bounded enforcer excluding time taken by the clean function in seconds respectively.

From the table one can observe that the time taken by the unbounded/ideal and the bounded enforcer (in columns C and F of above table) increases linearly with the trace length (by considering traces such that the no. of times clean is invoked increases linearly). Also, when comparing the time taken by the bounded and unbounded enforcer, the additional time (T2-T1 in column H) taken by the bounded enforcer is similar to the time taken by the ideal/unbounded enforcer. Thus, when cleaning the buffer is not necessary (e.g, for some input traces/when the buffer size is large), the performance of the bounded enforcer is similar to the unbounded/ideal enforcer. The time taken for cleaning (per call on average) is 0.0306652 ms which is low/reasonable.


## Determining memory bounds with probabilistic analysis
We perform a probabilistic analysis on the buffer size for the current case
study of logging of steering commands in AVs, using stationary distributions
of Markov Chains s.t., the enforcer will eventually utilize N memory units
with a given probability  that the output of the bounded enforcer is equal to the
output of the ideal enforcer.

Python file ComputingProbabilities.py contains the implementation for the same. 
- The function CalProbab computes the probabilities of taking transitions (na,nn,aa,an) and returns all those four probabilities. 
- These probabilities are utilized by function Compute_N which computes the size of the bounded buffer for a given probability.
- The computed N is taken as the size of the bounded enforcer with the given probability that the output of bounded = output of unbounded enforcer.
-  Function enforcers runs both the bounded (N) and unbounded enforcers for a given input and finds that the output of bounded = output of unbounded enforcer for a given probability.
