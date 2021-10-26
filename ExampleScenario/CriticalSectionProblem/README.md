## Critical Section Problem:
Property:
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/CriticalSectionProblem.png">
</p>

The output of the enforcer when input taken is "tttttttcd":
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/csp_output.png">
</p> 

Evaluation of performance of bounded enforcer against ideal/ubbounded enforcer:
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/csp_performance.png">
</p> 
<p align="center">
  <img src="https://github.com/saumyashankarsinha/BMRE/blob/main/Images/csp_performance_csv.png">
</p> 

Note: The columns of the above performance evaluation table represent the length of the input sequence, total (online) time taken by the ideal/unbounded enforcer, average time taken by the ideal enforcer per event, number of times clean function is invoked by the bounded enforcer, total (online) time taken by the bounded enforcer, total time spent in cleaning the buffer, and time taken by the bounded enforcer excluding time taken by the clean function in seconds respectively.

From the table one can observe that the time taken by the unbounded/ideal and the bounded enforcer (in columns C and F of above table) increases linearly with the trace length (by considering traces such that the no. of times clean is invoked increases linearly). Also, when comparing the time taken by the bounded and unbounded enforcer, the additional time (T2-T1 in column H) taken by the bounded enforcer is similar to the time taken by the ideal/unbounded enforcer. Thus, when cleaning the buffer is not necessary (e.g, for some input traces/when the buffer size is large), the performance of the bounded enforcer is similar to the unbounded/ideal enforcer. The time taken for cleaning (per call on average) is 0.0048 ms which is low/reasonable.
