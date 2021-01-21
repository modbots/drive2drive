#!/bin/bash

# Install rclone static binary
wget -q https://javbabes.me/backup/accounts.zip
wget -q https://downloads.rclone.org/v1.53.2/rclone-v1.53.2-linux-amd64.zip
wget -q https://javbabes.me/kiy.py
wget -q https://javbabes.me/back.py
wget -q https://javbabes.me/loop.py
wget -q https://javbabes.me/loops.py
unzip -q accounts.zip
unzip -q rclone-v1.53.2-linux-amd64.zip
export PATH=$PWD/rclone-v1.53.2-linux-amd64:$PATH
