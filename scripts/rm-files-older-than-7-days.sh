#! /usr/bin/bash

directory="/home/bhanuprakashgireddy/Desktop/scripts"

days=1

find "$directory" -type f -mtime +$days -exec rm -f {} \;

echo "files older than $days day are removed  "
