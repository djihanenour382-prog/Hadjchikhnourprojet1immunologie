#2/selection
print(df["Longueur"])

# 5/Ajouter la colonne "Categorie GC"

# je crée d'abord une colonne vide
df["Categorie GC"] = ""

df.loc[df["Pourcentage GC"] > 55, "Categorie GC"] = "Riche"

df.loc[(df["Pourcentage GC"] >= 45) & (df["Pourcentage GC"] <= 55),"Categorie GC"] = "Moyen"

df.loc[df["Pourcentage GC"] < 45, "Categorie GC"] = "Faible"
print(df)








