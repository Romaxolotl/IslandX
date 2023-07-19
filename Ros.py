
import os
import threading
import random
import time
from colorama import init, Fore, Back, Style    
import msvcrt  # module specifique e Windows pour la gestion des touches (remplacez-le par getch() sur d'autres systemes)
import sys
import requests
import base64

init()  # Initialisez Colorama pour activer les sequences d'echappement ANSI sur Windows.
################################################# fonction mere ######################
def connexion():
    identifiant = input(Fore.RED + "quelle est votre identifiant >> \n")
    mdp = print("quelle est votre mot de passe >>")
    mdp = get_password()
    if identifiant == "Romaxolotl" and mdp == "1006":
        connecte("admin", identifiant)
    elif identifiant == "Luke" and mdp == "2009":
        connecte("user", identifiant)
    else :
        print("identifiant ou/et mot de passe invalide")
        connexion()

def connecte(arg1, arg2):
    identifiant = arg2
    tipe = arg1
    print(Fore.BLUE + "bienvenue " + tipe + " " + identifiant )
    for i in range(21):  # 11 etapes, y compris l'etape finale avec 10 #
        print('#' * i, end='\r')
        time.sleep(0.25)  # Ajoutez un delai pour l'effet d'animation (0.5 seconde dans cet exemple)
    print("####################")
    print("Chargement termine!")
    if tipe == "admin":
        suite_admin()
    elif tipe == "user":
        suite_user()

def get_password():
    mdp = ""
    while True:
        # La fonction msvcrt.getch() r�cup�re un caract�re sans l'afficher � l'�cran
        char = msvcrt.getch().decode("utf-8")
        
        # Si l'utilisateur appuie sur la touche Entr�e (fin de la saisie du mot de passe)
        if char == '\r':
            print()  # Aller � la ligne pour la clart�
            break
        # Si l'utilisateur appuie sur la touche de retour arri�re
        elif char == '\x08':
            # Supprimer le dernier caract�re du mot de passe et effacer l'ast�risque correspondant
            if len(mdp) > 0:
                mdp = mdp[:-1]
                print('\b \b', end='', flush=True)  # Effacer le dernier caract�re affich�
        else:
            # Ajouter le caract�re � la cha�ne du mot de passe et afficher un ast�risque
            mdp += char
            print('*', end='', flush=True)
    
    return mdp

def verif_system():
    verificator("Config.RomOS")
    verificator("Save.RomOS")
    Averificator("Scripts")
    return True

def colora():
    colora = input("entre une valeur entre : 0=noir , 7=gris, 1=bleu >> \n")
    colora = colora + ", F"
    set_console_color(colora)

def delete_file(nom_fichier):
    try:
        os.remove(nom_fichier)
        print(f"Le fichier '{nom_fichier}' a ete supprime avec succes.")
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas ete trouve.")
    except PermissionError:
        print(f"Vous n'avez pas la permission de supprimer le fichier '{nom_fichier}'.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la suppression du fichier '{nom_fichier}': {e}")

def menu(arg1):
    print(Fore.GREEN + "Menu")
    print("Commandes disponibles:")
    print("help pour le menu help")
    print("Save pour sauvegarder")
    print("clear pour nettoyer la console")
    print("reboot pour sauvegarder et redemarrer")
    print("et beaucoup d'autres ...")
    print(Fore.RESET)
    if arg1 == "admin":
        print("En tant qu'administrateur, utilisez la commande ROS avant une commande d'admin")
        CMDa(arg1)
    else: 
        print("En tant qu'utilisateur, vous n'avez pas acces aux fonctionnalites des administrateurs")
        CMDa(arg1)

    
def CMDa(arg1):
    CMDe = input(Fore.RESET + ">> ")
    if CMDe == "help":
        menu()
        CMDa(arg1)
    elif CMDe == "clear":
        clear()
        CMDa(arg1)
    elif CMDe.startswith("ROS") and "refill" in CMDe:
        if arg1 == "admin":
            delall()
            verif_system()
            suite_admin()
        else:
            print(Fore.RED + "vous n'etes pas admin")
            CMDa(arg1)
    elif CMDe == "reboot":
        clear()
        Bios()
    elif CMDe.startswith("launch"):
        CMDe_2 = CMDe.replace("launch ", "")
        CMDu = CMDe_2 + ".py"
        print(Fore.BLUE)
        launchh(CMDu)
        print(Fore.RESET)
        CMDa(arg1)
    elif CMDe.startswith("islandx download "):
        CMDe_1 = CMDe.replace("islandx download ", "")
        islandX("Romaxolotl", "IslandX", CMDe_1)
        CMDa(arg1)
    elif CMDe.startswith("ls"):
        CMDe_1 = CMDe.replace("ls ", "")
        afficher_contenu_dossier(CMDe_1)
        print(Fore.RESET)
        CMDa(arg1)
    else:
        print(Fore.RED + "Commande invalide")
        CMDa(arg1)

def afficher_contenu_dossier(arg1="."):
    # V�rifier si le dossier existe
    print(Fore.GREEN)
    if not os.path.exists(arg1):
        print(f"Le dossier '{arg1}' n'existe pas.")
        return

    # R�cup�rer la liste des fichiers et dossiers dans le dossier
    contenu_dossier = os.listdir(arg1)

    # V�rifier si le dossier est vide
    if not contenu_dossier:
        print(f"Le dossier '{arg1}' est vide.")
        return

    # Afficher le contenu du dossier
    print(f"Contenu du dossier '{arg1}':")
    for element in contenu_dossier:
        print(element)

def launchh(arg2, arg1="Scripts"):
    chemin_fichier = os.path.join(arg1, arg2)
    if os.path.exists(chemin_fichier):
        print(f"Execution du fichier '{chemin_fichier}'...")
        os.system(f"python {chemin_fichier}")
    else:
        print(f"Le fichier '{chemin_fichier}' n'existe pas dans le dossier '{arg1}'.")

def islandX(repo_owner, repo_name, script_name):
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{script_name}.py'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        script_content = response.json()['content']
        script_content = base64.b64decode(script_content).decode('utf-8')
        
        scripts_folder = "scripts"
        if not os.path.exists(scripts_folder):
            os.makedirs(scripts_folder)
        
        script_path = os.path.join(scripts_folder, f"{script_name}.py")
        with open(script_path, 'w') as script_file:
            script_file.write(script_content)
        
        print(f"Le script '{script_name}' a ete telecharge depuis GitHub et sauvegarde dans le dossier 'scripts'.")
    else:
        print(f"Erreur lors du telechargement du script '{script_name}' depuis GitHub.")

###################################################### MISE A JOUR  ################################

def get_current_version():
    return "01/01/2000"  # Remplacez ceci par la version actuelle de votre script

def get_latest_version(repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('tag_name')
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la recuperation de la derniere version : {e}")
        return None

def download_and_replace_script(download_url):
    response = requests.get(download_url)
    response.raise_for_status()

    with open('mon_script_maj.py', 'wb') as f:
        f.write(response.content)

    # Ajoutez ici le code pour sauvegarder l'ancien script (facultatif)
    # Puis, remplacez l'ancien script par la mise � jour.
    os.replace('mon_script_maj.py', sys.argv[0])

def maj(arg1):
    # Mettez � jour ces valeurs avec les informations de votre r�f�rentiel GitHub
    repo_owner = "Romaxolotl"
    repo_name = "RomOS"

    current_version = get_current_version()
    latest_version = get_latest_version(repo_owner, repo_name)

    if latest_version and latest_version != current_version:
        print(f'Une nouvelle version ({latest_version}) est disponible !')
        print(f'Vous utilisez actuellement la version {current_version}.')
        download_url = f'https://github.com/{repo_owner}/{repo_name}/releases/latest/download/mon_script_maj.py'
        download_and_replace_script(download_url)
        print("Le script a ete mis e jour avec succes.")
        return latest_version
    else:
        print(f'Vous utilisez deja la derniere version ({current_version}).')
        return arg1


###################################################### Protocole ###################################
def protocole3():
    creator("Config.RomOS")
    editor("Config.RomOS", "Color::F")
    editor("Config.RomOS", "ColorBG::0")

def protocole2():
    creator("Save.RomOS")
###################################################### READER ######################################
def read(arg1, arg2=None):
    chemin_fichier = arg2 if arg2 is not None else "Config.RomOS"

    if isinstance(arg1, str) and arg1.startswith("Del"):
        return supprimer(arg1[4:].strip())
    elif isinstance(arg1, str):
        return lire_variable(arg1, chemin_fichier)
    elif isinstance(arg1, int):
        return lire_ligne(arg1, chemin_fichier)
    else:
        raise ValueError("Les arguments fournis ne sont pas valides.")

def lire_ligne(numero_ligne, chemin_fichier):
    with open(chemin_fichier, "r") as fichier:
        lignes = fichier.readlines()
        if 1 <= numero_ligne <= len(lignes):
            valeur = lignes[numero_ligne - 1].strip()
            return valeur
    return None

def lire_variable(nom_variable, chemin_fichier):
    with open(chemin_fichier, "r") as fichier:
        for ligne in fichier:
            if ligne.startswith(nom_variable + "::"):
                valeur = ligne.split("::")[1].strip()
                return valeur
    return None

def supprimer(arg):
    if arg.isdigit():
        return supprimer_ligne(int(arg))
    else:
        return supprimer_variable(arg)

def supprimer_ligne(numero_ligne):
    with open("config.RomOS", "r") as fichier:
        lignes = fichier.readlines()

    if 1 <= numero_ligne <= len(lignes):
        lignes.pop(numero_ligne - 1)

        with open("config.RomOS", "w") as fichier:
            fichier.writelines(lignes)
        return True
    return False

def supprimer_variable(nom_variable):
    with open("config.RomOS", "r") as fichier:
        lignes = fichier.readlines()

    with open("config.RomOS", "w") as fichier:
        supprime = False
        for ligne in lignes:
            if not ligne.startswith(nom_variable + "::"):
                fichier.write(ligne)
            else:
                supprime = True
        return supprime
        
########################################################## CONSOLE #####################
def pear(loading_text, done_text, duration):
    print(loading_text, end='', flush=True)
    time.sleep(duration)
    print('\r' + ' ' * len(loading_text) + '\r' + done_text, end='', flush=True)

def clear_line():
    sys.stdout.write("\033[K")
    sys.stdout.flush()

def set_console_color(text_color, background_color):
    if os.name == 'nt':  # Pour Windows
        os.system(f"color {text_color}{background_color}")
    else:  # Pour les syst�mes UNIX (Linux, macOS, etc.)
        print(f"\033[0;{text_color};{background_color}m", end='')
# Les attributs de couleurs sont sp�cifi�s par DEUX chiffres hexad�cimaux -- le premier correspond � l�arri�re-plan, le second au premier plan.
#   0 = Noir        8 = Gris
#   1 = Bleu        9 = Bleu clair
#    2 = Vert        A = Vert clair
#   3 = Bleu-gris        B = Cyan
#    4 = Rouge      C = Rouge clair
#    5 = Violet     D = Violet clair
#    6 = Jaune        E = Jaune clair
#    7 = Blanc       F = Blanc brillant

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
########################################### BIOS #############################################
def Bios():
    V = "1"
    #V = maj("0.0.2")
    system = "ROSNoG_RomOSXIsland"  # RomaOSNoGuiV.0.1 ##############################################################################################################################
    print(Fore.WHITE + "boot on ROS.NG")
    if V == "1":
        print("vous etes en version NoError ")
    time.sleep(1)
    print(system)
    print("version " + V)
    print("Boot.", end='\r')
    time.sleep(1)
    print("Boot..", end='\r')
    time.sleep(1)
    print("Boot...", end='\r')
    time.sleep(1)
    clear_line()
    print("Boot.", end='\r')
    time.sleep(1)
    print("Boot..", end='\r')
    time.sleep(1)
    print("Boot...", end='\r')
    time.sleep(1)
    connexion()
################################################ CEVAD ##########################################
def creator(arg1):
    chemin = arg1
    # Cr�er un fichier et l'ouvrir en mode �criture
    fichier = open(chemin, 'w')
    fichier.close()  # Fermer le fichier apr�s utilisation

def editor(arg1, arg2):
    chemin = arg1
    # Ouvrir le fichier en mode ajout et �crire du contenu � la fin
    with open(chemin, 'a') as fichier:
        fichier.write(arg2 + "\n")

def verificator(nom_fichier):
    # R�cup�rer le chemin absolu du r�pertoire courant du script
    repertoire_courant = os.path.dirname(os.path.abspath(__file__))
    
    # V�rifier si le fichier existe dans le r�pertoire courant
    chemin_fichier = os.path.join(repertoire_courant, nom_fichier)
    if os.path.exists(chemin_fichier):
        print(f"Le fichier '{nom_fichier}' existe dans le repertoire courant.")
    else:
        print(f"Le fichier '{nom_fichier}' n'existe pas dans le repertoire courant.")
        if nom_fichier == "Config.RomOS":
            print("LANCEMENT DU PROTOCOLE 3")
            protocole3()
            verif_system()
        elif nom_fichier == "Save.RomOS":
            print("LANCEMENT DU PROTOCOLE 2")
            protocole2()
            verif_system()

def Averificator(nom_dossier):
    if os.path.exists(nom_dossier):
        print("le dossier " + nom_dossier + " existe")
    else:
        os.makedirs(nom_dossier)
        print(f"Le dossier '{nom_dossier}' a ete cree.")
    
def deletor(file_path):
    try:
        os.remove(file_path)
        print(f"Le fichier '{file_path}' a ete supprime avec succes.")
    except OSError as e:
        print(f"Erreur lors de la suppression du fichier '{file_path}': {e}")
################################################## Object ##################################
def delall():
    delete_file("Config.RomOS")
    delete_file("Save.RomOS")

def suite_user():
    verif_system()
    menu("user")

def suite_admin():
    commande1 = input(Fore.WHITE + "commande de demarage (tapez entrer pour continuer normalement)>> \n")
    if commande1 == "":
        verif_system()
        rr = read("Color")
        rr2 = read("ColorBG")
        set_console_color(rr2, rr)
        print("couleur appliquer avec succees")
        menu("admin")
    if commande1 == "NP":
        menu("admin")
    elif commande1 == "delall":
        delall()
        suite_admin()
    elif commande1 == "refill":
        delall()
        verif_system()
        suite_admin()
    elif commande1 == "color":
        colora()
        suite_admin()
    else:
        print(Fore.RED + "commande invalide")
        suite_admin()

V = "1"
Bios()
