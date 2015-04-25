#include <stdio.h>
#include <algorithm>

using namespace std;

const int N_MAX = 16;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        int h;
        scanf("%d", &h);
        int entry;
        int tab[2][N_MAX];
        scanf("%d", &entry);
        tab[0][0] = entry;
        for (int i = 1; i < h; ++i) {
            for (int j = 0; j <= i; ++j) {
                scanf("%d", &entry);
                if (j > 0 && j <= i - 1) {
                    tab[1][j] = max(tab[0][j] + entry, tab[0][j-1] + entry);
                }
                else if (j == 0) {
                    tab[1][j] = tab[0][j] + entry;
                }
                else {
                    tab[1][j] = tab[0][j-1] + entry;
                }
            }
            for (int j = 0; j <= i; ++j) {
                    tab[0][j] = tab[1][j];
            }
        }
        int maks = 0;
        for (int i = 0; i < h; ++i) maks = max(maks, tab[0][i]);
        printf("%d\n", maks);
    }
    return 0;
}
