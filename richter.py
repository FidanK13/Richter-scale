tnt=4.184 * 10 ** 6
while True:
    richter=input('richter shkalasi ile eded daxil edin')
    if richter.isnumeric():
        richter=float(richter)
        energy = 10 ** ( 1.5 * richter + 4.8)
        print('Coil = ', energy)
        compare=energy/tnt
        print('TNT ile chekisi = ', compare)
    else:
        print('reqem daxil edin')
        continue
    davam = input('davam etmek isteyirsiniz? y/n')
    if davam == 'y':
        continue
    else: # davam == 'n':
        break