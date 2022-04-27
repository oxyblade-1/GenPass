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
* longeur (par défaut 10) -> max 100 caractères

![setting](https://github.com/oxyblade-1/GenPass/blob/main/maquette/setting.png)

* sauvegarde des mots de passes

> Connaissance requise au projet

* Utilisation de Tkinter
* Création d'onglets -> nouvelle fenêtre 
* gestion des images
* Utilisation des modules "random" & "string"

> Problème ?

L'un des gros problème actuelle est lors de la sauvegarde des données le mot de passe n'est pas crypté ce qui fait que les données sauvegarder sur l'ordinateur ne sont pas sécurisé contre des pirates et autres (recherche de solution en cour).
