#####Imports####################
from copy import deepcopy
###############################


def ts(x):
    return tuple(sorted(x))

class DFA:
    
    def __init__(self, S, Q, q0, F, d, e = ('.l',)):
        self.S = S
        self.Q = Q
        self.q0 = q0
        self.q = q0
        self.F = F
        self.d = d
        self.e = e # empty word

        self.reset()
        

    def isEmpty(self):
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for a in self.S:
                q = self.d(node, a)
                if q and q not in visited:
                    dfs(q)
                    
        dfs(self.q0)
        return all(not self.F(q) for q in visited)


    def reset(self, q = None):
        
        q = q or self.q0
        
        self.q = q


    def step1(self, a):
        #if a != '' and a != self.e:
        if a and a not in self.e:
            self.q = self.d(self.q, a)
            return self.q
            
    def makeInit(self, q):
        #if a != '' and a != self.e:
        #if a and a not in self.e:
        self.q0 = q
        
            
    def step(self, a):
        #if a != '' and a != self.e:
        if a and a not in self.e:
            self.q = self.d(self.q, a)

    def isInAcceptingState(self):
        return self.F(self.q)


    def accepts(self, w):

        if not w or w == self.e:
            return self.F(self.q0)
            
        #if '.d' in w: 
        if w == ('.d',): 
            return False
        
        q = self.q
        
        self.reset()

        for a in w:
            self.step(a)
            
        ret = self.isInAcceptingState()
        
        self.reset(q)

        return ret

