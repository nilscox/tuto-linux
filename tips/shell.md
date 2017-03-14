# Le shell

Le shell est une interface entre l'utilisateur et le système d'exploitation. Il
pemet d'interprêter des commandes pour effecuter des actions diverses et
variées sur l'ordinateur. On peut communiquer avec lui de façon très simple
(afficher les fichier dans un dossier par exemple), mais aussi plus compliquée
(bien qu'une utilisation simple soit très souvent amplement suffisante).

Il existe plusieurs shells, citons par exemple *bash*, *tcsh*, *ksh*, *zsh*,
*fish*, et même simplement *sh*. On va retrouver quelques différences entre ces
programmes, comme la manière de les configurer, certaines fonctionalités plus
ou moins avancées, l'utilisation de plugins... Mais pour une utilisation
simple, ils se ressemblent tous. Dans les exemples, c'est *42sh* qui est
utilisé. Pour changer de shell, il est possible d'utiliser la commande *chsh*
(et avoir installé le shell en question au préalable, bien sûr).

## Utilisation simple

Dans son utilisation la plus simple, le shell permet simplement d'éxécuter des
programmes. Ainsi, la commande `42sh$ ls` permet de lancer le *programme* *ls*
(le *42sh$* en début de ligne représente le "prompt", il peut être configuré
pour afficher par exemple le nom de l'utilisateur, le nom de la machine, la
date...) Les programmes qui sont appelés depuis le shell, et qui n'ouvrent pas
de fenêtre sont dit en *CLI* (Command Line Interface). Il est tout de même
possible de lancer un programme ouvrant une fetêtre dans le shell (par exemple
`42sh$ firefox`).

Le plus souvent, il sera nécéssaire de préciser quelques informations au
programme. Par exemple, il est possible d'utiliser le programme *convert* pour
convertir une image, et il faudra préciser le fichier original, le fichier
après la conversion, les nouvelles dimensions, le taux de compression... Même
pour afficher les fichiers dans un dossier avec *ls*, il est possible de
préciser tout plein choses. Ces informations qui seront passées au programmes
peuvent être sous différente formes :

- les arguments
- les variables d'environment
- l'entrée standard

Les arguments sont entrés juste après la commande, comme par exemple dans
`42sh$ ls -l /home`. *ls* est le programme, *-l* est un argument (permettant
d'afficher une liste détaillée), et */home* est le dossier à lister. Les
arguments ont très souvent des valeurs par défaut, ainsi l'appel à *ls* sans
arguments permet de lister simplement les fichiers se trouvant dans le dossier
actuel. La liste exhaustive des arguments qu'il est possible de donner à une
commande se trouve dans le *man* (tout ce qui est entre *[]* est optionnel).

Les argement qui commencent par un tiret permettent d'activer ou de désactiver
certaines options. Elles existent souvent sous deux formes : une forme courte
(un tiret et une lettre) et une forme longue (deux tirets et un mot) : avec
`42sd$ ls -l --file-type`, on a *ls* qui est appelé avec `-l` (liste détaillée,
sous forme courte) et `--file-type` (afficher le type des fichiers, sous forme
longue). Les argument sous forme coutes peuvent être combilnées : par exemple
`42sh$ ls -l -a -R -t -h` est équivalent à `42sh$ ls -aR -lth` et même `42sh$
ls -alhRt`.

Les variables d'environment sont dans informations qui persistent entre
plusieurs commandes. Elles sont plus utilisée pour préciser des informations
propre à l'environment (quel est l'utilisateur actuel ? quel est le dossier
dans lequel il se trouve ? ...). Il est assez rare d'avoir besoin d'y toucher,
mais il est toujours possible de toutes les afficher avec la commande `42sh$
env`. Pour changer la valeur d'une variable d'environment pour un programme
spécifique, il faut la préciser *avant* d'entrer la commande. Par exemple
`PORT=8000 node ./index.js` permet d'appeler le programme *node* avec la
variable d'environement `PORT` ayant la valeur `8000` (après, c'est le
programme qui gère cette valeur comme il veut...).

## Configuration

La configuration d'un shell se fait le plus souvent via un fichier de
configuration. Par convention, il est placé dans le *home* de l'utilisateur
(*/home/username*), son nom commence par un point suivi du nom du shell, puis
*rc*. Par exemple `/home/username/.bashrc`. La contenu de ce fichier cependant
varie selon le shell utilisé. Chaque shell explique très bien la syntaxe de sa
configuration dans son *man*, mais très honnêtrement, c'est impossible à lire
(à moins de chercher une information en particulier). Heureusement, il existe
des quantités de sites internet proposant des tutos entiers dédiés à la
configuration de son shell.

Petit mot sur le *prompt* : il est possible de le configurer via la variable
d'environment `PS1`, il y aura donc certainement une ligne du type `PS1='42sh\$
'` dans le fichier de configuration du shell. Il y a des sites dédiés
uniquement à la création de cette variable d'environement, permettant de mettre
des couleurs, d'afficher le nom de la machine, l'heure, l'utilisateur, le
dossier actuel, etc.

## L'entrée et les sorties

Un programme peut lire des informations via son entrée standard. C'est ce qui
se passe quand l'utilisateur écrit sur son clavier lorsque le programme est
lancé (le terminal transmet les lettres à l'entrée standard du programme).
Exemple : `42sh$ cat -n -` appel le programme `cat`, avec un argument `-n` et
un autre argument `-` (juste tiret) : l'utilisateur peut entrer du texte dans
le terminal, et *cat* va réafficher chaque ligne précédée du numéro de cette
ligne.

```sh
toto
     1  toto
tata
     2  tata
```

Les programmes sont également capables d'afficher des informations dans le
shell via ses sorties. La commande *ls* va simplement afficher la liste des
fichier dans sa sortie standard, et s'arrêter (pour rendre la main au shell).
La seconde sortie est la sortie d'erreur. Elle est mélangée avec la sortie
standard, mais représente bien une sortie différente. Pour une utilisation
simple du shell, on peut concidérer qu'il n'y a qu'une seule sortie.

## Redirections

Il est possible de rediriger la sortie standard (ou la sortie d'erreur) dans
des fichiers avec le symbole `>`. Par exemple, `42sh$ echo toto` va aficher
*toto* sur la sortie standard, alors que `42sh$ echo toto > file.txt` ne va
rien afficher dans la console, mais va écrire dans le fichier *file.txt*. Ce
fichier sera créé s'il n'existe pas, et écrasé sinon. De plus, il est possible
d'utiliser `>>` pour ajouter à la fin du fichier s'il existait déjà. Un petit
exemple :

```sh
42sh$ cd /tmp
42sh$ mkdir -p test
42sh$ cd test
42sh$ echo hello
hello
42sh$ echo hello > file.txt
42sh$ cat file.txt
hello
42sh$ pwd >> file.txt
42sh$ cat file.txt
hello
/tmp/test
42sh$ ls -l > file.txt
42sh$ cat file.txt
total 0
-rw-r--r--  1 user  group 4096  Jan 1 00:00 file.txt
```

Il est également possible de rediriger le contenu d'un fichier vers l'entrée
standard d'un programme avec `<`. Pour l'exemple, on va utiliser le programme
*banner*, qui permet d'afficher du texte en ASCII art.

```sh
42sh$ mkdir -p /tmp/test; cd /tmp/test
42sh$ banner -l -f 2
toto

 t           t
 t    ooo    t    ooo
ttt  o   o  ttt  o   o
 t   o   o   t   o   o
 t   o   o   t   o   o
 tt   ooo    tt   ooo

^D
42sh$ echo 'tata' > file.txt
42sh$ banner -l -f 2 < file.txt

 t           t
 t    aaa    t    aaa
ttt      a  ttt      a
 t    aaaa   t    aaaa
 t   a   a   t   a   a
 tt   aaaa   tt   aaaa

42sh$
```

Dans cet exemple, on commence par créer un dossier *test* dans */tmp* s'il
n'existe pas, et on entre dedans (en une ligne, en séparant les commandes avec
un `;`). On appel le programme *banner* qui va attendre que l'utilisateur entre
du texte sur l'entrée standard. On écrit "toto" (et un retour à la ligne), et
banner affiche *toto* en ASCII art sur la sortie standard. On peut quitter le
programme avec *Ctrl-D* (ce qui permet d'écrire un caractère spécial (non
affichable) qui représente la fin d'un fichier).

Ensuite, on écrit "tata" dans le fichier *file.txt*, et on appel *banner*, mais
cette fois ci en envoyant le contenu du fichier *file.txt* vers l'entrée
standard de *banner* avec le symbole `<`.

## Pipes

Les pipes (`|`) permettent de brancher la sortie d'une commande vers l'entrée
d'une autre commande.

```sh
42sh$ mkdir -p /tmp/test; cd /tmp/test; echo 'toto' > file.txt
42sh$ cat file.txt | banner -l -f 2
 t           t
 t    ooo    t    ooo
ttt  o   o  ttt  o   o
 t   o   o   t   o   o
 t   o   o   t   o   o
 tt   ooo    tt   ooo

42sh$
```

Pour aller plus loin, prenons un exemple un peu plus évolué :

```sh
42sh$ ls -l | awk '{ print $5 " " $9 }' | sort -n | sed 's/^.* //'
```

Ici, 4 commandes sont éxécutées (*ls*, *awk*, *sort* et *sed*), et la sortie de
chaque programme est redirigée vers l'entrée du suivant (sauf pour *sed* qui
affiche le résultat dans la console). La première commande (*ls -l*) va
afficher la liste détaillée des fichiers dans le dossier actuel. Au lieu de
l'afficher dans le terminal, ces informations sont transmises vers le programme
*awk*, ce qui permet d'extraire uniquement la taille du fichier suivi de son
nom. On redirige cette liste détaillée simplifiée vers le programme *sort*, qui
va trier la liste par ordre croissant, et enfin on envoie le tout dans *sed*,
qui va effacer la taille, ne laissant que le nom du fichier. Cette ligne permet
donc d'afficher les fichiers triés par taille (dans le monde réel, on utilisera
plutôt `42sh$ ls -S`).
