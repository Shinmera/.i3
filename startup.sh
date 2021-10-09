#!/bin/sh

function start {
    if hash "$1" 2>/dev/null; then
        $@ &
    fi
}

## Base executables
start nitrogen --restore
start uim-toolbar-gtk3-systray
start twmnd
start greenclip daemon

## X settings
xset s off
xset b off
start fixwacom

if [ -f ~/.startuprc ]; then
    source ~/.startuprc
fi
