#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using vi = vector<int>;

string N;
int K;
queue<string> q;

void swapChar(string &str, int a, int b) {
	char tmp = str[a];
	str[a] = str[b];
	str[b] = tmp;
	return;
}

int main(){
	cin.tie(0)->sync_with_stdio(0);
	cin >> N >> K;
	q.push(N);

	for(int i=0; i<K; ++i){
		set<string> strSet;
		int qLen = q.size();

		for(int j=0; j<qLen; ++j){
			string nowState = q.front();
			q.pop();

			if(strSet.count(nowState)) continue;
			strSet.insert(nowState);

			int stLen = nowState.size();
			for(int k=0; k<stLen-1; ++k){
				for(int r=k+1; r<stLen; ++r){
					if(!(k == 0 && nowState[r] == '0')){
						swapChar(nowState, k, r);
						q.push(nowState);
						swapChar(nowState, k, r);
					}
				}
			}
		}
	}

	string ret ="-1";
	while(!q.empty()){
		ret = max(ret, q.front());
		q.pop();
	}
	cout << ret << "\n";
	return 0;
}