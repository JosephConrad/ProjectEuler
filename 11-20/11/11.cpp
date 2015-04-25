#include <algorithm>
#include <stdio.h>

using namespace std;

const int N_MAX = 20;

int tab[N_MAX][N_MAX];

int right(int i, int j) {
    if ((j+4) > N_MAX) return -1;
    int product = 1;
    for (int k = j; k < j + 4; k++) 
        product *= tab[i][k];
    return product;
}

int down(int i, int j) {
    if ((i+4) > N_MAX) return -1;
    int product = 1;
    for (int k = i; k < i + 4; k++) 
        product *= tab[k][j];
    return product;
}

int diag(int i, int j) {
    if ((i+4) > N_MAX) return -1;
    if ((j+4) > N_MAX) return -1;
    int product = 1;
    for (int k = 0; k < 4; k++) 
        product *= tab[i+k][j+k];
    return product;
}

int diag_left(int i, int j) {
    if ((i+4) > N_MAX) return -1;
    if ((j-4) > N_MAX) return -1;
    int product = 1;
    for (int k = 0; k < 4; k++) 
        product *= tab[i+k][j-k];
    return product;
}

int main() {
    int maks = 0;
    for (int i = 0; i < N_MAX; i++) {
        for (int j = 0; j < N_MAX; j++) {
            int temp;
            scanf("%d", &temp);
            tab[i][j] = temp;
        }
    }
    for (int i = 0; i < N_MAX; i++) {
        for (int j = 0; j < N_MAX; j++) { 
            maks = max(maks, right(i, j));
            maks = max(maks, down(i, j));
            maks = max(maks, diag(i, j));
            maks = max(maks, diag_left(i, j));
        }
    }
    printf("%d\n", maks);

}
