#!/bin/bash

IPYNB_FILES=$(find . -name '*.ipynb' -not -path "./envs/*" -not -path "./.ipynb_checkpoints/*")
for f in $IPYNB_FILES
do
    echo "Removing $f..."
    rm -f "$f"
done