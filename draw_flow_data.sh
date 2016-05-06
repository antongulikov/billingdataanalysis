#!/bin/bash

values=(10 20 30 40 60 80 100 120 1440)

for val in "${values[@]}"
do
	python3 summarize_flow_data.py ${val}
	python3 gen_top_html.py ./new_data/graph_near_petr/g${val}/g${val}.desc ./new_data/graph_near_petr/g${val}/flow_data/top_edges.data
	echo ${val}
done