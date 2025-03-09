#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
using ll = long long;

int N;
int arr[1001];
int curMax = 0;
ll ret = 0;

void dvCnq(int st, int ed, int cur) {
	if (st == ed) return;
	int nowMax = *max_element(arr+st, arr+ed);
	int maxIdx = find(arr+st, arr+ed, nowMax) - arr;
	if (st <= maxIdx-1) dvCnq(st, maxIdx, nowMax);
	if (maxIdx+1 < ed) dvCnq(maxIdx+1, ed, nowMax);
	ret += cur - nowMax;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N;
	for (int i = 0; i < N; i++) {
        cin >> arr[i];
		curMax = max(curMax, arr[i]);
	}
	dvCnq(0, N, curMax);
    cout << ret << "\n";
}