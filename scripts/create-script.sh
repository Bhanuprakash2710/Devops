
#Create a script that create an executable Script
#whose name is decided by the user 

#! /usr/bin/bash

echo "Enter the name of the script: "

read name

touch $name.sh

chmod +x $name.sh 
