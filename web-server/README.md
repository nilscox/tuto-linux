# Web server

Un *serveur web* est programme, qui tourne en continue sur une machine (souvent
un serveur, ça sert à ça), et qui attend des connexions internet (sur le port
80 par défaut).

Lorsqu'un utilisateur se connect à un site web, son navigateur va établir une
connexion avec le serveur (qui était alors en attente). Une fois la connexion
établie, le navigateur va pouvoir dialoguer avec le serveur pour afficher le
site correctement.

Le but de l'exo est d'*installer* un serveur web sur une machine debian, de
*configurer* ce serveur, et de *déployer* deux sites. Le code du premier site
est fourni dans le dossier `tuto-linux/web-server/iti`. Pour le second site en
revanche, je te fais confiance...

## Nginx

*Nginx* est un serveur web. Il est utilisé le plus souvent en tant que *démon*
(daemon en anglais), et est appelé un `service` sous linux.  Un démon est un
programme qui tourne en tâche de fond, et pour le contrôler (start, stop,
restart...) on passe par la commande `service` (sous debian, et `systemctl`
sous archlinux par exemple).

Comme déjà annoncé, le but de l'exo est d'installer et de configurer nginx pour
gérer deux sites. [La documentation](http://nginx.org/en/docs/) est assez bien
faite, et il y a toujours [stackov'](http://stackoverflow.com/) en cas de
pépin...).

A toi de jouer, commence par installer et lancer nginx. Nous reviendrons sur la
config plus tard... Si le serveur est bien lancée, un message doit s'afficher
sur [http://localhost/](http://localhost/).

## Raspout

Nous avons maintenant un serveur qui tourne, mais pas encore de site.
Commençons par écrire le site `raspout`. Le code HTML / CSS (/ JS ?) doit être
présent dans le dossier `tuto-linux/web-server/raspout`, et le fichier d'entrée
doit s'appeler `index.html`. une page HTML simple et un peu de CSS feront
l'affaire... :^).

Une fois que le site est terminé, il faut le déployer ! Première étape, il faut
créer un nouveau hostname pour faire des tests en local. C'est à dire qu'on va
pouvoir accédér au site sur [http://raspout/](http://raspout) ([quelques liens
ici](http://lmgtfy.com/?q=debian+host)).

C'est maintenant parti pour configurer nginx ! (GLHF
!)[http://nginx.org/en/docs/beginners_guide.html]

## Iti

Ah pour `iti`, c'est un peu différent... Le site n'est pas *static* comme pour
`raspout`, mais *dynamique* ; c'est à dire que le code est généré
automatiquement (à l'aide de JavaScript). Nginx sera utilié alors un peu
différement : on parle ici de serveur *proxy* (il va rediriger toutes les
connexions vers un autre serveur).

Il est donc ici nécéssaire de lancer le serveur du site `iti`. Pour utiliser ce
serveur, il est nécéssaire d'installer le paquet `node`. Il se lance avec la
commande : `PORT=4242 node index.js` à partir du dossier
`tuto-linux/web-server/iti`. Si le serveur est lancé correctement, le site doit
être accessible sur `http://localhost:4242/`.

Avoir une console ouverte pour que le site tourne en permanance, c'est pas
pratique. Heureusement, il existe une commande qui permet de lancer un
programme en tant que démon ! ... Comment ? Tu la connais ? Pour créer un
nouveau démon (un nouveau service), il faut simplement créer un script dans le
dossier `/etc/init.d/nom_du_service`. Le fichier
`tuto-linux/web-server/iti/iti.service` peut être copié avec le nom `iti` pour
créer un service qui va lancer node pour nous.

Nous pouvons maintenant lancer le site en tâche de fond avec une seule commande
(laquelle ? hum...). Dernière étape : ajouter le site iti dans la configuration
de nginx, pour que le site soit accessible sur `http://iti` en local (et donc
ajouter le hostname `iti`, comme pour `raspout`). Encore une fois, la doc est
relativement claire sur la configuration d'un *proxy server*.
