#include <iostream>
using namespace std;
bool vst[51] = {false, };

int dfs(string S, int idx){
    int cnt = 0;

    for (int i=0; i < S.size(); i++){
        if(S[i] == '(' && !vst[i]){
            vst[i] = true;
            int now = S[i-1] - '0'; //'0'의 아스키코드를 빼주어 쉽게 정수로 변환
            cnt--; //이전 문자의 cnt를 제거하여 보정해주는 역할
            cnt += now * dfs(S, i+1);
        } else if (S[i] == ')' && !vst[i]){
            vst[i] = true;
            return cnt;
        } else if (!vst[i]){
            vst[i] = true;
            cnt++;
        }
    }
    return cnt;
}

int main(void){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    string S;
    cin >> S;
    cout << dfs(S, 0) << "\n";

    return 0;
}