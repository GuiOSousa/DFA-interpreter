def step(state, step, deltas):
    auxDeltas = []

    for delta in deltas:
        if (delta[0] == state):
            auxDeltas.append(delta)

    if auxDeltas == []:
        print('Estado não encontrado')

    for delta in auxDeltas:
        if(delta[1] == step):
            print(f"{delta[0]} -> {delta[2]}")
            return delta[2]
    print('Função delta incompleta.')
    return state

def extendedDeltaFunction(initialState, deltas, word):
    actualState = initialState

    for s in word:
        actualState = step(actualState, s, deltas)
    
    return actualState