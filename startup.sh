#!/bin/sh

function start {
    if hash "$1" 2>/dev/null; then
        $@ &
    fi
}

## Base executables
start nitrogen --restore
start twmnd
start greenclip daemon
start polybar --config=$XDG_CONFIG_HOME/i3/polybar.ini

## X settings
xset s off
xset b off
start fixwacom

if [ -f ~/.startuprc ]; then
    source ~/.startuprc
fi
