# Documentation TKinter (non officielle)

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

Le label permet d'afficher du texte sur la fenêtre
il est d'ailleur possible de le configurer avec différent parramètre.
(Tout les parramètre dans le Label ne sont pas obligatoire, vous pouvez donc en ajouter ou en retirer à l'exeption ici de `root`)

```py
text = Label(root, text="text", font=("FontName", 15), fg="hexacode", bg="hexacode")
#bg: background -> couleur de fond du texte
#fg: fontground -> couleur d'écriture de la police
```
/!\ Il est possible de mettre le texte sous format image nous en parlerons juste après !

> Boutton

> Frame



