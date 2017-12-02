# Rot13

Cet exercice a pour but de travailler la lecture et l'écriture dans un fichier,
par le biais d'un algorithme de chiffrement très simple : la rotation de 13
caractères. Une rotation de n caractères dans un texte consiste à remplacer
chaque lettre par la nème suivante dans l'alphabet. L'avantage si l'on prend
`n = 13`, est que `text == rot13(rot13(text))` (c'est à dire que l'algorithme de
chiffrement est le même que celui de déchiffrement).

## Fonction de chiffrement

Pour commencer, il serait préférable de créer une fonction qui ne s'occupe que
d'effectuer une rotation de 13 caractères dans l'alphabet. Cette fonction
prendra le texte à chiffrer en paramêtre, et retournera le text chiffré (ben
voyon...).

Sa signature est :

```
rot13(str) -> str
```

Les caractères minuscules doivent rester minuscules (de même pour les
majuscules). Tous les autres caractères (chiffres, caractères spéciaux, lettres
accentuées...) ne doivent pas subir de rotation.

Hint : il serait peut-être intéressant de créer une fonction qui s'occupe de
faire la rotation d'un unique caractère, puis de l'appeler sur tous les
caractères du texte...

## Arguments passés au script

Le script doit s'appeler `rot13.py`, et doit contenir une fonction `main`,
appelée uniquement si le script est lancé en ligne de commande
(`if __name__ == "__main__"`). Le script reçevra un unique argument : le nom
du fichier à chiffrer.

S'il manque l'argument ou si plusieurs arguments sont passés au script, une
erreur doit être affichée (`usage: rot13.py <filename>`) et le script doit
s'arrêter avec le code de retour `1`.

Si le chemin donné en argument n'est pas un fichier, une erreur doit être
affichée, et le script doit s'arrêter avec le code de retour `1`.

## Gestion des fichiers

Le script devra avoir une gestion des noms de fichiers intelligente. En
admettant que le fichier existe :

- si le nom du fichier d'entrée ne se termine pas par `.rot13`, alors le fichier
  de sortie devra avoir le même nom que le fichier d'entrée suffixé par
  `.rot13`.
- si le nom du fichier d'entrée se termine par `.rot13`, alors le fichier de
  sortie devra avoir le même nom que le fichier d'entrée sans le `.rot13`
  final.

Avant d'écrire le résultat du chiffrement dans le fichier de sortie, si un
fichier (ou un dossier, un lien...) porte déjà le nom du fichier de sortie,
alors le script demandera à l'utilisateur s'il veut l'écraser. Si oui, alors
le fichier existant sera remplacé par le nouveau fichier, si non alors le script
devra se terminer avec le code de retour `1`.

## Exemple

```
42sh$ ls
rot13.py  toto.txt
42sh$ cat toto.txt
J'aime les vaches
J'4IM3 L3$ V4CH3$
42sh$ ./rot13.py
usage: ./rot13.py <filename>
42sh$ echo $?
1
42sh$ ./rot13.py toto.txt
42sh$ echo $?
0
42sh$ ls
rot13.py  toto.txt  toto.txt.rot13
42sh$ cat toto.txt.rot13
W'nvzr yrf inpurf
W'4VZ3 Y3$ I4PU3$
42sh$ mv toto.txt.rot13 tata.txt.rot13
42sh$ ./rot13 tata.txt.rot13
42sh$ ls
rot13.py  tata.txt  tata.txt.rot13  toto.txt  toto.txt.rot13
42sh$ cat tata.txt
J'aime les vaches
J'4IM3 L3$ V4CH3$
```

## Hints

Fonctions utilisées :

- `print`
- `input`
- `sys.exit`
- `open`
- `ord`
- `chr`
- `file.read`
- `file.write`
- `os.path.isfile`
- `string.isalpha`
- `string.isupper`
- `string.endswith`

Fonctions écrites :

- `rot13(str) -> str`
- `read_file(str) -> str`
- `write_file(str, text) -> str`
- `get_output_filename(str) -> str`
- `check_overwrite(str) -> Bool`
- `usage() -> None`
- `main() -> None`
