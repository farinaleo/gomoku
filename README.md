# gomoku
***
## Algorithm
We chose to implement the alpha beta pruning version of MinMax.
MinMax is a two players game algorithm who generate a possibilities tree.
***
## Clustering
To reduce expansions possibility we chose to limit the searching area with rules:

#### Only alignment for opponent :

#### Alignment for AI :

#### Square for AI :

***
## Heuristic
Thanks to the subject we are free to create and implement our own heuristic function. \
We based it according the following concepts / checks :

#### Winning :

#### Capture stones :

#### Potential captures :

#### Move freedom :

#### Alignment to victory :

#### Alignment freedom :

#### Combinations :

#### Blocking opponent combinations :

#### Opponent last move :

#### Opponent patterns :

***