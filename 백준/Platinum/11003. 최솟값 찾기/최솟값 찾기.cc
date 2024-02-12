#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, L;
    cin >> N >> L;

    vector<int> A;
    deque<pair<int, int>> Q;

    for (int i = 0; i < N; i++) {
        if (!Q.empty() && Q.front().second < i-L+1) { //idx 비교
            Q.pop_front();
        }
        int now;
        cin >> now;
        
        while (!Q.empty() && Q.back().first > now) { //값 비교
            Q.pop_back();
        }
        Q.push_back(make_pair(now, i));
        A.push_back(Q.front().first);
    }
    for (int i = 0; i < N; i++) {
        cout << A[i] << " ";
    }
    return 0;
}