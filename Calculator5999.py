print ('Bonjour Humain.')
entree1 = raw_input('Donnez moi un chiffre ')
entree2 = raw_input('Donnez moi un second chiffre ')
operateur = raw_input('Donnez moi un operateur ')

entree1 = int(entree1)
entree2 = int(entree2)

if operateur == '+':
    resultat = entree1 + entree2
    print ('Votre resultat est ' + str(resultat))
elif operateur == '-':
    resultat = entree1 - entree2
    print ('Votre resultat est ' + str(resultat))
elif operateur == '*':
    resultat = entree1 * entree2
    print ('Votre resultat est ' + str(resultat))
elif operateur == '/':
    resultat = entree1 / entree2
    print ('Votre resultat est ' + str(resultat))
else:
    print ('404 OPERATEUR NOT FOUND')
