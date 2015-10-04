#!/bin/sh

function start {
    if hash "$1" 2>/dev/null;; then
        $1 &
    fi
}

## Base executables
nitrogen --restore
start clipit
start uim-toolbar-gtk3-systray
start twmnd

## X settings
xset s off
xset b off
start fixwacom

if [ -f ~/.startuprc ]; then
    source ~/.startuprc
fi
