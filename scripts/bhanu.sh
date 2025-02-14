# Create a Script that does the following:

#Create  2 .txt files: "1.txt" "2.txt"
#Inside 1.txt write the content of your pwd. in the long list format
#Ask the user what prefix he wants to give to the file "1.txt"
#Change the name of "1.txt" adding to it the prefix choosen by the user

#! /usr/bin/bash

touch 1.txt 2.txt

ls -l>>1.txt

echo "enter the prefix name of the file: "

read name

mv 1.txt $name.txt
