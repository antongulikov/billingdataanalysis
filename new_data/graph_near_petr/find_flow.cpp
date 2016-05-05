#include <bits/stdc++.h>

using namespace std;

string from_int_to_str(int x) {
    string ret = "";
    while (x) {
        ret.push_back(char(x % 10 + int('0')));
        x /= 10;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

map < pair <int, int> , int > edges_positions;

int N = 0;

/**
 * f - flow
 * c - capacity
 * v - from
 * u - to
 * id - edge id
 * inv - reverse edge id
 */

const int maxn = (int)3e6 + 10;

int ptr[maxn], used[maxn], level[maxn];
int count_iteration = 0;
vector < int > g[maxn];
vector < int > d[maxn];

struct edge {
    int v, u, f, c, id, inv;
    edge(int v = 0, int u = 0, int f = 0, int c = 0, int id = 0, int inv = 0) :
            v(v), u(u), f(f), c(c), id(id), inv(inv)
    {
        edges_positions[{v, u}] = id;
        d[v].push_back(u);
    }

    bool operator < (const edge &other) const {
        return f < other.f;
    }
};

vector < edge > edges;


void add_edge(int from, int to) {
    if (!edges_positions.count({from, to})) {
        int size_edge = (int)edges.size();
        edges.push_back(edge{from, to, 0, 1, size_edge, size_edge + 1});
        edges.push_back(edge{to, from, 0, 0, size_edge + 1, size_edge});
        g[from].push_back(size_edge);
        g[to].push_back(size_edge + 1);
    } else {
        int pos = edges_positions[{from, to}];
        edges[pos].c++;
    }
}

void read_graph() {
    int u = 0;
    int v = 0;
    while (cin >> v >> u) {
        add_edge(v, u);
        N = max(N, v);
        N = max(N, u);
    }
    N += 10;
}

void dfs(int v) {
    used[v] = 1;
    for (auto x : d[v]) {
        if (used[x] == 0) {
            dfs(x);
        }
    }
}

bool is_connected(int v, int u) {
    for (int i = 0; i < N; i++)
        used[i] = 0;
    dfs(v);
    return used[u];
}

bool find_new_path(int flow, int begin, int end) {
    count_iteration++;
    queue < int > q;
    used[begin] = count_iteration;
    level[begin] = 0;
    q.push(begin);
    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (auto edge_id : g[v]) {
            int to = edges[edge_id].u;
            if (used[to] != count_iteration && edges[edge_id].c - edges[edge_id].f >= flow) {
                used[to] = count_iteration;
                level[to] = level[v] + 1;
                q.push(to);
            }
        }
    }
    return used[end] == count_iteration;
}

bool push_flow(int v, int flow, int begin, int end) {
    if (v == end) {
        return 1;
    }
    used[v] = count_iteration;

    for (; ptr[v] < int(g[v].size()); ptr[v]++) {
        int edge_id = g[v][ptr[v]];
        edge& current_edge = edges[edge_id];
        if (level[v] + 1 == level[current_edge.u] && current_edge.c - current_edge.f >= flow &&
                push_flow(current_edge.u, flow, begin, end)) {
            current_edge.f += flow;
            edges[current_edge.inv].f -= flow;
            return 1;
        }
    }
    return 0;
}

void make_flow(int begin, int end) {
    int ans = 0;
    /*for (auto val : edges) {
        if (val.v == begin) {
            cerr << val.c << endl;
        }
    }*/
    cerr << is_connected(begin, end) << " " << begin << " " << end << endl;
    for (int flow = (1 << 30); flow > 0; flow >>= 1) {
        while (find_new_path(flow, begin, end)) {
            for (int i = 0; i < N; i++)
                ptr[i] = 0;
            count_iteration++;
            while (push_flow(begin, flow, begin, end)) {
                ans += flow;
                count_iteration++;
            }
        }
    }
    cerr << "Flow is " << ans << endl;
    cout << ans << endl;
}

void print_top_edges(int cnt) {    
    sort(edges.begin(), edges.end());
    reverse(edges.begin(), edges.end());
    for (int i = 0; i < min(cnt, (int)edges.size()); i++) {
        if (edges[i].f == 0)
            continue;
        cout << edges[i].v << " " << edges[i].u << " " << edges[i].f << " " << edges[i].c << " " << (double)edges[i].f / (double)edges[i].c << endl;
    }    
}

int main(int argc, char **argv) {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int s_flow = atoi(argv[3]);
    int f_flow = atoi(argv[4]);
    int line_to_print = 100;
    string in_file_name = string(argv[1]) + ".graph";
    string out_file_name = string(argv[2]) + "/flow_data/top_flow_" + from_int_to_str(s_flow) + "_" + from_int_to_str(f_flow) + ".data";
    cerr << in_file_name << endl << out_file_name << endl;
    freopen(in_file_name.c_str(), "r", stdin);
    freopen(out_file_name.c_str(), "w", stdout);
    read_graph();
    make_flow(s_flow, f_flow);
    print_top_edges(line_to_print);
    return 0;
}