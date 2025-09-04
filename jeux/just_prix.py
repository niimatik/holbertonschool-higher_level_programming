#!/usr/bin/python3
import random

if __name__ == "__main__":
    print("Bienvenue au Juste Prix ! Essaie de trouver un nombre entre 0 et 100.")
    jouer = True
    while jouer:
        number = random.randint(0, 100)
        while True:
            difficulte = input("Choisis ta difficulté facile, moyen, difficile: ")
            if difficulte == "facile":
                chance = 10
                break
            elif difficulte == "moyen":
                chance = 7
                break
            elif difficulte == "difficile":
                chance = 5
                break
            else:
                print("On ta dit facile, moyen ou difficile connard.")
        for i in range (chance):
            saisie = input(f"{i} quel est le juste prix ?")
            if saisie.isdigit() != True:
                print("T'es con ou quoi un chiffre entre 0 et 100 on ta dit !")
                continue
            var = int(saisie)
            if var < 0 or var > 100:
                print("T'es con ou quoi un chiffre entre 0 et 100 on ta dit !")
                continue
            if var < number:
                print("c'est plus !")
            elif var > number:
                print("c'est moins !")
            elif var == number:
                print("bien jouer connard !!!!!")
                break
        else:
            print(f"sale noob t'as perdu ! C'était : {number}")
        reponse = input("t'abandonne ? : ")
        if reponse != "non":
            jouer = False
            print("t'abandonne déjà ? lacheur va !")
