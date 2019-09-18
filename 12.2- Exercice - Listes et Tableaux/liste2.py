# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

nb=0
plusGrand = tab[0][0]
for i in range (len(tab)):
    for j in range(len(tab[i])):
        if tab[i][j] >= plusGrand:
            plusGrand = tab[i][j]
            indiceUn = i
            indiceDeux = j
print("La valeur maximum est :",plusGrand," et elle se trouve à l'indice [ ",indiceUn," ][ ",indiceDeux," ]")


