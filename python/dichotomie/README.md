# Dichotomie

## Principe

Le but de la dichotomie est de trouver l'index d'un élément dans une liste
triée, et de manière optimisée (mieux qu'une simple boucle for).

L'algorithme est simle : la fonction de recherche dichotomique prend deux
paramètres : une liste triée composée d'élements comparables, et un élément. On
récupère l'élément situé au milieu de la liste (`len(list) / 2`), et on le
compare avec l'élément recherché. Si l'élément de la liste est inférieur à
l'élément recherché, on recommence avec la première moitié de la liste, de même
avec la seconde moitié si l'élément est supérieur. Dans le cas ou les éléments
sont égaux, bin... on l'a trouvé.

## Prototype

```
dichotomie(list, elem) -> int
```