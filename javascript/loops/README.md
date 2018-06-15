# Loops

Petite série d'exercices sur les boucles...

## intersect

Ecrire la fonction `intersect`, dont le but est de trouver les valeurs
existantes dans deux tableaux.

Prototype: `intersection(arr1: Array<Number>, arr2: Array<Number>) -> Array<Number>`

Exemple:
```
const a = [5, 2, 8, 4, 3, 7];
const b = [9, 4, 1, 5, 6];

intersection(a, b);
// [5, 4];
```

> Note: l'ordre des éléments dans le tableau résultant n'importe pas.

## excldisj

Ecrire la fonction `excldisj`, dont le but est de trouver les valuers
existantes dans l'un des deux tableaux, mais pas dans les deux.

Prototype: `excldisj(arr1: Array<Number>, arr2: Array<Number>) -> Array<Number>`

Exemple:
```
const a = [5, 2, 8, 4, 3, 7];
const b = [9, 4, 1, 5, 6];

excldisj(a, b);
// [2, 8, 3, 7, 9, 1, 6];
```
