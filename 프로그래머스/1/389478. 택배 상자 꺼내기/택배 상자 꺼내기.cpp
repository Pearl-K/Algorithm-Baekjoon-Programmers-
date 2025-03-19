#include <string>
#include <vector>
#include <algorithm>
using namespace std;
using vi = vector<int>;
vi box;

int solution(int n, int w, int num) {
    int ret = 0;
    for(int i=1; i<2*w; i+=2) box.push_back(i);
    sort(box.rbegin(), box.rend());
    
    int floor = num/w - (num%w==0 ? 1 : 0);
    int nxt = num;
    while(nxt <= n){
        int add;
        add = nxt%w==0 ? w : nxt%w;
        nxt = nxt+box[add-1];
        ret++;
        floor++;
    }
    return ret;
}