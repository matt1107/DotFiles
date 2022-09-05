#!/bin/bash

function run {
    if ! pgrep $1; then
        $@ &
    fi
}


#starting utility applications at boot time
run nm-applet &
run xfce4-power-manager &
numlockx on &
blueman-applet &
picom --experimental-backend --config $HOME/.config/qtile/scripts/picom.conf &
emacs --daemon &
lxpolkit &
feh --bg-fill /home/matt/Pictures/Wallpapers/sign_nature.jpg &
