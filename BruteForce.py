alphabet = 'abcdefghijklmnopqrstuvwxyz';
motDePasse= 'cis'
motdePasseConfirmation=""
lettre1=''
lettre2=''
lettre3=''
compteur=0

for i in range(26):

    lettre1=alphabet[i]

    for j in range(26):
        lettre2=alphabet[j]
        for k in range(26):
            lettre3=alphabet[k]

            motdePasseConfirmation =lettre1+lettre2+lettre3


            if motDePasse== motdePasseConfirmation:
                print("wouhou !!!!")

            print (motDePasse)
            print (motdePasseConfirmation)


