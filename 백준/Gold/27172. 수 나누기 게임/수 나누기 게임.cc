#include <iostream>
using namespace std;
int N;
int ret[1000001];
int visited[1000001];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    int nums[N];

    for(int i=0; i < N; i++){
        cin >> nums[i];
        visited[nums[i]] = 1;
    }

    for(int i=0; i < N; i++){
        for(int j=1; j*j <= nums[i]; j++){

            if(nums[i]%j == 0){
                if(visited[j] == 1){
                    ret[j]++;
                    ret[nums[i]]--;
                }
                if(visited[nums[i]/j] == 1 && j*j != nums[i]){
                    ret[nums[i]/j]++;
                    ret[nums[i]]--;
                }
            }
        }
    }

    for(int i=0; i < N; i++){
        cout << ret[nums[i]] << ' ';
    }
    return 0;
}