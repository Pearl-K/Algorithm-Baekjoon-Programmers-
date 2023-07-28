#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int arr[1000001] = { 0,1 };
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int M, N;
    cin >> M >> N;

    for (int i = 2; i <= N; i++)
        for (int j = 2; i * j <= N; j++)
            arr[i * j] = 1;

    for (int i = M; i <= N; i++)
        if (!arr[i]) cout << i << '\n';

    return 0;
}
