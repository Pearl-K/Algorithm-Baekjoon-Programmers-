#include <iostream>
using namespace std;
int T;
string a, b;
string isSame(){
    for(int i = 0; i < a.size(); i++) if(a[i] != b[i]) return "ERROR";
    return "OK";
}
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> T;
    while(T--){
        cin >> a >> b;
        cout << isSame() << "\n";
    }
    return 0;
}