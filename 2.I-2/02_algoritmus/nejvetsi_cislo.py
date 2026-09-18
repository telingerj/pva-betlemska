#  najděte v seznamu čísel největší, vypište největší číslo a jeho pozici
l = [8, 4, 1, 2, 5, 4, 7, 9, 6, 3, 10, 1]

#  popište algoritmus, pak ho implementujte

# proměnná pozice = 0
# pro i od 0 do délky l
#   když l[i] > l[pozice]
#      ulož číslo i do pozice
# vypiš l[pozice] a pozice

pozice = 0
for i in range(len(l)):
    if l[i] > l[pozice]:
        pozice = i
print(l[pozice], pozice)
