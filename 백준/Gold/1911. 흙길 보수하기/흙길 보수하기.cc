#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using pii = pair<int, int>;
using vi = vector<int>;
int N, L;
vector<pii> range;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> L;
    for(int i=0; i<N; ++i){
        int a, b;
        cin >> a >> b;
        range.push_back({a,b});
    }

    sort(range.begin(), range.end());
    int rangeEnd = 0;
    int retCnt = 0;

    for(int i=0; i<N; ++i){
        int st = range[i].first;
        int ed = range[i].second;

        if (rangeEnd >= ed) continue;
        int uncovered = max(rangeEnd, st);
        int cover = ed - uncovered;
        int nowL = (cover+L-1)/L;
        retCnt += nowL;
        rangeEnd = uncovered + nowL*L; 
    }
    cout << retCnt << "\n";
    return 0;
}