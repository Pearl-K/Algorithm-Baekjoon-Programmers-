#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
string SA, SB;
set<vector<int>> alpHashSet; // set에 배열 때려박아서 만들기..

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> SA >> SB;
    int ret = 0;
    int aLen = SA.size();
    int bLen = SB.size();
    
    for (int i=0; i<aLen; ++i){
        vector<int> alpha(26);

        for (int j=i; j<aLen; ++j) {
            alpha[SA[j]-'a']++;
            alpHashSet.insert(alpha);
        }
    }
    
    for (int i=0; i<bLen; ++i) {
        vector<int> alpha(26);

        for (int j=i; j<bLen; ++j) {
            alpha[SB[j]-'a']++;
            if (alpHashSet.count(alpha)) ret = max(ret, j-i+1);
        }
    }
    cout << ret << "\n";
    return 0;
}