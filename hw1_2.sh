#!/bin/bash
mkdir -p test2
i=1
while(($i<=100))
do
	
	filename="DDM"$i""
	mkdir test2/$filename
	touch test2/$filename/time_until_now.txt
	t=$(date +%s%N)
	echo "nanoseconds since 1970-01-01 00:00:00 UTC:" $t >>test2/$filename/time_until_now.txt
	#touch $path/$filename/makefile
	let i++
done
