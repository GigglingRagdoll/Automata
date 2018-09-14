class DFA:
    def __init__(self, simpleTransitions, finalStates):
        ''' A DFA is a 5-tuple containing 
            a set of symbols called an alphabet
            a set of states 
            a transition function 
            a set of final states contained in the set of states
            and a starting state

            We can implicitly compute all of those things by
            simply giving the transition function, the
            set of final states and assuming the start state is 0

            simpleTransitions: A dictionary where each key is a
                               2-tuple consisting of a string 
                               containing each symbol used in the
                               state and the state itself. Each
                               value is the state being mapped to
                               i.e. { ("abcd", 0) : 1 }

            finalStates: A list representing the set of final states
        '''
        self.transitions = self.convert(simpleTransitions)
        self.finalStates = finalStates

    def convert(self, simpleTransitions):
        ''' Unpacks the simplified transition function.

            Example: { ("abcd", 0) : 1 } 
                     becomes
                     { ("a", 0) : 1, ("b", 0) : 1, ("c", 0) : 1, ("d", 0) : 1 }
        '''
        conversion = {}

        for key in simpleTransitions.keys():
            symbols, state = key

            for symbol in symbols:
                conversion[(symbol, state)] = simpleTransitions[key]

        return conversion
        
    def validate(self, s):
        ''' Checks if the string s is contained in the language
            
            s: The string to be validated
        '''
        state = 0

        for c in s:
            state = self.transitions.get((c, state))

            if state == None:
                return False

        return True if state in self.finalStates else False

if __name__ == '__main__':
    from string import printable

    # checks if the lowercase substring "cool" exists in a string
    transitions = {
            # transitions from 0
            (printable, 0) : 0,
            ('c', 0)       : 1,
            # transitions from 1
            (printable, 1) : 0,
            ('o', 1)       : 2,
            # transitions from 2
            (printable, 2) : 0,
            ('o', 2)       : 3,
            # transitions from 3
            (printable, 3) : 0,
            ('l', 3)       : 4,
            # transitions from 4
            (printable, 4) : 4,
            
    }
    finals = [4]
    dfa = DFA(transitions, finals)

    S = ['cool', 'kool', 'coolio']

    for s in S:
        print(s, dfa.validate(s))

