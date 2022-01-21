from Ville import Ville
import math as m


# Récupération des Villes de puis le fichier
f = open("./instances/ListeComplete.txt")
# récupère les lignes du doc txt
lines = f.readlines()
listeVilles = []
for line in lines:
    # parse des lignes
    ville = line.split(" ")
    ville[3] = ville[3].strip('\n')

    # création ville
    city = Ville(int(ville[0]), ville[1], float(ville[2]), float(ville[3]))

    # ajout à la liste de ville la ville
    listeVilles.append(city)
f.close()


# Affichage des villes
def afficherVille():
    for ville in listeVilles:
        print(str(ville.numVille) + ' ' + str(ville.nom) + ' ' + str(ville.latitude) + ' ' + str(ville.longitude))


# calcule la distance entre deux villes
def distance(v1: Ville, v2: Ville) -> float:
    r = 6371
    x1 = m.radians(v1.longitude)
    x2 = m.radians(v2.longitude)
    y1 = m.radians(v1.latitude)
    y2 = m.radians(v2.latitude)

    distance = abs(r*m.acos( (m.sin(y1)*m.sin(y2)) + (m.cos(y1)*m.cos(y2)*m.cos(x1-x2)) ))
    return distance


# créer une tournée de ville par ordre croissants des numéros de ville
def tourneeCroissante():
    tourneCroissante = []
    i = 1
    for ville in listeVilles:
        if(ville.numVille == i):
            tourneCroissante.append(ville)
        i += 1
    return tourneCroissante


# affiche le numero des villes de la tournée passée en paramètre
def afficherTournee(tournees : Ville):
    temp = []
    for tournee in tournees:
        temp.append(tournee.numVille)
    print("tournée croissante ", temp)


# calcule la distance totale d'une tournée
def cout(tournees) -> float:
    cout = 0
    i = 0

    for i in range(len(tournees)):
        if(i < (len(tournees)-1)):
            cout += distance(tournees[i], tournees[i+1])
            print("itération numéro", i ,cout)
        else:
            return cout

    return cout


## Appel des fonctions ##
# afficherVille()
# print("distance entre les deux villes : " , distance(listeVilles[0], listeVilles[1]))
# print(tourneeCroissante())
# afficherTournee(listeVilles)
# print(cout(listeVilles))