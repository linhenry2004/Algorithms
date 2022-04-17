#include <iostream>
#include <vector>
using namespace std;

int maximalNetworkRank (int n, vector<vector<int>> roads) {
    vector <int> deg(n);
    vector<vector<int>> edges(n, vector<int>(n));
    for (int i = 0; i < roads.size(); i++) {
        int x = roads[i][0];
        int y = roads[i][1];
        deg[x]++;
        deg[y]++;
        edges[x][y]++;
        edges[y][x]++;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            ans = max(deg[i] + deg[j] - edges[i][j], ans);
        }
    }
    return ans;
}

int main () {
    int n;
    cin >> n;
    vector <vector<int>> roads(n);
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        roads[a].push_back(b);
        roads[b].push_back(a);
    }

    cout << maximalNetworkRank(n, roads) << endl;

    return 0;
}