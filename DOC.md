#Documentation TKinter

Tkinter est un module python très utile pour la programmation d'interface graphique.
Sa syntexte reste globalement explicite et permet aux utilisateur d'executer leur code
interprété tout un utilisant du graphique

/!\ Utiliser `ctrl` + `F` pour chercher un élément spécifique !

> Création d'une fenêtre

Dans mon cas j'utilise la variable `root` (racine) qui pour moi
symbolise bien le concept. Si vous voulez la changer veuillez vérifier les modification sur tout votre code !

```py
root = Tk() # créer une fenêtre
root.mainloop() # l'afficher
```

* titre d'une fenêtre
```py
root.title('Name')
```

* Dimensionner une fenêtre
```py
root.geometry("500x500")# fenêtre 500pixels x 500pixels
```

* Garder la forme de la fenêtre
```py
root.resizable(width=False, height=False) 
# désactiver le dimensionnement
# width (largeur)
# height (hauteur)
```

* Ajouter un icon
Pour pouvoir mettre une image en tant que logo je vous conseille
d'utilise ce [convertisseur](https://convertio.co/fr/) afin de pouvoir mettre votre image en format `ico`

```py
root.iconbitmap('FilePath/name.ico')
```

* Fond écrand fenêtre
```py
root.config(background='hexacode')
#configurer le font avec un code hexadécimale
#ou un code coleur red, green, blue, ...
```


> Label (Texte)



