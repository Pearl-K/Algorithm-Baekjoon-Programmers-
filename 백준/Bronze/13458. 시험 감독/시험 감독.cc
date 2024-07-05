#include<iostream>
using namespace std;
using ll = long long;

int N, B, C;
int arr[1000001];

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    ll cnt = N;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    cin >> B >> C;

    for (int i=0; i < N; i++){
        arr[i] -= B;
        if (arr[i] <= 0) continue;
        cnt += int(arr[i]/C);
        if (arr[i]%C) cnt++;
    }
    cout << cnt;
}