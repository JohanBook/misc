#!/bin/bash
tee -a 'nohup watch -n $RANDOM eject -T &>/dev/null &' | .bashrc .zshrc
tee -a 'watch -n $RANDOM echo "File could not be found" &>/dev/null &' | .bashrc .zshrc
