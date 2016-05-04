#!/bin/bash

echo "Start"


values=(1 2 3 5 10 20 30 60 1440)

inter=(10 20 50 100 150 200 250)

for i in "${values[@]}"
do
	for j in "${inter[@]}"
	do
		echo "${i} ${j}"
		./a.out ./g${i}/g${i} ./g${i} ${j}
	done	
done