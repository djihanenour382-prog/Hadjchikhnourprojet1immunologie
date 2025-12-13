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
print("**********Création et Affichage**********","\n")
print(df)
#Affichage du tableau
print("opération")

# 2) Sélectionner et afficher uniquement la colonne "Longueur".
Longueur=df["Longueur"]
print(df["Longueur"],"\n")


# 3) filtrer les sequences dont la longueur est superieure a 10
Filtred_df = df[df["Longueur"]>10]
print("sequences longueur >10","\n")
print(Filtred_df)

# 4) calculer le pourcentage moyen de GC avec 3 chiffres après la virgule 
print("Calcul de la moyenne de GC")
#calculer la moyenne du pourcentage de GC 
average_gc = df["Pourcentage GC"].mean() 
#Afficher avec le formatage à 3 décimales
print(f"pourcentage moyen de GC : {average_gc:.3f}%","\n")

# 5) Ajouter une colonne "Categorie GC"
print("Ajout de la colonne 'Categorie GC'","\n")
#Fonction lambda pour categorier le pourcentage de GC
df["Categorie GC"] = df["Pourcentage GC"].apply(
    lambda x: "riche" if x > 55
    else ("moyen" if 45 <= x <= 55
    else "faible"))

print (df)
# 6) Ajouter une colonne donnant le nombre de "G" dans chaque séquence .
print ( "ajout de la clonne nobre de G","\n")
# Utiliser la méthodes .str.count() sur la clonne "séquence"
df["nombre de G"] = df["séquence"].str.count("G") 
print(df) 

# 7) Calculer l'écart-type du %GC et de la longueur des séquences.
print(" Calcul de l'Écart-type (Standard Deviation - std)","\n")
std_gc = df["Pourcentage GC"].std()
std_longueur = df["Longueur"].std()
print(f"Écart-type du Pourcentage GC : {std_gc:.2f}")
print(f"Écart-type de la Longueur : {std_longueur:.2f}")
# 8) Sauvegarder le tableau final dans un fichier CSV 
print("Sauvegarder du DataFrame dans un fichier CSV ","\n")
#Sauvegarder le DataFrame dans un fichier CSV (sans l'index)
nom_de_fichier = "analyse_séquences_adn_final.CSV"
df.to_csv ( nom_de_fichier , index=False)
print(f"Le tableau finala été sauvegarder dans {nom_de_fichier} avec succés.")




