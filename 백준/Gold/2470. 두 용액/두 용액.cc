#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const int INF = 2000000001;
int N;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    vector<int> ret(2);
    int s = 0, e = N-1;
    int arr[N];

    for(int i=0 ; i < N ; i++) cin >> arr[i];
    sort(arr, arr+N);

    int min = INF;
    while(s < e) {
        int tmp = arr[s]+arr[e];

        if (tmp == 0){
            ret[0] = arr[s];
            ret[1] = arr[e];
            break;
        }

        if(abs(tmp) < min) {
            ret[0] = arr[s];
            ret[1] = arr[e];
            min = abs(tmp);
        }

        if(tmp < 0) s++;
        else e--;
    }

    sort(ret.begin(), ret.end());
    cout << ret[0] << ' ' << ret[1];
    return 0;
}