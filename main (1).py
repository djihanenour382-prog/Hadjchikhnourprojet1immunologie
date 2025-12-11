import pandas as pd
#Donées:séquence ADN, Longueur ,Pourcentage
data={
"séquence":["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
"Longueur":[12,12,12,10,11,10,10],
"Pourcentage GC":[50,66.67,58.33,40,45.45,60,50]
}
#Création d'un DataFrame(tableau pandas)
df=pd.DataFrame(data)
print("*************Création et Affichage **************","\n")
print(df)
#Affichage du tableau
print("opération")
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






