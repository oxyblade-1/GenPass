# GenPass (le générateur) [Projet en cour]

> Utilitée ?

Permet de créer des mots de passes Sécurisés 
en Locale, avec une interface accessible au utilisateurs

> Comment sa ce présente ?

Lorsque vous exécuter le logicielle cela
vous ouvre une fenêtre avec en premier l'interface principale.

![main](https://github.com/oxyblade-1/GenPass/blob/main/maquette/main.png)

Puis un boutton avec un engreinage "setting" qui vous permet de parramétré
le type de mot de passe que vous voulez:
* caractère
* chiffres
* ponctuation
* longeur (par défaut 10) -> max 100 caractère

![setting](https://github.com/oxyblade-1/GenPass/blob/main/maquette/setting.png)

* sauvegarde des mots de passes

> Connaissance requise au projet

* Utilisationde Tkinter
* Création d'onglets -> nouvelle fenêtre 
* gestion des images
* Utilisation des modules "random" & "string"

> Problème ?

L'un des gros problème actuelle est lors de la sauvegarde des données le mot de passe n'est pas cryptée
(je n'est pas voulu m'éloigné dans le projet car ceci est de base qu'un entrainement).