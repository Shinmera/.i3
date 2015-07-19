#!/bin/sh

function start {
    if ! pgrep "$1" &> /dev/null; then
        $1 &
    fi
}

## Base executables
nitrogen --restore
start clipit
start uim-toolbar-gtk3-systray

## X settings
xset s off
xset b off
fixwacom

if [ -f ~/.startuprc ]; then
    source ~/.startuprc
fi
