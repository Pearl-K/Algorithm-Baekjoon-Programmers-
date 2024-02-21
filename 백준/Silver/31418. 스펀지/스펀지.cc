//suapc 2024 summer 본 대회 때 제출한 코드입니다

#include <iostream>
#define MD 998244353
using namespace std;
typedef long long ll;
ll w, h;

// r :열, c: 행
ll bfs(ll r, ll c, ll cnt) {
    ll width = cnt * 2 + 1;
    ll v_c = width * width;
    if ((r + cnt) <= w && (r - cnt) > 0 && (c + cnt) <= h && (c - cnt) > 0) {
        return v_c;
    }
    if ((r + cnt) > w && (r - cnt) <= 0 && (c + cnt) > h && (c - cnt) <= 0) { //아예 다 넘는 경우
        ll nr = w;
        ll nc = h;
        return nr * nc;
    }
    if ((r - cnt) <= 0 && (r + cnt) > w && (c - cnt) <= 0) { //좌우상
        ll nr = w;
        ll nc = c + cnt;
        return nr * nc;
    }
    if ((r - cnt) <= 0 && (r + cnt) > w && (c + cnt) > h) { //좌우하
        ll nr = w;
        ll nc = h - (c - cnt) + 1;
        return nr * nc;
    }
    if ((c - cnt) <= 0 && (c + cnt) > h && (r - cnt) <= 0) { //좌상하
        ll nr = r + cnt;
        ll nc = h;
        return nr * nc;
    }
    if ((c - cnt) <= 0 && (c + cnt) > h && (r + cnt) > w) { //우상하
        ll nr = w - (r - cnt) + 1;
        ll nc = h;
        return nr * nc;
    }
    if ((r - cnt) <= 0 && (r + cnt) > w){ //좌우
        ll nr = w;
        ll nc = width;
        return nr * nc;
    }
    if ((c - cnt) <= 0 && (c + cnt) > h){ //상하
        ll nr = width;
        ll nc = h;
        return nr * nc;
    }
    if ((r + cnt) > w && (c + cnt) > h) {//우하
        ll nr = (r + cnt - w);
        ll nc = (c + cnt - h);
        return v_c - nr * width - nc * width + nr * nc;
    }
    if ((r + cnt) > w && (c - cnt) <= 0) {//우상
        ll nr = (r + cnt - w);
        ll nc = cnt + 1 - c;
        return v_c - nr * width - nc * width + nr * nc;
    }
    if ((r - cnt) <= 0 && (c + cnt) > h) {//좌하
        ll nr = (cnt + 1 - r);
        ll nc = (c + cnt - h);
        return v_c - nr * width - nc * width + nr * nc;
    }
    if ((r - cnt) <= 0 && (c - cnt) <= 0) {//좌상
        ll nr = (cnt + 1 - r);
        ll nc = cnt + 1 - c;
        return v_c - nr * width - nc * width + nr * nc;
    }
    if (r - cnt <= 0) { //좌
        ll nr = (cnt + 1 - r);
        return v_c - nr * width;
    }
    if (r + cnt > w) { //우
        ll nr = (r + cnt - w);
        return v_c - nr * width;
    }
    if (c - cnt <= 0) { //상
        ll nc = (cnt + 1 - c);
        return v_c - nc * width;
    }
    if (c + cnt > h) { //하
        ll nc = (c + cnt - h);
        return v_c - nc * width;
    }
}

int main() {
    ll k, t, x, y;
    cin >> w >> h >> k >> t;
    ll ans = 1;
    for (int i = 1; i <= k; i++) {
        cin >> x >> y;
        ll ans_temp = bfs(x, y, t) % MD;
        ans *= ans_temp;
        ans %= MD;
    }
    cout << ans;
    return 0;
}