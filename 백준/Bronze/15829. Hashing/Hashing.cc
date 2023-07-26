#include <iostream>
#include <cstring>
using namespace std;

#include <iostream>
using namespace std;

int main() {
    long long M = 1234567891, ret = 0;
    int L;
    int asc = 0, r = 1;

    string str = "";
    cin >> L >> str;

    for (int i = 0; i < L; i++) {
        asc = str[i] - 96;
        ret += (asc * r) % M;
        r = (r * 31) % M;
    }
    cout << ret % M;
    return 0;
}