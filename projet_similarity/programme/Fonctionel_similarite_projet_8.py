#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:51:27 2023

@author: gordibus
"""

from sklearn.neighbors import DistanceMetric
from typing import List, Dict
from sklearn.feature_extraction.text import CountVectorizer
# import glob
import json

def stocker(chemin, contenu):
    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()
    return chemin

def calculer_distances(textes:List[str], metriques:List[str], noms_textes:List[str]) -> Dict:
    distances = {}
    for i in range(len(textes)):
        for j in range(i+1, len(textes)):
            for systeme in metriques:
                dist = DistanceMetric.get_metric(systeme)
                V = CountVectorizer(analyzer='word')
                X = V.fit_transform([textes[i], textes[j]]).toarray()
                distance_tab = dist.pairwise(X).tolist()
                if systeme not in distances:
                    distances[systeme] = []
                result = {noms_textes[i]: textes[i], noms_textes[j]: textes[j], "resultat": distance_tab}
                distances[systeme].append(result)
    return distances

# str3 = "Sur la planete Mars il n'y a pas de plan B pour le climat" 
# str4 = "Sur la planete Mar il n'y a pas de plan b pour le clima"
# V = CountVectorizer(analyzer='word')
# X = V.fit_transform([str3, str4]).toarray()
# distance_tab=dist.pairwise(X)
# print(distance_tab)

    ###MAIN
# for path_ in pathe_corpora
dist = DistanceMetric.get_metric("jaccard")
# path_corpora1 ="../DATA/traduction_NH*.txt"
# path_corpora2 ="../DATA/traduction_NH_reverso.txt"
# Y = CountVectorizer(analyzer='word')
# Z = Y.fit_transform([path_corpora1, path_corpora2]).toarray()
# print (path_corpora1)
# distance_tabs=dist.pairwise(Z)
# print (distance_tabs)
            ###Les variable ci dessus ne fonctionne pas comme je l'exige.
            
            ###Donnée exemple des phrase + Stockage des données en json
phrase_teste1="ceci est un test, néanmoins je ne pense pas que cela fonctionne ?"
phrase_teste2="ceci et un test, cependant sa fonctionnalité m'est méconnu"
phrase_teste3 = "Sur la planète Mars il n'y a pas de plan B pour le climat"
phrase_teste4 = "Sur la planete Mar il n'y a pas de plan b pour le clima"
V = CountVectorizer(analyzer='word')
X = V.fit_transform([phrase_teste1, phrase_teste2]).toarray()
O = CountVectorizer(analyzer='word')
P = O.fit_transform([phrase_teste3, phrase_teste4]).toarray()
distance_tab=dist.pairwise(X)
distance_tabs=dist.pairwise(P)
### Ne fonctionne pas
# distance_tab=dist.pairwise[X,P]
print(distance_tab)
print(distance_tabs)

if __name__ == '__main__':
    phrase_teste1="ceci est un test, néanmoins je ne pense pas que cela fonctionne ?"
    phrase_teste2="ceci et un test, cependant sa fonctionnalité m'est méconnu"
    phrase_teste3 = "Sur la planète Mars il n'y a pas de plan B pour le climat"
    phrase_teste4 = "Sur la planete Mar il n'y a pas de plan b pour le clima"

    textes = [phrase_teste1, phrase_teste2, phrase_teste3, phrase_teste4]
    noms_textes = ["phrase_teste1", "phrase_teste2", "phrase_teste3", "sphrase_teste4"]
    metriques = ["euclidean", "jaccard", "manhattan", "chebyshev","minkowski" ]

    distances_tabuse = calculer_distances(textes, metriques, noms_textes)

    print(distances_tabuse)
    ### Enregistrer les résultats dans un fichier JSON
    stocker("distances_metrique.json", distances_tabuse)
