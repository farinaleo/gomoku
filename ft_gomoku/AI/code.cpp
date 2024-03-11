#include <cstring>
#include <stdio.h>
#include <stdlib.h>

extern "C" {
    typedef struct s_point
    {
        int x;
        int y;
    }	t_point;

    int free_deg(const char *line, int x, int y, int opponent, int size) {
        int cnt = 0;
    
        int _up = y - 1;
        int _down = y + 1;
        int _left = x - 1;
        int _right = x + 1;
//        up left
        if (0 <= _left < size && 0 <= _up < size && line[_left + _up * size] != opponent)
            cnt = cnt + 1;
//        up mid
        if (0 <= x < size && 0 <= _up < size && line[x + _up * size] != opponent)
            cnt = cnt + 1;
//        up right
        if (0 <= _right < size && 0 <= _up < size && line[_right + _up * size] != opponent)
            cnt = cnt + 1;
//        mid left
        if (0 <= _left < size && 0 <= y < size && line[_left + y * size] != opponent)
            cnt = cnt + 1;
//        mid right
        if (0 <= _right < size && 0 <= y < size && line[_right + y * size] != opponent)
            cnt = cnt + 1;
//        down left
        if (0 <= _left < size && 0 <= _down < size && line[_left + _down * size] != opponent)
            cnt = cnt + 1;
//        down mid
        if (0 <= x < size && 0 <= _down < size && line[x + _down * size] != opponent)
            cnt = cnt + 1;
//        down right
        if (0 <= _right < size && 0 <= _down < size && line[_right + _down * size] != opponent)
            cnt = cnt + 1;
    
        return (cnt);
    }

    t_point* possible_mvt(const char *line, int size, int i, int end) {
        int s = 361;
        t_point *possible =  (t_point*)malloc(s * sizeof(t_point));;
        int pos_point = 0;

        while (i < end) {
            int x = i % size;
            int y = i / size;
            if (line[i] != '0'){
                int _up = y - 1;
                int _down = y + 1;
                int _left = x - 1;
                int _right = x + 1;
    //			up left
                if (0 <= _left < size && 0 <= _up < size && line[_left + _up * size] == '0'){
                    possible[pos_point].x = _left;
                    possible[pos_point].y = _up;
                    pos_point++;
                }
    //			up mid
                if (0 <= x < size && 0 <= _up < size && line[x + _up * size] == '0'){
                    possible[pos_point].x = x;
                    possible[pos_point].y = _up;
                    pos_point++;
                }
    //			up right
                if (0 <= _right < size && 0 <= _up < size && line[_right + _up * size] == '0'){
                    possible[pos_point].x = _right;
                    possible[pos_point].y = _up;
                    pos_point++;
                    }
    //			mid left
                if (0 <= _left < size && 0 <= y < size && line[_left + y * size] == '0'){
                    possible[pos_point].x = _left;
                    possible[pos_point].y = y;
                    pos_point++;
                }
    //			mid right
                if (0 <= _right < size && 0 <= y < size && line[_right + y * size] == '0'){
                    possible[pos_point].x = _right;
                    possible[pos_point].y = y;
                    pos_point++;
                }
    //			down left
                if (0 <= _left < size && 0 <= _down < size && line[_left + _down * size] == '0'){
                    possible[pos_point].x = _left;
                    possible[pos_point].y = _down;
                    pos_point++;
                }
    //			down mid
                if (0 <= x < size && 0 <= _down < size && line[x + _down * size] == '0'){
                    possible[pos_point].x = x;
                    possible[pos_point].y = _down;
                    pos_point++;
                }
    //			down right
                if (0 <= _right < size && 0 <= _down < size && line[_right + _down * size] == '0'){
                    possible[pos_point].x = _right;
                    possible[pos_point].y = _down;
                    pos_point++;
                }
            }
            i = i + 1;
        }
        while (pos_point < s) {
            possible[pos_point].x = -1;
            possible[pos_point].y = -1;
            pos_point++;
        }

        return possible;
    }

    void free_alloc(void * ptr) {
        if (ptr)
            free(ptr);
    }
}