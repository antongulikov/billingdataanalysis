#!/bin/bash

echo "Start"


values=(10 20 30 40 60 80 100 120 1440)

for i in "${values[@]}"
do
	cd new_data/graph_near_petr/
	mkdir "g${i}"
	cd ../../
	python3 build_near_petr.py ./new_data/graph_near_petr/g${i}/g${i} ${i}
	echo $i
done

echo "Finish Build"

echo "Build top edges"

inter=(10 20 50 70 100 120 150 200 250)

for i in "${values[@]}"
do
	for j in "${inter[@]}"
	do
		echo "${i} ${j}"
		cd ./new_data/graph_near_petr/		
		./a.out ./g${i}/g${i} ./g${i} ${j}
		cd ../../
		python3 gen_top_html.py ./new_data/graph_near_petr/g${i}/g${i}.desc ./new_data/graph_near_petr/g${i}/top${j}.data 
	done	
done
