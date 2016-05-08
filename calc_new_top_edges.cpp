#include <bits/stdc++.h>

using namespace std;

const int maxn = 1e6;

int vertex_number = 0;

int cnt_vertex[maxn];
map < pair < int, int > , int > cnt_edges;

struct edge {
	int u, v, cnt;
	edge(int u = 0, int v = 0, int cnt = 0): u(u), v(v), cnt(cnt){}
	bool operator < (const edge &other) const {
		return cnt < other.cnt;
	}
};

int main(int argc, char **argv){
	ios_base :: sync_with_stdio(false);
	cin.tie(0);
	int u, v, cnt;
	while (cin >> u >> v >> cnt) {
		vertex_number = max(vertex_number, u);
		vertex_number = max(vertex_number, v);
		if (u > v) {
			swap(u, v);
		}				
		cnt_edges[{v, u}] += cnt;
		cnt_vertex[u] += cnt;
		cnt_vertex[v] += cnt;
	}	
	vector < edge > edges;
	for (auto x : cnt_edges) {
		edges.push_back(edge(x.first.first, x.first.second, x.second));
	}
	sort(edges.begin(), edges.end());
	reverse(edges.begin(), edges.end());
	int threshold = atoi(argv[1]);
	for (int i = 0; i < min((int)edges.size(), threshold); i++) {
		edge tmp = edges[i];
		cout << tmp.u << " " << tmp.v << " " << tmp.cnt << endl;
	}
	return 0;
}