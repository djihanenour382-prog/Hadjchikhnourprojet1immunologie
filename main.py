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

#1-Affichage du tableau
print("opération")

#2-sélectionner la colonne "longueur"
longueur = df["Longueur"]
print(longueur)

#3-Filtrer les séquences de longueur ≥ 10
df_filtre=df[df["Longueur"] > 10]
print(df_filtre)

#4-Pourcentage moyen de GC arrondi à 3 décimales
#je calcule d'abord la moyenne de la colonne Pourcentage GC
moyenne_gc = df["Pourcentage GC"].mean()
# j'arrondis la moyenne à 3 chiffres après la virgule
moyenne_gc = round(moyenne_gc, 3)
print(moyenne_gc)


