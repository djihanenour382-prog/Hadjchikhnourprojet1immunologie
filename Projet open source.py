#HADJ CHIKH Nour Djihane , MASTER 1 Immunologie , 13/12/2025
#Les membres du groupe
#MENIRI Chaima
#YAGOUB Mohammed El Amine 
#ARBI Sihem
#ARBI Hayat

import pandas as pd 
#Données: séquences ADN, Longueur, Pourcentage 
data={
"séquence":["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
"Longueur":[12,12,12,10,11,10,10],
"Pourcentage GC":[50,66.67,58.33,40,45.45,60,50]
}
# 1)Création d'un DataFrame(tableau pandas)
df=pd.DataFrame(data)
print("**********Création et Affichage**********")
print(df)
#Affichage du tableau
print("opération")

# 2) Sélectionner et afficher uniquement la colonne "Longueur".
Longueur=df["Longueur"]
print(df["Longueur"])

# 3) filtrer les sequences dont la longueur est superieure a 10
Filtred_df = df[df["Longueur"]>10]
print("sequences longueur >10")
print(Filtred_df)

# 4) calculer le pourcentage moyen de GC avec 3 chiffres après la virgule 
print("Calcul de la moyenne de GC")
#calculer la moyenne du pourcentage de GC 
average_gc = df["Pourcentage GC"].mean() 
#Afficher avec le formatage à 3 décimales
print(f"pourcentage moyen de GC : {average_gc:.3f}%")

# 5) Ajouter une colonne "Categorie GC"
print("Ajout de la colonne 'Categorie GC'")
#Fonction lambda pour categorier le pourcentage de GC
df["Categorie GC"] = df["Pourcentage GC"].apply(



