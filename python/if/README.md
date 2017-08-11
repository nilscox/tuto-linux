# If

Petite série d'exercices sur les conditions...

## isPositive

Ecrire la fonction `isPositive` dont le but est de trouver le signe d'un entier.
Si l'entier est positif ou negatif, la fonction doit retourner `vrai` ou `faux` respectivement,
mais s'il est nul, alors la elle ne doit rien retourner.

Prototype: `isPositive(int) -> bool`

## isOdd

Ecrire la fonction `isOdd`, retournant `vrai` uniquement si le nombre donné en
paramètre est impair ou `faux` sinon.

Prototype: `isOdd(int) -> bool`

## isVowel

Ecrire la fonction `isVowel`, retournant `vrai` uniquement si la lettre passée
en paramêtre est une voyelle ou `faux` sinon.

Prototype: `isVowel(char) -> bool`

## max2

Ecrire la fonction `max2` calculant le maximum entre deux entiers.

Prototype: `max2(int, int) -> int`

## max3

Ecrire la fonction `max3` calculant le maximum entre trois entiers.

Prototype: `max(int, int, int) -> int`

## med

Ecrire la fonction `med` cherchant l'entier médian entre trois entiers
distincts.

Prototype: `med(int, int, int) -> int`

## daysInMonth

Ecrire la fonction `daysInMonth` retournant le nombre de jours dans un mois.
On concidère que l'année n'est pas bissextile. Le paramêtre passé à la fonction
est le numéro du mois (janvier étant le mois 1)

Prototype: `daysInMonth(int) -> int`

## areValidTriangleAngles

Ecrire la fonction `areValidTriangleAngles` retournant vrai si la valeur des trois
angles du triangle passées en paramêtres permettent de former un triangle.

Prototype: `areValidTriangleAngles(int, int, int) -> bool`

## areValidTriangleSides

Ecrire la fonction `areValidTriangleSides` retournant vrai si la valeur des trois
angles du triangle passées en paramêtres permettent de former un triangle

Prototype: `areValidTriangleSides(int, int, int) -> bool`

## solveQuadratic

Ecrire la fonction `solveQuadratic` calculant les racines d'un polynôme du
second degré.
Cette fonction prend en paramêtres les coefficients de l'équation. Par exemple,
avec une équation du type `a*x² + b*x + c`, les paramêtres seront `a`, `b` et
`c`.
Elle doit retourner un couple d'entiers en cas de racines doubles, un entier si
les racines sont simples, sinon elle ne retourne rien.

Prototype: `solveQuadratic(int, int, int) -> (int, int) | int | None`

## isSorted

Ecrire la fonction `isSorted`, retournant `vrai` uniquement si la liste passée
en paramêtre est triée par ordre croissant ou décroissant, `faux` sinon.

Prototype: `isSorted(list) -> bool`
