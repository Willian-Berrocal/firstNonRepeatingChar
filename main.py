# Este programa devuelve el primer char que no se repite dentro de un string
# El tiempo de ejecucion es O(n), siendo n el len del input

s = 'streSS'

nonRep = ''

alphaCount = [0] * 95
alphaOrder = [-1] * 95
auxOrder = 0

for c in s.upper():
    alphaCount[ord(c) - 32] += 1
    alphaOrder[ord(c) - 32] = auxOrder
    auxOrder += 1

minOrder = len(s)

for i in range(0, 95):
    if alphaCount[i] == 1:
        if alphaOrder[i] < minOrder:
            nonRep = chr(i+32)
            minOrder = alphaOrder[i]

for c in s:
    if c == nonRep.upper() or c == nonRep.lower():
        print(c)
