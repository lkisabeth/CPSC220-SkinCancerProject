#!/bin/bash

for i in $(find images/* -type d); do
	echo $i $(ls $i | wc -l)
done
