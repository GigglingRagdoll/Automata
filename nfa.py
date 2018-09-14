class NFA:
    def __init__(self, stf, F):
        ''' stf: Simplified transition function
                 A dictionary where each key has the form
                 (sigma', x) where sigma' is a subset of the alphabet
                 and x is a state and each value has the form y where
                 y is a state i.e. { ("abc", 0) : 1 }

                 Since this is a nondeterministic finite automaton the
                 value may be a list i.e. { ("a", 0) : [1,2,3] } in
                 order to introduce nondeterminism

            F: The set of final states
        '''
        self.delta = self.unpack(stf)
        self.F = F

    def unpack(self, stf):
        ''' Takes an STF and makes a valid transition function
            delta freom it
        '''
        delta = {}

        for key in stf.keys():
            symbols, state = key

            for symbol in symbols:
                condition = (symbol, state)
                delta[condition] = stf[key]

        return delta

    def validate(self, s, start=0):
        ''' Nondeterministically finds if the string s
            exists in the language described by delta
        '''
        state = start

        for c in s:
            curr = (c, state)
            nextStates = self.delta.get(curr)

            # detected nondeterminism
            if type(nextStates) == list:
                successors = []

                # have to split the nfa into branches
                for nextState in nextStates:
                    successors.append(self.validate(s[1:], start=nextState))

                # if any branch finds a solution return true
                return any(successors)

            else:
                state = nextStates

        return True if state in self.F else False

if __name__ == '__main__':
    # nondeterministic stf for the language ['ab', 'aab', 'abb']
    stf = { ('a', 0)  : [1, 2]
          , ('b', 1)  : 3
          , ('ab', 2) : 1
          }

    F = [3]

    S = ['', 'ab', 'aab', 'abb', 'abba']

    nfa = NFA(stf, F)

    for s in S:
        print(s, nfa.validate(s))

