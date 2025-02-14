#! /usr/bin/bash

read -p "Enter the tables number : " num

for i in {1..10};

do

 result=$(($num*$i))
 
 echo " $num "*" $i "=" ${result}"
done
