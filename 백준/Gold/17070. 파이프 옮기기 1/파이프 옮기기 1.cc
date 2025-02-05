#include <iostream>
using namespace std;
int N;
bool grid[16][16];
int ret[16][16][3];

void fillDp(){
	ret[0][1][0] = 1;
	for (int i=2; i<N; ++i){
        if (!grid[0][i]) ret[0][i][0] = ret[0][i-1][0];
    }
	for (int i=1; i<N; ++i){
		for (int j=2; j<N; ++j){
			if (!grid[i][j]){
				ret[i][j][0] = ret[i][j-1][0] + ret[i][j-1][1];
				ret[i][j][2] = ret[i-1][j][1] + ret[i-1][j][2];
				if (!grid[i-1][j] && !grid[i][j-1]){
                    ret[i][j][1] = ret[i-1][j-1][0] + ret[i-1][j-1][1] + ret[i-1][j-1][2];
                }
			}
		}
	}
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
	cin >> N;
	for (int i=0; i<N; ++i){
        for (int j=0; j<N; ++j) cin >> grid[i][j];
    }
	fillDp();
    int cnt = ret[N-1][N-1][0] + ret[N-1][N-1][1] + ret[N-1][N-1][2];
	cout << cnt << "\n";
    return 0;
}