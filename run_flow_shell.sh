#!/bin/bash

echo "Start"


values=(1440 120 100 80 60 40 30 20 10)

for i in "${values[@]}"
do
	python3 generate_shell.py ./new_data/graph_near_petr/g${i}/flow_data/vertex.data ./new_data/graph_near_petr/g${i}/flow_data/run_flow_shell.sh ${i}
	cd ./new_data/graph_near_petr/g${i}/flow_data
	chmod +x run_flow_shell.sh
	echo "make run_flow_shell executable"
	./run_flow_shell.sh	
	cd ../../../../	
	echo ${i}
done
