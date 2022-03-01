age = int(input('Inserisci l\'età del tuo cane: '))
dogage = 0

for i in range(age):
    if i < 2:
        dogage += 10.5
    else:
        dogage += 4

print('L\'eta umana del tuo cane sarebbe: ', dogage)

