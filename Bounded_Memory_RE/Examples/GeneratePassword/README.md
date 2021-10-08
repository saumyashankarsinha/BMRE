1. Generate Password- Consider a scenario where an application generates passwords for a system, using characters and digits. Let us suppose that the generated password should meet a specific requirement which is, *“The password should start with one or more characters and end with one or more digits”*. The password is valid only if this required format condition holds. The automaton in the below figure defines this requirement φ. Let us suppose the alphabets and digits provided are {a, b, c} and {1, 2} respectively. The enforcer for φ must buffer all the characters without generating an authentic password for the user, until atleast one digit is received. Once it receives a digit, it can “flush” its buffer and provide the password.

![This is an image](https://github.com/saumyashankarsinha/BMRE/blob/main/Images/password.png)

*How to run:*
> go to Bounded_Memory_RE/Examples

> open terminal in Examples

> run *python "give path of GeneratePassword.py file"*
