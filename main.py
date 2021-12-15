
import pandas as pd


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

    #On parcourt chaque profil et on regarde les valeurs pertinantes
    score_MI = 0
    score_ME = 0
    score_AMOT = 0
    for ligne in data_pvalues.index:
        #On intialise le score
        score = 0
        #On parcourt les valeurs de MI, ME et AM
        # Si la pvalues est inférieur à 0 on additionne au score l'influence correpsondante
        if data_pvalues["MI"][ligne] < 0.1:
            score_MI += data_influences['MI'][ligne]
        if data_pvalues["ME"][ligne] < 0.1:
            score_ME += data_influences['ME'][ligne]
        if data_pvalues["amotI"][ligne] < 0.1:
            score_AMOT += data_influences['amotI'][ligne] * eleve['amotI']
    score_MI *= (eleve['micoI'] + eleve['miacI'] + eleve['mistI'])/3
    score_ME *= (eleve['meidI'] + eleve['meinI'] + eleve['mereI'])/3
    #print(liste_score)
    return [score_MI, score_ME, score_AMOT]

def score_influence_hexad (name_fichier, name_fichier2, eleve):
    #Création de la liste des scores pour chaque profil
    liste_score = []

    #On lit les données des deux fichiers d'influence et de pvalues
    data_influences = pd.read_csv(name_fichier, sep=";")
    data_pvalues = pd.read_csv(name_fichier2, sep=";")

    #On enleve la prmeière colonne qui ne sert à rien ici
    del data_pvalues['Unnamed: 0']
    del data_influences['Unnamed: 0']

    #On parcourt chaque profil et on regarde les valeurs pertinantes
    score_achiever = 0
    score_player = 0
    score_socialiser = 0
    score_freespirit = 0
    score_disruptor = 0
    score_philantropist = 0

    for ligne in data_pvalues.index:
        #On intialise le score
        score = 0
        #On parcourt les valeurs de MI, ME et AM
        # Si la pvalues est inférieur à 0 on additionne au score l'influence correpsondante
        if data_pvalues["achiever"][ligne] < 0.1:
            score_achiever += data_influences['achiever'][ligne]
        if data_pvalues["player"][ligne] < 0.1:
            score_player += data_influences['player'][ligne]
        if data_pvalues["socialiser"][ligne] < 0.1:
            score_socialiser += data_influences['socialiser'][ligne]
        if data_pvalues["freeSpirit"][ligne] < 0.1:
            score_freespirit += data_influences['freeSpirit'][ligne]
        if data_pvalues["disruptor"][ligne] < 0.1:
            score_disruptor += data_influences['disruptor'][ligne]
        if data_pvalues["philanthropist"][ligne] < 0.1:
            score_philantropist += data_influences['philanthropist'][ligne]
    score_achiever *= eleve['achiever']
    score_player *= eleve['player']
    score_socialiser *= eleve['socialiser']
    score_freespirit *= eleve['freeSpirit']
    score_disruptor *= eleve['disruptor']
    score_philantropist *= eleve['philanthropist']
    #print(liste_score)
    return [score_achiever, score_player, score_socialiser, score_freespirit, score_disruptor, score_philantropist]

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
        # liste_score_joueur.append([k, vecteur_tot[k][2]])
    # print(liste_score_joueur)
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

def vecteur_influence_Hexad (eleve) :
    #On calcule les différents vecteurs pour chaque type d'éléments ludiques
    vecteur_tot = []
    vecteur_tot.append(score_influence_hexad("Hexad/avatarPathCoefs.csv","Hexad/avatarpVals.csv", eleve)) #AVATARS : 0
    vecteur_tot.append(score_influence_hexad("Hexad/badgesPathCoefs.csv", "Hexad/badgespVals.csv", eleve)) #BADGES : 1
    vecteur_tot.append(score_influence_hexad("Hexad/progressPathCoefs.csv", "Hexad/progresspVals.csv", eleve)) #PROGRESS : 2
    vecteur_tot.append(score_influence_hexad("Hexad/rankingPathCoefs.csv", "Hexad/rankingpVals.csv", eleve)) #RANKING : 3
    vecteur_tot.append(score_influence_hexad("Hexad/scorePathCoefs.csv", "Hexad/scorepVals.csv", eleve)) #SCORE : 4
    vecteur_tot.append(score_influence_hexad("Hexad/timerPathCoefs.csv", "Hexad/timerpVals.csv", eleve)) #TIMER : 5

    #Tableau des valeurs de score pour chaque type de joueur
    liste_score_joueur = []
    #On regarde pour chaque type de joueur quel sont les activités ludiques les plus adéquates
    for k in range(len(vecteur_tot[0])):
        liste_score_joueur.append([k, vecteur_tot[k][0] + vecteur_tot[k][1] - vecteur_tot[k][2]])

    liste_score_joueur.sort(key=lambda x: x[1], reverse=True)
    return liste_score_joueur


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
    """for i in range(300):
        eleve = eleves.iloc[i, :]
    #print(type(eleve))
    #On lit les fichiers et on calcule
        #vecteur_influence_Hexad(eleve)
        liste_motiv = vecteur_influence_Motivation(eleve)
        liste_motiv = replace_name_element(liste_motiv)
        # print(liste_motiv)
        liste_hexad = vecteur_influence_Hexad(eleve)
        liste_hexad = replace_name_element(liste_hexad)
        print(liste_hexad)"""
    eleve = eleves.iloc[0,:]
    liste_motiv = vecteur_influence_Motivation(eleve)
    liste_motiv = replace_name_element(liste_motiv)
    print(liste_motiv)
    # print(liste_motiv)
    liste_hexad = vecteur_influence_Hexad(eleve)
    liste_hexad = replace_name_element(liste_hexad)
    print(liste_hexad)







