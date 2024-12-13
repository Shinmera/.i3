#!/bin/sh

function start {
    if hash "$1" 2>/dev/null; then
        $1 "${@:2}" &
    fi
}

## Base executables
start nitrogen --restore
start greenclip daemon
start picom

polybar --list-monitors | while IFS=$'\n' read line; do
  monitor=$(echo $line | cut -d':' -f1)
  primary=$(echo $line | cut -d' ' -f3)
  MONITOR=$monitor polybar --config=$HOME/.config/i3/polybar.ini --reload "top${primary:+"-primary"}" &
done

## X settings
xset s off
xset b off

if [ -f ~/.startuprc ]; then
    source ~/.startuprc
fi
