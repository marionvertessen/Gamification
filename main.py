
import pandas as pd

influence_achiever = []
influence_player = []
influence_socialiser = []
influence_freeSpirit = []
influence_disruptor = []
influence_philanthropist = []

influence_MI = []
influence_ME = []
influence_amotI = []

"""
Cette fonction retourne une liste de score correspondant à l'élément ludique de l'entrée
"""
def score_influence (name_fichier, name_fichier2, eleve):
    #Création de la liste des scores pour chaque profil
    liste_score = []

    #On lit les données des deux fichiers d'influence et de pvalues
    data_influences = pd.read_csv(name_fichier, sep=";")
    data_pvalues = pd.read_csv(name_fichier2, sep=";")

    #On enleve la prmeière colonne qui ne sert à rien ici
    del data_pvalues['Unnamed: 0']
    del data_influences['Unnamed: 0']
    #print(data_pvalues)

    #On parcourt chaque profil et on regarde les valeurs pertinantes
    score_MI = 0
    score_ME = 0
    score_AMOT =0
    for col in data_pvalues.columns:
        #On intialise le score
        score = 0
        #On parcourt les valeurs de MI, ME et AM
        # Si la pvalues est inférieur à 0 on additionne au score l'influence correpsondante
        if data_pvalues[col][0] < 0.1 :
            score_MI += data_influences[col][0] * (eleve['micoI'] + eleve['miacI'] + eleve['mistI'])
        if data_pvalues[col][1] < 0.1 :
            score_ME += data_influences[col][1] * (eleve['meidI'] + eleve['meinI'] + eleve['mereI'])
        if data_pvalues[col][2] < 0.1:
            score_AMOT -= data_influences[col][2] * eleve['amotI']
    #print(liste_score)
    return [score_MI, score_ME, score_AMOT]

def vecteur_influence_Motivation (eleve) :
    #On calcule les différents vecteurs pour chaque type d'éléments ludiques
    vecteur_tot = []
    vecteur_tot.append(score_influence("Motivation/avatarPathCoefs.csv","Motivation/avatarpVals.csv", eleve)) #AVATARS : 0
    vecteur_tot.append(score_influence("Motivation/badgesPathCoefs.csv", "Motivation/badgespVals.csv", eleve)) #BADGES : 1
    vecteur_tot.append(score_influence("Motivation/progressPathCoefs.csv", "Motivation/progresspVals.csv", eleve)) #PROGRESS : 2
    vecteur_tot.append(score_influence("Motivation/rankingPathCoefs.csv", "Motivation/rankingpVals.csv", eleve)) #RANKING : 3
    vecteur_tot.append(score_influence("Motivation/scorePathCoefs.csv", "Motivation/scorepVals.csv", eleve)) #SCORE : 4
    vecteur_tot.append(score_influence("Motivation/timerPathCoefs.csv", "Motivation/timerpVals.csv", eleve)) #TIMER : 5
    #print(vecteur_tot)
    #Tableau des valeurs de score pour chaque type de joueur
    liste_score_joueur = []
    #On regarde pour chaque type de joueur quel sont les activités ludiques les plus adéquates

    #print(vecteur_tot)
    for k in range(len(vecteur_tot)):
        liste_score_joueur.append([k, vecteur_tot[k][0] + vecteur_tot[k][1] - vecteur_tot[k][2]])
    print(liste_score_joueur)
    liste_score_joueur.sort(key=lambda x: x[1], reverse=True)

    #print(liste_score_joueur)
    """for k in range(len(vecteur_tot[0])):
        activite = []
        for j in range(len(vecteur_tot)):
            activite.append([j, vecteur_tot[j][k]])
        activite.sort(key=lambda x: x[1], reverse=True)
        #print(activite)

        #On remplit l'influence pour le joueur associé
        liste_score_joueur.append(activite)"""

    #print(liste_score_joueur)
    return liste_score_joueur

    #On remplit les score associé à chaque joueur
    """influence_MI.append(liste_score_joueur[0])
    influence_ME.append(liste_score_joueur[1])
    influence_amotI.append(liste_score_joueur[2])"""

def vecteur_influence_Hexad (eleve) :
    #On calcule les différents vecteurs pour chaque type d'éléments ludiques
    vecteur_tot = []
    vecteur_tot.append(score_influence("Hexad/avatarPathCoefs.csv","Hexad/avatarpVals.csv", eleve)) #AVATARS : 0
    vecteur_tot.append(score_influence("Hexad/badgesPathCoefs.csv", "Hexad/badgespVals.csv", eleve)) #BADGES : 1
    vecteur_tot.append(score_influence("Hexad/progressPathCoefs.csv", "Hexad/progresspVals.csv", eleve)) #PROGRESS : 2
    vecteur_tot.append(score_influence("Hexad/rankingPathCoefs.csv", "Hexad/rankingpVals.csv", eleve)) #RANKING : 3
    vecteur_tot.append(score_influence("Hexad/scorePathCoefs.csv", "Hexad/scorepVals.csv", eleve)) #SCORE : 4
    vecteur_tot.append(score_influence("Hexad/timerPathCoefs.csv", "Hexad/timerpVals.csv", eleve)) #TIMER : 5

    #Tableau des valeurs de score pour chaque type de joueur
    liste_score_joueur = []
    #On regarde pour chaque type de joueur quel sont les activités ludiques les plus adéquates
    for k in range(len(vecteur_tot[0])):
        activite = []
        for j in range(len(vecteur_tot)):
            activite.append([j, vecteur_tot[j][k]])
        activite.sort(key=lambda x: x[1], reverse=True)
        #print(activite)

        #On remplit l'influence pour le joueur associé
        liste_score_joueur.append(activite)

    #On remplace les nombre par des nom

    #On remplit les score associé à chaque joueur
    """influence_achiever.append(liste_score_joueur[0])
    influence_player.append(liste_score_joueur[1])
    influence_socialiser.append(liste_score_joueur[2])
    influence_freeSpirit.append(liste_score_joueur[3])
    influence_disruptor.append(liste_score_joueur [4])
    influence_philanthropist.append(liste_score_joueur [5])"""

def replace_name_element (liste):
    for k in range (len(liste)):
        if liste[k][0] == 0:
            liste[k][0] = "Avatar"
        if liste[k][0] == 1:
            liste[k][0] = "Badge"
        if liste[k][0] == 2:
            liste[k][0] = "Progress"
        if liste[k][0] == 3:
            liste[k][0] = "Ranking"
        if liste[k][0] == 4:
            liste[k][0] = "Score"
        if liste[k][0] == 5:
            liste[k][0] = "Timer"
    return liste

if __name__ == '__main__':
    #On choisit un eleve
    eleves = pd.read_csv("donnees_eleves/userStats.csv", sep=";")
    for i in range(300):

        eleve = eleves.iloc[i, :]
    #print(type(eleve))
    #On lit les fichiers et on calcule
        vecteur_influence_Hexad(eleve)
        liste_test = vecteur_influence_Motivation(eleve)
        liste_test = replace_name_element(liste_test)
        print(liste_test)

    """#On replace les numero par les noms des éléments ludiques
    influence_disruptor = replace_name_element(influence_disruptor[0])
    influence_player =replace_name_element(influence_player[0])
    influence_philanthropist = replace_name_element(influence_philanthropist[0])
    influence_socialiser = replace_name_element(influence_socialiser[0])
    influence_freeSpirit = replace_name_element(influence_freeSpirit[0])
    influence_achiever = replace_name_element(influence_achiever[0])

    influence_ME = replace_name_element(influence_ME[0])
    influence_MI = replace_name_element(influence_MI[0])
    influence_amotI = replace_name_element(influence_amotI[0])"""
    # print(influence_MI)
    # print(influence_ME)
    # print(influence_amotI)







