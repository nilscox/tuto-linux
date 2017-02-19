# Git

Git est un outil très puissant et super util (utilisé principalement par les
developpeurs). C'est ce qu'on appelle un "gestionnaire de versions", et ça
permet (entre autre) de partager du code, et de pouvoir bosser à plusieurs
dessus. Pour le tuto, j'utiliserai `git` pour détailler les exos, et pour qu'on
puisse partager des fichiers. On ne va voir ici que les commandes git de
bases, qui nous seront utiles pour suivre le tuto.

Le principe est simple : git permet de creer des *dépôts* (repository ou repo en
anglais). Un dépôt est un dossier, qui contient tout type de fichier (mais généralement du code). *tuto-linux*
est donc un dépôt, et est hébergé sur github.com. Le dossier `tuto-linux`, quelque part sur les serveurs de github, est celui de référence (cela permet de centraliser les
fichiers du projet). Chaque utilisateur à de son côté son propre dépôt (dit
*local*, sur sa machine).

Git va permettre de suivre l'historique des modifications du code, en faisant
ces modifications en local, et en mettant à jour le dépôt partagé pour que tout
le monde puisse prendre en compte les modifications apportées par les nouvelles versions. Un ensemble de "modifications" créent une nouvelle version et ça à même un nom : un
*commit*. Quand on code, on va par exemple fixer
un bug, et tout de suite faire un commit qui va prendre en compte la nouvelle version du code
corrigé. En général, on donne un message de commit pour exprimer ce à quoi il sert.

Il y a donc plusieurs étapes pour apporter une modification sur un dépôt. Dans
l'ordre :

- `git add file.txt` : prendre en compte les changements apportés sur le fichier `file.txt`
- `git commit -m "message"` : éffectue un commit (les modifications de tous les fichiers qui ont été `git add` sont prises en comptes, les autres non)
- `git push` : met à jour le dépôt global en envoyant tous les nouveau commits (on peut par exemple faire 20 commits et pusher qu'en fin de journée)

J'ajoute quelques commandes plutôt utiles (les détails sont dans le *man*) :

- `git status` : affiche l'état du dépôt (les fichiers en vert sont ceux qui vont être pris en compte en faisant `git commit`)
- `git pull` : c'est l'inverse de git push (ça récupère les modifications du dépôt global pour mettre à jour le dépôt local)
- `git clone` : pour créer (clôner) un dépôt local à partir d'un dépôt global existant
