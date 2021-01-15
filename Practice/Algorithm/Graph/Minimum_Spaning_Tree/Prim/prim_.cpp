#include <queue>
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int visited[10001];
vector<pair<int, int>> edges[10001];
typedef pair<int, int> pii;

void prim(int start) {
    visited[start] = true;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    for (int i=0; i<edges[start].size(); i++) {
        int adj = edges[start][i].first;
        int weight = edges[start][i].second;
        pq.push(pii(weight, adj));
    }
    int ans = 0;
    while (!pq.empty())
    {
        int cur = pq.top().second;
        int weight = pq.top().first;
        pq.pop();
        if (visited[cur]) {
            continue;
        }
        visited[cur] = true;
        ans += weight;
        for (int i=0; i<edges[cur].size(); i++) {
            int adj = 
        }
    }
    

}

int main() {
    int v,e;
    scanf("%d %d", &v, &e);
    for (int i=0; i<e; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        edges[a].push_back(pii(b, c));
        edges[b].push_back(pii(a, c));
    }
}