#!/bin/bash

values=(10 20 30 40 60 80 100 120 1440)

for i in "${values[@]}"
do
	python3 mcl_cluster.py ./new_data/graph_near_petr/g${i}/flow_data/top_vertex_200.data ./new_data/graph_near_petr/g${i}/flow_data/new_edges_desc.data ./new_data/graph_near_petr/g${i}/flow_data/html_result/clustering200.html
	python3 mcl_cluster.py ./new_data/graph_near_petr/g${i}/flow_data/top_vertex_100.data ./new_data/graph_near_petr/g${i}/flow_data/new_edges_desc.data ./new_data/graph_near_petr/g${i}/flow_data/html_result/clustering100.html
done