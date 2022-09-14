from msvcrt import getch

first = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print("\nEntrez les éléments de la première matrice :")
for i in range(len(first)):
   for j in range(len(first[0])):
       first[i][j] = int(input(">"))

second = [[0,0,0],
          [0,0,0],
          [0,0,0]]

print("\nEntrez les éléments de la seconde matrice :")
for i in range(len(first)):
   for j in range(len(first[0])):
       second[i][j] = int(input(">"))

add = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(first)):
   for j in range(len(first[0])):
       add[i][j] = first[i][j] + second[i][j]

print("\nRésultat de l'addition des deux matrices :\n")
for r in add:
   print(r)
getch()
