#!/bin/sh
#source https://github.com/x70b1/polybar-scripts
#source https://github.com/polybar/polybar-scripts

#arch
#if ! updates_arch=$(checkupdates 2> /dev/null | wc -l ); then
    #updates_arch=0
#fi

#Dnf
if ! updates_arch=$(dnf check-update 2> /dev/null | wc -l ); then
    updates_arch=0
fi

if [ $updates_arch -gt 0 ]; then
    echo $updates_arch
else
    echo "0"
fi
