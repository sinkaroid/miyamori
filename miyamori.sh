#!/bin/bash
#sin

RED=$(tput setaf 1) 
GREEN=$(tput setaf 2) 

echo -e "${RED}
   _____  .__                                    .__ 
  /     \ |__|___.__._____    _____   ___________|__|
 /  \ /  \|  <   |  |\__  \  /     \ /  _ \_  __ \  |
/    Y    \  |\___  | / __ \|  Y Y  (  <_> )  | \/  |
\____|__  /__|/ ____|(____  /__|_|  /\____/|__|  |__|
        \/    \/          \/      \/                 "
echo "(IndoXXI,LK21,Gudangmovie) Movie scraper with python"
echo -e "${GREEN}"
PS3='select your platform or "4" to exit: '
options=("lk21" "gudangmovie" "search instead" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "lk21")
            cd bin;python 21.py
            ;;
        "gudangmovie")
            cd bin;python gu.py
            ;;
        "search instead")
            cd bin;python query.py
            ;;
       
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done