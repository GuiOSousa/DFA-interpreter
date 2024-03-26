from convertion import convertDelta
from step import extendedDeltaFunction

alphabet = input('Insira seu alfabeto: ').split(' ')
states = input('Insira seus estados: ').split(' ')

deltaString = input('Funcoes delta: ')
deltas = convertDelta(deltaString, states, alphabet)

startState = input('Estado inicial: ')
finalStates = input ('Estados finais: ').split(' ')
actualState = startState

word = input('Insira a String desejada: ')

actualState = extendedDeltaFunction(startState, deltas, word)
    
if (actualState in finalStates):
    print('String pertence à linguagem')
else:
    print('String não pertence à linguagem')