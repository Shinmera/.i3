#!/bin/sh

function start {
    if hash "$1" 2>/dev/null; then
        $@ &
    fi
}

## Base executables
start nitrogen --restore
start greenclip daemon
start polybar --config=$HOME/.config/i3/polybar.ini

## X settings
xset s off
xset b off

if [ -f ~/.startuprc ]; then
    source ~/.startuprc
fi
