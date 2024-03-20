#include <string>
#include <iostream>
#include "grid/grid.hpp"
#include "run_ai.h"

// Je suis ici, pour remplacer .extends() de Python, on peut utiliser insert de std::vector. Il fait la meme chose.
// Le seul hic c'est que il faudrait faire en sorte de pas creer des vecteurs a chaque fois qu'on appelle la fonction.
// Il faudrait generer les vecteurs seulement si on en a besoin.

//float matching_cases(char *line, Grid grid, int x, int y, char player, char opponent, int size, int line_size, int* lens, bool block) {
//    (void)line;
//    (void)grid;
//    (void)x;
//    (void)y;
//    (void)player;
//    (void)opponent;
//    (void)size;
//    (void)line_size;
//    (void)lens;
//    (void)block;
//
//    int default_lens[3] = {2, 3, 4};
//    int count = 0;
//    std::vector<std::vector<int>> goal;
//
//    if (!lens)
//        lens = default_lens;
//    for (int i = 0; i < 3; i++) {
//        if (lens[i] == 2) {
//            if (player == '2') {
//
//            }
//            else
//            {
//
//            }
//        }
//        else if (lens[i] == 3) {
//            if (player == '2') {
//
//            }
//            else
//            {
//
//            }
//        }
//        else if (lens[i] == 4) {
//            if (player == '2') {
//
//            }
//            else
//            {
//
//            }
//        }
//    }
//    return 0.0;
//}