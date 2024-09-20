#include <iostream>
#include <set>
#include <map>
using namespace std;

set<pair<int, int>> LvP;
map<int, int> plist;
int N, M;

int main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    cin >> N;
    for(int i=0; i<N; ++i){
        int p, l;
        cin >> p >> l;
        LvP.insert(make_pair(l, p));
        plist[p] = l;
    }

    cin >> M;

    for(int i=0; i<M; ++i){
        string o;
        cin >> o;

        if(o == "add"){
            int p, l;
            cin >> p >> l;

            LvP.insert(make_pair(l, p));
            plist[p] = l;
        }
        else if(o == "recommend"){
            int x;
            cin >> x;

            if(x == 1){
                cout << (*prev(LvP.end())).second << "\n";
            }
            else{
                cout << (*LvP.begin()).second << "\n";
            }
        }
        else{
            int p;
            cin >> p;
            LvP.erase(make_pair(plist[p], p));
            plist.erase(p);
        }
    }
    return 0;
}