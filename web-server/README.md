# Web server

Un *serveur web* est programme, qui tourne en continue sur une machine, et qui
attend des connexions internet (sur le port 80 par défaut).

Lorsqu'un utilisateur se connecte à un site web, son navigateur va établir une
connexion avec le serveur (qui était en attente). Une fois la connexion
établie, le navigateur va pouvoir dialoguer avec le serveur pour afficher le
site correctement.

Le but de l'exo est d'*installer* un serveur web sur une machine sous linux, de
*configurer* ce serveur, et de *déployer* deux sites : un site statique et un
site dynamique.  Un site statique est composé uniquement de fichiers HTML /
CSS, et le serveur ne fait que transférer le contenu des fichiers bruts au
navigateur. Un site dynamique à l'inverse sera capable de produire le code HTML
des pages web dynamiquement (avec du code).

## Nginx

*Nginx* est un serveur web. Il est utilisé le plus souvent en tant que *démon*
(daemon en anglais), et est appelé un *service* sous linux.  Un démon est un
programme qui tourne en tâche de fond. Il peut être contrôlé avec la commande
`service` sous debian, ce qui permet de le démarrer, l'arrêter, le
redémarrer...

Comme je l'ai déjà dit, le but de l'exo est d'installer et de configurer nginx
pour donner accès à deux sites. [La documentation](http://nginx.org/en/docs/)
est assez bien faite (et il y a toujours [stackov'](http://stackoverflow.com/)
en cas de pépin...).

C'est parti, il est temps d'installer et de lancer nginx. Nous reviendrons sur
sa config plus tard... Si le serveur est bien lancé, un message doit s'afficher
sur [http://localhost/](http://localhost/).

## Raspout

Nous avons maintenant un serveur qui tourne, mais pas encore de site.
Commençons par écrire le site *raspout*. Le code HTML / CSS (/ JS ?) doit être
présent dans le dossier `tuto-linux/web-server/raspout`, et le fichier d'entrée
doit s'appeler `index.html`. Aucune autre indication n'est donnée, le contenu
de site est totalement lible (une page HTML simple et un peu de CSS feront tout
à fait l'affaire...).

Une fois que le site est terminé, il faut le déployer (le rendre accessible en
ligne). Première étape : créer un nouveau hostname pour faire des tests en
local. C'est à dire qu'on va devoir être capable d'accédér au site sur
[http://raspout/](http://raspout), mais uniquement depuis ta machine (quelques
infos [ici](http://lmgtfy.com/?q=debian+host)).

C'est maintenant parti pour configurer nginx !
[GLHF](http://nginx.org/en/docs/beginners_guide.html) !

## Iti

Pour le second site, c'est un peu différent... Le site n'est plus statique,
mais est généré avec un serveur (écrit en JavaScript). Nginx sera utilié alors
un peu différement : on parle ici de serveur *proxy* (il va rediriger toutes
les connexions vers l'autre serveur).

Le serveur du site est écrit en utilisant [NodeJS](https://nodejs.org/en/), qui
permet d'éxécuter du code JavaScript. Il est ainsi nécéssaire d'installer le
paquet `node`. De plus, il faut installer les dépendances du projet avec `npm
install` depuis le dossier `tuto-linux/web-server/iti`. Il est enfin possible
de lancer le serveur, avec la commande `PORT=4242 node index.js` à partir du
dossier du site. Si tout fonctionne correctement, le site doit être accessible
sur `http://localhost:4242/`.

Avoir une console ouverte pour que le site tourne en permanance, c'est pas
pratique. Heureusement, il existe une commande qui permet de lancer un
programme en tant que démon ! Hmmm...

Pour créer un nouveau démon (un nouveau service), il faut simplement créer un
script dans le dossier `/etc/init.d/nom_du_service`. Le fichier
`tuto-linux/web-server/iti/iti.service` peut être copié sous le nom `iti` pour
créer un service qui va lancer node pour nous (il faut aussi installer un petit
outil avec la commande `sudo npm install --save -g forever` pour que ça
marche). Il est maintenant possible de lancer le site en tâche de fond avec une
seule commande !

Dernière étape : ajouter le site iti dans la configuration de nginx, pour que
le site soit accessible sur `http://iti` en local (et donc ajouter le hostname
`iti`). Encore une fois, la doc est relativement claire sur la configuration
d'un *proxy server*.

## Déploiement en prod

Une fois que les deux sites sont fonctionnels en local, on peut les déployer en
production (les rendre accessible sur internet) ! Il suffit de changer les
hostnames en *iti.nilslayet.com* et *raspout.nilslayet.com*, et de m'envoyer un
sms pour me donner ton adresse IP (sans oublier d'ouvrir le port 80 sur ta
box).
