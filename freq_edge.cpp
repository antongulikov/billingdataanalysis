#include <bits/stdc++.h>

using namespace std;

map < pair <int, int> , int > edge_f;

void read_edges() {
	int from = 0;
	int to = 0;
	int cnt = 0;
	while (cin >> from >> to) {
		edge_f[{from, to}]++;				
	}	
}

void print_top_edges(int cnt) {	
	vector < pair <int, int> > values;
	int pos = 0;
	for (auto x : edge_f) {
		values.push_back({x.second, pos++});
	}
	sort(values.begin(), values.end());
	reverse(values.begin(), values.end());
	set < int > good;
	for (int i = 0; i < min((int)values.size(), cnt); i++) {
		good.insert(values[i].second);
	}
	vector < pair <int, pair < int, int> > > ret;
	pos = 0;
	for (auto x : edge_f) {
		if (good.find(x.second) != good.end()) {
			ret.push_back({x.second, x.first});
		}
	}
	sort(ret.begin(), ret.end());
	reverse(ret.begin(), ret.end());
	for (auto x : ret) {
		cout << x.second.first << " " << x.second.second << " " << x.first << "\n";
	}
}

string from_int_to_str(int x) {
	string ret = "";
	while (x) {
		ret.push_back(char(x % 10 + int('0')));
		x /= 10;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

int main(int argc, char **argv) {
	ios_base :: sync_with_stdio(false);
	cin.tie(0);
	int line_to_print = atoi(argv[2]);
	string in_file_name = string(argv[1]) + "/g.graph";
	string out_file_name = string(argv[1]) + "/top" + from_int_to_str(line_to_print) + ".data";	
	cerr << in_file_name << endl << out_file_name << endl;
	freopen(in_file_name.c_str(), "r", stdin);				
	freopen(out_file_name.c_str(), "w", stdout);
	read_edges();
	print_top_edges(line_to_print);
	return 0;
}