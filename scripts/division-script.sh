#! /usr/bin/bash

divisible()
{
	num=$1
	
	for i in {2,3,5}
	
	do
		if [ $(( $num%$i)) -eq 0 ]; then
			echo " $num is divisible by $i "
	
		fi 
	done
}

divisible 33
	
	
