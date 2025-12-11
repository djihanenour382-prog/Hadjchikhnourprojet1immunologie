#selection
print(df["Longueur"])
#flitration (superieure a 10)
print(df[df["Longueur"] > 10])
#le Pourcentage
mean_gc = round(df["Pourcentage GC"].mean(), 3)
print(mean_gc)
#ajoute clone 
def categ(gc):
    if gc > 55:
        return "Riche"
    elif gc >= 45:
        return "Moyen"
    else:
        return "Faible"

df["Catégorie GC"] = df["Pourcentage GC"].apply(categ)
print(df)







