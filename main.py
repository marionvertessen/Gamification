
import pandas as pd
from scipy import stats

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
        #On parcourt les valeurs de MI, ME et AM
        # Si la pvalues est inférieur à 0 on additionne au score l'influence correpsondante
        if ligne <2:
            if data_pvalues["MI"][ligne] < 0.1:
                score_MI += data_influences['MI'][ligne]
            if data_pvalues["ME"][ligne] < 0.1:
                score_ME += data_influences['ME'][ligne]
            if data_pvalues["amotI"][ligne] < 0.1:
                score_AMOT += data_influences['amotI'][ligne] * eleve['amotI']
        else :
            if data_pvalues["MI"][ligne] < 0.1:
                score_MI -= data_influences['MI'][ligne]
            if data_pvalues["ME"][ligne] < 0.1:
                score_ME -= data_influences['ME'][ligne]
            if data_pvalues["amotI"][ligne] < 0.1:
                score_AMOT -= data_influences['amotI'][ligne] * eleve['amotI']
    score_MI *= (eleve['micoI'] + eleve['miacI'] + eleve['mistI'])
    score_ME *= (eleve['meidI'] + eleve['meinI'] + eleve['mereI'])
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
        if ligne < 2:
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
        else :
            if data_pvalues["achiever"][ligne] < 0.1:
                score_achiever -= data_influences['achiever'][ligne]
            if data_pvalues["player"][ligne] < 0.1:
                score_player -= data_influences['player'][ligne]
            if data_pvalues["socialiser"][ligne] < 0.1:
                score_socialiser -= data_influences['socialiser'][ligne]
            if data_pvalues["freeSpirit"][ligne] < 0.1:
                score_freespirit -= data_influences['freeSpirit'][ligne]
            if data_pvalues["disruptor"][ligne] < 0.1:
                score_disruptor -= data_influences['disruptor'][ligne]
            if data_pvalues["philanthropist"][ligne] < 0.1:
                score_philantropist -= data_influences['philanthropist'][ligne]
    score_achiever *= eleve['achiever']
    score_player *= eleve['player']
    score_socialiser *= eleve['socialiser']
    score_freespirit *= eleve['freeSpirit']
    score_disruptor *= eleve['disruptor']
    score_philantropist *= eleve['philanthropist']
    #print ([score_achiever, score_player, score_socialiser, score_freespirit, score_disruptor, score_philantropist])
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
        liste_score_joueur.append([k, vecteur_tot[k][0] + vecteur_tot[k][1] + vecteur_tot[k][2]])
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
    #print(vecteur_tot)
    for k in range(len(vecteur_tot)):
        liste_score_joueur.append([k, vecteur_tot[k][0] + vecteur_tot[k][1] + vecteur_tot[k][2] + vecteur_tot[k][3] + vecteur_tot[k][4] + vecteur_tot[k][5]])

    liste_score_joueur.sort(key=lambda x: x[1], reverse=True)
    return liste_score_joueur


def replace_name_element (liste):
    for k in range (len(liste)):
        if liste[k][0] == 0:
            liste[k][0] = "avatar"
        if liste[k][0] == 1:
            liste[k][0] = "badge"
        if liste[k][0] == 2:
            liste[k][0] = "progress"
        if liste[k][0] == 3:
            liste[k][0] = "ranking"
        if liste[k][0] == 4:
            liste[k][0] = "score"
        if liste[k][0] == 5:
            liste[k][0] = "timer"
    return liste

def algo_adaptation (vecteur_hexad, vecteur_motivation):
    score_pos = []
    score_medium = []
    score_negatif = []
    for k in range(len(vecteur_hexad)):
        nameH = vecteur_hexad[k][0]
        scoreH = vecteur_hexad[k][1]
        for i in range (len(vecteur_motivation)):
            nameM = vecteur_motivation[i][0]
            scoreM = vecteur_motivation[i][1]
            if nameM == nameH :
                if scoreM >= 0 and scoreH >=0:
                    score = scoreM + scoreH
                    score_pos.append([nameH, score])
                elif scoreM * scoreH < 0 :
                    score = scoreM + scoreH
                    score_medium.append([nameH, score])
                else :
                    score = scoreM + scoreH
                    score_negatif.append([nameH, score])
    if len(score_pos) != 0 :
        score_max = score_pos[0][1]
        elementF = score_pos[0][0]
        for element in score_pos:
            if element[1] > score_max:
                elementF = element[0]
    elif len(score_medium) != 0 :
        score_max = score_medium[0][1]
        elementF = score_medium[0][0]
        for element in score_medium:
            if element[1] > score_max:
                elementF = element[0]
    else :
        score_max = score_negatif[0][1]
        elementF = score_negatif[0][0]
        for element in score_negatif:
            if element[1] > score_max:
                elementF = element[0]
    return elementF

def algo_adaptation2 (vecteur_hexad, vecteur_motivation):
    score_max = -1000000
    element = vecteur_hexad[0][0]
    for k in range (len(vecteur_hexad)):
        for i in range(len(vecteur_motivation)):
            if vecteur_hexad[k][0] == vecteur_motivation[k][0]:
                if vecteur_hexad[k][1] + vecteur_motivation[i][1] > score_max:
                    element = vecteur_hexad[k][0]
                    score_max = 0.7*vecteur_hexad[k][1] + 0.3*vecteur_motivation[i][1]
    return element

def algo_anti_adaptation (vecteur_hexad, vecteur_motivation):
    score_min = +1000000
    element = vecteur_hexad[0][0]
    for k in range (len(vecteur_hexad)):
        for i in range(len(vecteur_motivation)):
            if vecteur_hexad[k][0] == vecteur_motivation[k][0]:
                if vecteur_hexad[k][1] + vecteur_motivation[i][1] < score_min:
                    element = vecteur_hexad[k][0]
                    score_max = vecteur_hexad[k][1] + vecteur_motivation[i][1]
    return element

def groupe ():
    eleves = pd.read_csv("donnees_eleves/userStats.csv", sep=";")
    groupe_prop_ok = []
    groupe_prop_not_ok = []
    for i in range(len(eleves['User'])):
        eleve = eleves.iloc[i, :]
        liste_motiv = vecteur_influence_Motivation(eleve)
        liste_motiv = replace_name_element(liste_motiv)
        liste_hexad = vecteur_influence_Hexad(eleve)
        liste_hexad = replace_name_element(liste_hexad)
        #element = algo_adaptation(liste_hexad, liste_motiv)
        element = algo_adaptation2(liste_hexad, liste_motiv)
        anti_element = algo_anti_adaptation(liste_hexad, liste_motiv)
        #print(element)
        #print(eleve['GameElement'])
        #print()
        if element == eleve['GameElement'] :
            groupe_prop_ok.append(eleve)
        else :
            """if anti_element == eleve['GameElement']:
                groupe_prop_not_ok.append(eleve)"""
            groupe_prop_not_ok.append(eleve)
    print(len(groupe_prop_ok))
    print(len(groupe_prop_not_ok))
    return groupe_prop_ok, groupe_prop_not_ok



def satisfaction (eleve):
    ratio_question = int(eleve['CorrectCount']) / int(eleve['QuestionCount'])
    #print(ratio_question)
    ratio_quizz = int(eleve['PassedQuizCount']) / int(eleve['QuizCount'])
    #print(ratio_quizz)
    time_eleve = eleve['Time'].split(':')
    time = int(time_eleve[0])*3600 + int(time_eleve[1])*60 + int(time_eleve[2])
    ratio_time = time / 11867
    #print(ratio_time)
    somme_mot = int(eleve['micoVar']) + int(eleve['miacVar']) + int(eleve['mistVar']) + int(eleve['meidVar']) + int(eleve['meinVar']) + int(eleve['mereVar']) - int(eleve['amotVar'])
    #print(somme_mot)
    ratio_mot = (somme_mot + 46) / 94
    #print(ratio_mot)
    #return (ratio_time + ratio_quizz + ratio_question + ratio_mot) / 4
    return somme_mot

def calcul_ratio_moyen (groupe):
    somme = 0
    liste = []
    for k in range (len(groupe)):
        somme = somme + satisfaction(groupe[k])
        liste.append(satisfaction(groupe[k]))
    return somme / len(groupe), liste

def test_t (list_satisfaction_ok, list_satisfaction_not_ok):
    test = stats.ttest_ind(list_satisfaction_ok, list_satisfaction_not_ok, equal_var=True)
    print(test)


if __name__ == '__main__':
    groupe_prop_ok, groupe_prop_not_ok = groupe()
    moyenne_groupe_ok, list_ok = calcul_ratio_moyen(groupe_prop_ok)
    print(moyenne_groupe_ok)
    moyenne_groupe_not_ok, list_not_ok = calcul_ratio_moyen(groupe_prop_not_ok)
    print(moyenne_groupe_not_ok)
    test_t(list_ok, list_not_ok)
    """eleves = pd.read_csv("donnees_eleves/userStats.csv", sep=";")
    for i in range(len(eleves['User'])) :
        eleve = eleves.iloc[i, :]
        sati = satisfaction(eleve)
        if sati < 0 or sati >1 :
            print("PROBLEME")"""

    """#On choisit un eleve
    eleves = pd.read_csv("donnees_eleves/userStats.csv", sep=";")
    print(len(eleves['User']))
    for i in range(300):
        eleve = eleves.iloc[i, :]
    #print(type(eleve))
    #On lit les fichiers et on calcule
        #vecteur_influence_Hexad(eleve)
        liste_motiv = vecteur_influence_Motivation(eleve)
        liste_motiv = replace_name_element(liste_motiv)
        #print(liste_motiv)
        liste_hexad = vecteur_influence_Hexad(eleve)
        liste_hexad = replace_name_element(liste_hexad)
        #print(liste_hexad)
        element = algo_adaptation(liste_hexad, liste_motiv)
        print(element)
    eleve = eleves.iloc[4, :]
    liste_motiv = vecteur_influence_Motivation(eleve)
    liste_motiv = replace_name_element(liste_motiv)
    #print(liste_motiv)
    # print(liste_motiv)
    liste_hexad = vecteur_influence_Hexad(eleve)
    liste_hexad = replace_name_element(liste_hexad)
    #print(liste_hexad)
    element = algo_adaptation(liste_hexad, liste_motiv)
    print(element)"""