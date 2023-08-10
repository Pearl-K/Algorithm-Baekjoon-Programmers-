#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int N, M;
int arr[1000001];

int main(void){
    cin >> N >> M;

    for(int i=1; i <= N; i++){
        cin >> arr[i];
    }

    ll start = 1, end = 1000000000001; //max 값(N*M)
    ll b;

    while (start < end){
        b = 0;
        ll mid = start + (end-start)/2;
        for (int i = 1; i <= N; i++){
            b += mid / arr[i];
        }
        if (b >= M) end = mid;
        else start = mid + 1;
    }

    cout << end << "\n";
    return 0;
}