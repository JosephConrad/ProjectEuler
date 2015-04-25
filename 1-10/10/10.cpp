#include <algorithm>
#include <stdio.h>

using namespace std;

typedef long long int ll;

const ll N_MAX = 1000000; 
ll pierwsza[N_MAX+1]; 
ll prime_sum[N_MAX+1]; 

typedef long long int ll;
 
void sito(ll n) { 
    for (ll i = 1; i <= n; ++i) pierwsza[i] = true; 
    pierwsza[1] = false; 
    for (ll i = 2; i*i <= n; ++i) { 
        if (pierwsza[i]) { 
            for (ll j = 2*i; j <= n; j += i) { 
                pierwsza[j] = false; 
            } 
        } 
    } 
}

int main() {
    int T;
    scanf("%d", &T);
    sito(N_MAX);
    for (int i = 1; i < N_MAX; ++i) {
        if (pierwsza[i])
            prime_sum[i] = prime_sum[i-1] + i;
        else
            prime_sum[i] = prime_sum[i-1];
    }
    
    for (int i = 0; i < T; ++i) {
        int border;
        ll sum = 0;
        scanf("%d", &border);
        printf("%lld\n", prime_sum[border]);
    }
}
