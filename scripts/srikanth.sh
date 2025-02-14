#! /usr/bin/bash

read -p "enter a number between 1-5: " num

if [ $num == "1" ] ; then 

  echo "Entered 1 "
  
elif [ $num == "2" ]; then

  echo "Entered 2 "
  
elif [ $num == "3" ]; then

  echo "Entered 3 "
  
elif [ $num == "4" ]; then

  echo "Entered 4 "
  
elif [ $num == "5" ]; then

  echo "Entered 5 "
  
else

  echo "None of the above" 
  
fi

echo "bye"
  

