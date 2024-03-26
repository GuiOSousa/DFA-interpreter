import numpy as np

def convertDelta(string, states, alphabet):
    convertedDeltas = string.split(' ')
    existentStates = []

    for delta in convertedDeltas:
        existentStates.append(delta[0])
        existentStates.append(delta[2])

    existentStates = set(existentStates)
    existentStates = list(existentStates)

    if (sorted(existentStates) != sorted(states)):
        print('Existem estados não incluídos no seu autômato.')

    for state in existentStates:
        existentSteps = []
        auxAlphabet = alphabet.copy()

        for delta in convertedDeltas:
            if (delta[0] == state):
                existentSteps.append(delta[1])

        for step in existentSteps:
            auxAlphabet.remove(step)

        if (auxAlphabet != []):
            print(f'O estado {state} não possue os passos:')
            for m in auxAlphabet:
                print(state, m, '_')
    
    return convertedDeltas