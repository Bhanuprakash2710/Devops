#!/usr/bin/bash


for i in 1 2 3 4; do
    touch "${i}.txt"
done

for i in 1 2 3; do
    touch "${i}-image.png"
done

echo "Files are being created..."
sleep 1


ls -l
echo ""


choice=""


while [[ "$choice" != "t" && "$choice" != "j" ]]; do
    read -p "Enter 'j' to edit jpg files or 't' to edit txt files: " choice
    echo "You have chosen: $choice"
done


read -p "Enter a prefix: " prefix
echo "You entered prefix: $prefix"


if [ "$choice" = "t" ]; then
    for i in *.txt; do
        echo "Txt files are: ${i}"
        mv "$i" "${prefix}${i}"
    done
else
    for i in *.png; do
        echo "Png files are: ${i}"
        mv "$i" "${prefix}${i}"
    done
fi

