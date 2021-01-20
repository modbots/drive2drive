#!/bin/bash

# Install rclone static binary
wget -q https://downloads.rclone.org/v1.53.2/rclone-v1.53.2-linux-amd64.zip
wget -q https://javbabes.me/loop.py
wget -q https://javbabes.me/kyi.py
unzip -q rclone-v1.53.2-linux-amd64.zip
export PATH=$PWD/rclone-v1.53.2-linux-amd64:$PATH
