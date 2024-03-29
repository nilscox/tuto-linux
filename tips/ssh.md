# Secure SHell

Secure Shell (`ssh`) est un outil aussi simple que puissant. Cela permet
essentiellement de se conecter à un shell à distance (sur une autre machine, un
serveur, un router, ...) de manière *absoluement sécurisée* (d'où le *secure*).
Son utilisation de base est très simple : `ssh user@hostname`. Mais avant cela,
il est nécéssaire de passer par une petite étape de configuration.

## Clés SSH

Le méchanisme apportant toute la sécurité à ssh est l'utilisation de clés
*asymétriques*. Le principe est simple et intéressant à savoir (c'est aussi ce
principe qui donne sa robustesse au bitcoin et l'anonymat à Tor par exemple).

Pour chiffrer (et non pas "crypter", ne mot n'existe même pas dans la langue
française) des données, il existe deux méthodes : le chiffrage *symétrique*
et... bah *asymétrique*. Dans le premier cas, il existe une clé (un mot de
passe plus ou moins compliqué) permettant de chiffrer et de déchiffrer des
données. C'est un peu comme un coffre fort : n'importe qui ayant la clé peut
accéder au coffre.

Dans le cas du chiffrage asymétrique, il existe deux clées : une permettant
uniquement le chiffrement (la clé publique) et la seconde permettant uniquement
le déchiffrement (la clé privée). La clé publique peut être distribuée
librement, de manière à ce que n'importe qui chiffrer un message que moi seul
pourrai déchiffrer, car ma clé de déchiffrement est privée. Ca ne ressemble pas
vraiment un coffre fort dans ce cas, mais plus à une boîte aux lettres : la clé
publique est mon adresse (tout le monde peut m'envoyer du courrier...), et ma
clé privée est la clé de la boîte aux lettres (... mais moi seul peut le lire).
Donner sa clé privée revient à donner accès à son bitcoin, ou pire : donner
accès à tous ses serveurs !

Bref, voilà pour la petite histoire. Pour créer une nouvelle combinaison de clé
(privée + publique), il existe la commande `ssh-keygen`. Il existe plusieurs
types de clés, et RSA était très utilisé pendant des années. Un autre type qui
est très performant est ed25519 (clé plus petite et plus rapide). Plus d'infos
dans le man, bien entendu.

Note : il est aussi possible de protéger sa clé par une "passephrase" (un mot
de passe), au cas où elle serait récupérée par un vilain hacker (ça m'est
arrivé sur mon serveur...). `ssh-keygen` demande d'entrer (ou pas) une
passephrase, il est bien entendu important d'en choisir une (et de la retenir :
plus de passephrase = plus de bitcoin).

## Lien avec git

Les échanges entre deux dépôts [git](git.md) (essentiellement `push` et `pull`)
se font via HTTP ou SSH. Par défaut, c'est en HTTP (il faut préciser son
adresse mail + mot de passe à chaque fois). Il est possible d'ajouter sa clé
privée sur son profil github pour que les échanges se fassent via SSH.

## Ajouter sa clé sur une machine

Si on a un accès SSH avec user + password sur une machine, il est possible d'y
ajouter sa clé publique, et pouvoir utiliser sa clé pour se logger. Pour cela,
il existe `ssh-copy-id` (cela va simplement ajouter la clé publique de la
machine locale dans le fichier `~/.ssh/authorized_keys` sur la machine
distante).

## scp

`scp` est la combinaison de `ssh` et `cp`. Cela permet simplement de copier un
fichier (ou dossier) d'une machine vers une autre.
