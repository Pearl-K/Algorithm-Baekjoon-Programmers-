#include <iostream>
#include <string>
using namespace std;

string S;
int retMin = 1e9;
int retMax = 0;

int oddCnt(string str){
    int cnt = 0;

    for(char s : str){
        int tmp = s - '0';
        if (tmp%2 != 0) cnt++;
    }
    return cnt;
}

pair<int, int> dfs(string str, int cnt){

    int sLen = str.length();
    cnt += oddCnt(str);

    if(sLen == 1){
        retMin = retMax = cnt;
        return {retMin, retMax};
    } else if (sLen == 2){
        int tmp = 0;
        for(char s : str) tmp += s-'0';
        return dfs(to_string(tmp), cnt);
    } else {
        for(int i = 0; i < sLen-2; i++){
            for(int j = i+1; j < sLen-1; j++){

                string s1 = str.substr(0,i+1); // 0 ~ i
                string s2 = str.substr(i+1,j-i); //i+1 ~ j
                string s3 = str.substr(j+1); // j ~ str.length
                string sum = to_string(stoi(s1) + stoi(s2) + stoi(s3));

                pair<int,int> val = dfs(sum,cnt);

                retMin = min(retMin,val.first);
                retMax = max(retMax,val.second);
            }
        }

        return {retMin,retMax};
    }
}

int main(void) {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    cin >> S;
    pair<int, int> ret = dfs(S, 0);
    cout << ret.first << " " << ret.second;

    return 0;
}