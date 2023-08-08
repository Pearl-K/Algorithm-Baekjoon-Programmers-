#include <iostream>
using namespace std;

int main() {
    int L, P, V;
    int i = 1;
    while (1){
		cin >> L >> P >> V;
		if (L == 0 && P == 0 && V == 0)
			break;
        
        int ret = (V / P) * L + min(V % P, L);
		cout << "Case " << i << ": " << ret << "\n";
        i++;
    }
	return 0;
}