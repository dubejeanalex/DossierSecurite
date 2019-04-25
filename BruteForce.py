import time
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
#motDePasse= 'cisco'
motdePasseConfirmation=""
lettre1=''
lettre2=''
lettre3=''
lettre4=''
lettre5=''

#print("Choisissez un mot de passe de 5 lettres :")
motDePasse = sys.argv[2]


def BruteForceFaible():
    # Début du décompte du temps
    start_time = time.time()
    for i in range(26):
        lettre1=alphabet[i]

        for j in range(26):
            lettre2=alphabet[j]
            for k in range(26):
                lettre3=alphabet[k]
                for l in range(26):
                    lettre4=alphabet[l]
                    for m in range(26):
                        lettre5=alphabet[m]

                        motdePasseConfirmation=lettre1+lettre2+lettre3+lettre4+lettre5
                        #print(motdePasseConfirmation)

                        if motDePasse==motdePasseConfirmation:
                            print("Le mot de passe que vous avez entré est =>",motdePasseConfirmation)
                            # Affichage du temps d'exécution
                            print("Temps d'execution =>", round((time.time() - start_time), 2), "secondes")
                            quit()

def BruteForceMoyen():
    # Début du décompte du temps
    start_time = time.time()
    for i in range(52):
        lettre1=alphabet[i]

        for j in range(52):
            lettre2=alphabet[j]
            for k in range(52):
                lettre3=alphabet[k]
                for l in range(52):
                    lettre4=alphabet[l]
                    for m in range(52):
                        lettre5=alphabet[m]

                        motdePasseConfirmation=lettre1+lettre2+lettre3+lettre4+lettre5
                        #print(motdePasseConfirmation)

                        if motDePasse==motdePasseConfirmation:
                            print("Le mot de passe que vous avez entré est =>",motdePasseConfirmation)
                            # Affichage du temps d'exécution
                            print("Temps d'execution =>", round((time.time() - start_time), 2), "secondes")
                            quit()

def BruteForceFort():
    # Début du décompte du temps
    start_time = time.time()
    for i in range(62):
        lettre1=alphabet[i]

        for j in range(62):
            lettre2=alphabet[j]
            for k in range(62):
                lettre3=alphabet[k]
                for l in range(62):
                    lettre4=alphabet[l]
                    for m in range(62):
                        lettre5=alphabet[m]

                        #motdePasseConfirmation=lettre1+lettre2+lettre3+lettre4+lettre5
                        print(motdePasseConfirmation)

                        if motDePasse==motdePasseConfirmation:
                            print("Le mot de passe que vous avez entré est =>",motdePasseConfirmation)
                            # Affichage du temps d'exécution
                            print("Temps d'execution =>", round((time.time() - start_time), 2), "secondes")
                            quit()

if(sys.argv[1]== "faible"):
    BruteForceFaible()
elif (sys.argv[1] == "moyen"):
    BruteForceMoyen()
elif (sys.argv[1] == "fort"):
    BruteForceFort()