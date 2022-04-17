#include <iostream>
#include <set>
#include <vector>
using namespace std;

#define max 100001

int findCenter (vector <pair<int, int>> edges) {
    vector <int> deg(max);
    int count = edges.size();
    int x, y;
    set <int> s;
    for (int i = 0; i < count; i++) {
        x = edges[i].first;
        y = edges[i].second;
        s.insert(x);
        s.insert(y);
        deg[x]++;
        deg[y]++;
    }
    for (int i = 1; i < count; i++) {
        if (deg[i] == (int)s.size() - 1) {
            return i;
        }
    }
    return 0;
}

int main () {
    int n;
    cin >> n;
    vector <pair<int, int>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first >> a[i].second;
    }
    
    int ans = 0;
    ans = findCenter(a);
    if (ans != 0) {
        cout << ans << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}