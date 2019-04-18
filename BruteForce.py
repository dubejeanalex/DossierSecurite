alphabet = 'abcdefghijklmnopqrstuvwxyz';
motDePasse= 'aaaaa'
motdePasseConfirmation=""
lettre1=''
lettre2=''
lettre3=''
lettre4=''
lettre5=''
compteur=0

while motdePasseConfirmation != motDePasse:
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



                        motdePasseConfirmation =lettre1+lettre2+lettre3+lettre4+lettre5
                        print(motdePasseConfirmation)

                        if motDePasse== motdePasseConfirmation:
                             print("wouhou !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11111")
                             break


    print (motdePasseConfirmation)


