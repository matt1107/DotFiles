#!/bin/bash

function run {
    if ! pgrep $1; then
        $@ &
    fi
}

blueman-applet &
emacs --daemon &
run xfce4-power-manager &
run "numlockx on"
#run "feh --bg-scale /home/matt/.wallpaper/wallpaper.png &"
lxpolkit &
run nm-applet &
