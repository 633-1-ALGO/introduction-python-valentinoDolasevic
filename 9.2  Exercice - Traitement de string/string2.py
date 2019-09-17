# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

# Nombre d'occurence du mot exemple
print(texte.count('exemple'))



n = len(texte)
n1 = len('est')
n2 = len('représente')
i = 0
while i <= n - n1:
    if 'est' == texte[i:i + n1]:
        texte = texte[:i] + 'représente' + texte[i + n1:]
        n += n2
    i += 1
print(texte)



