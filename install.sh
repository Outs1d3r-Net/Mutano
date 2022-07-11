#!/bin/bash

p3=$(which python3)
pathmutano=$(pwd)

echo "Installing dependencies..."
$($p3 -m pip install -r requirements.txt)

echo "Create symbolic link..."
chmod a+x mutano.py
ln -s "$pathmutano/mutano.py" /usr/sbin/mutano

mutano
