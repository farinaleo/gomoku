# gomoku

---

## Grid structure

We represent the game bord as following:
\begin{math}1 =x + y\end{math}

| \ | 0 | 1 | 2 |
|---|---|---|---|
| 0 | x |   |   |
| 1 |   | o |   |
| 2 |   |   |   |

---

## Algorithm

We chose to implement the alpha beta pruning version of MinMax.
MinMax is a two players game algorithm who generate a possibilities tree.

---

## Clustering

To reduce expansions possibility we chose to limit the searching area with rules:

#### Only alignment for opponent :

#### Alignment for AI :

#### Square for AI :

---

## Heuristic

Thanks to the subject we are free to create and implement our own heuristic function.
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

---

## How to start your AI correctly

_These tips are based on our personal progress and do not guarantee you an easy journey.
Nevertheless, we think they would have been very useful for us to better understand the
subject and be more efficient._

 