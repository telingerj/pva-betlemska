cisla = [0, 5, 8, 7, 4, 9, 6, 3, 2, 1]
#TODO: určit, na kterých indexech je nevětší a nejmenší číslo z celého seznamu

nejvetsi_index = 0
nejmensi_index = 0
for i in range(len(cisla)):
    if cisla[i] > cisla[nejvetsi_index]:  # je číslo na které koukám větší než zatím největší číslo?
        nejvetsi_index = i
    if cisla[i] < cisla[nejmensi_index]:
        nejmensi_index = i


print("největší číslo je na indexu", nejvetsi_index)
print("nejmenší číslo je na indexu", nejmensi_index)
