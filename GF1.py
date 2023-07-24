import os

def afficher_menu(repertoire_courant):
    print("")

def afficher_contenu_repertoire(repertoire_courant):
    contenu = os.listdir(repertoire_courant)
    print(f"Contenu du répertoire '{repertoire_courant}':")
    for element in contenu:
        print(element)

def ouvrir_fichier_enfant(repertoire_courant, nom_fichier):
    chemin_fichier = os.path.join(repertoire_courant, nom_fichier)
    if os.path.isfile(chemin_fichier):
        print(f"Contenu du fichier '{chemin_fichier}':")
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read()
            print(contenu)
    else:
        print(f"Le fichier '{chemin_fichier}' n'existe pas.")

def retourner_repertoire_parent(repertoire_courant):
    nouveau_repertoire = os.path.dirname(repertoire_courant)
    if nouveau_repertoire == repertoire_courant:
        print("Vous êtes déjà à la racine du système.")
    else:
        return nouveau_repertoire

def naviguer_vers_repertoire_enfant(repertoire_courant, nom_repertoire):
    chemin_repertoire = os.path.join(repertoire_courant, nom_repertoire)
    if os.path.isdir(chemin_repertoire):
        return chemin_repertoire
    else:
        print(f"Le répertoire '{chemin_repertoire}' n'existe pas.")
        return repertoire_courant
    
def charger_repertoire_different(repertoire_courant, chemin_repertoire):
    chemin_nouveau_repertoire = os.path.join(repertoire_courant, chemin_repertoire)
    if os.path.exists(chemin_nouveau_repertoire):
        return chemin_nouveau_repertoire
    else:
        print(f"Le répertoire '{chemin_nouveau_repertoire}' n'existe pas.")
        return repertoire_courant

def afficher_lettres_de_lecteur():
    if os.name == 'nt':  # Vérifie si le système d'exploitation est Windows
        import string
        lettres_disponibles = [f"{d}:" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
        if lettres_disponibles:
            print("Lettres de disque utilisées :", " ".join(lettres_disponibles))
        else:
            print("Aucune lettre de disque utilisée sur ce PC.")
    else:
        print("Affichage des lettres de lecteur disponible uniquement sur Windows.")

def afficher_contenu_fichier(chemin_fichier):
    try:
        if os.path.isfile(chemin_fichier):
            taille_max_fichier_afficher = 10000
            taille_fichier = os.path.getsize(chemin_fichier)

            if taille_fichier > taille_max_fichier_afficher:
                confirmation = input(f"Le fichier '{chemin_fichier}' est assez volumineux ({taille_fichier} octets). Êtes-vous sûr de vouloir l'afficher ? (o/n) : ")
                if confirmation.lower() != 'o':
                    return

            with open(chemin_fichier, 'r') as fichier:
                contenu = fichier.read()
                print(f"Contenu du fichier '{chemin_fichier}':\n{contenu}")
        else:
            print(f"Le fichier '{chemin_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'affichage du contenu : {e}")

def ajouter_contenu_au_fichier(chemin_fichier, contenu):
    try:
        if not os.path.exists(chemin_fichier):
            print(f"Le fichier '{chemin_fichier}' n'existe pas.")
        else:
            with open(chemin_fichier, 'a') as fichier:
                contenu_final = contenu.replace("\\n", "\n")
                fichier.write(contenu_final)
            print(f"Contenu ajouté à la fin du fichier '{chemin_fichier}'.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'ajout du contenu : {e}")

def supprimer_fichier_ou_repertoire(repertoire_courant, chemin):
    chemin_complet = os.path.join(repertoire_courant, chemin)
    try:
        if os.path.isfile(chemin_complet):
            os.remove(chemin_complet)
            print(f"Le fichier '{chemin_complet}' a été supprimé.")
        elif os.path.isdir(chemin_complet):
            contenu = os.listdir(chemin_complet)
            for element in contenu:
                element_chemin = os.path.join(chemin_complet, element)
                if os.path.isdir(element_chemin):
                    supprimer_fichier_ou_repertoire(repertoire_courant, element_chemin)
                else:
                    os.remove(element_chemin)
            os.rmdir(chemin_complet)
            print(f"Le répertoire '{chemin_complet}' et son contenu ont été supprimés.")
        else:
            print(f"Le chemin '{chemin_complet}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la suppression : {e}")

def creer_fichier_txt(chemin_fichier):
    try:
        chemin_absolu = os.path.join(repertoire_courant, chemin_fichier)
        with open(chemin_absolu, 'x') as fichier:
            print(f"Le fichier '{chemin_fichier}' a été créé avec succès.")
    except FileExistsError:
        print(f"Le fichier '{chemin_fichier}' existe déjà.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du fichier : {e}")

def afficher_help():
    print(f"\nRépertoire courant: {repertoire_courant}")
    print("Menu:")
    print("ls : Afficher le contenu du répertoire")
    print("o <nom_fichier> : Ouvrir un fichier enfant du répertoire")
    print("r : Revenir au répertoire parent")
    print("RR : Pour changer la lettre de repertoire ")
    print("RRls : pour afficher toute les lettre utiliser sur votre PC")
    print("d : suprimer ")
    print("e : pour creer un fichier txt")
    print("w : pour ecrire a la fin d'un fichier")
    print("q : Quitter")

if __name__ == "__main__":
    repertoire_courant = os.getcwd()
    afficher_help()
    while True:
        afficher_menu(repertoire_courant)
        commande = input(">> ").split()
        if commande[0] == "ls":
            afficher_contenu_repertoire(repertoire_courant)
        elif commande[0] == "help":
            afficher_help()
        elif commande[0] == "o" and len(commande) > 1:
            nom_repertoire = commande[1]
            repertoire_courant = naviguer_vers_repertoire_enfant(repertoire_courant, nom_repertoire)
            afficher_contenu_repertoire(repertoire_courant)
        elif commande[0] == "r":
            nouveau_repertoire = retourner_repertoire_parent(repertoire_courant)
            if nouveau_repertoire:
                repertoire_courant = nouveau_repertoire
            afficher_contenu_repertoire(repertoire_courant)
        elif commande[0] == "q":
            print("Au revoir !")
            break
        elif commande[0] == "d" and len(commande) > 1:
            chemin_a_supprimer = commande[1]
            supprimer_fichier_ou_repertoire(repertoire_courant, chemin_a_supprimer)
        elif commande[0] == "RR" and len(commande) > 1:
            chemin_repertoire = commande[1]
            repertoire_courant = charger_repertoire_different(repertoire_courant, chemin_repertoire)
            afficher_contenu_repertoire(repertoire_courant)
        elif commande[0] == "RRls":
            afficher_lettres_de_lecteur()
        elif commande[0] == "e" and len(commande) > 1:
            nom_fichier = commande[1]
            if nom_fichier.endswith(".txt"):
                creer_fichier_txt(nom_fichier)
            else:
                print("Le nom du fichier doit se terminer par l'extension '.txt'.")
        elif commande[0] == "w" and len(commande) > 2:
            nom_fichier = commande[1]
            contenu = " ".join(commande[2:])
            if nom_fichier.endswith(".txt"):
                ajouter_contenu_au_fichier(nom_fichier, contenu)
            else:
                print("Le nom du fichier doit se terminer par l'extension '.txt'.")
        elif commande[0] == "l" and len(commande) > 1:
            nom_fichier = commande[1]
            if nom_fichier.endswith(".txt"):
                afficher_contenu_fichier(nom_fichier)
            else:
                print("Le nom du fichier doit se terminer par l'extension '.txt'.")
        else:
            print("Commande invalide. Veuillez entrer une commande valide.")
