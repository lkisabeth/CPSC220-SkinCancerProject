#!/bin/bash

for category in $(find images/* -type d); do
	if [ $(ls $category | wc -l) -lt 1000 ]; then
		for image in $(ls $category); do
			convert $category/$image -flop $category/flipped_$image
			convert $category/$image -flip $category/flopped_$image
			convert $category/$image -flip -flop $category/flipped_and_flopped_$image
		done
	fi
done
