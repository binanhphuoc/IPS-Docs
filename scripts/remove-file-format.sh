#!/bin/bash

FILE_FORMAT="ipynb"

while getopts ":f:" opt; do
  case ${opt} in
    f )
        FILE_FORMAT=$OPTARG
      ;;
    \? ) 
        echo "Usage:"
        echo "  Opt       Default Argument    Description"
        echo "  [-f]      ipynb               file format"
        echo "  [-h]      NONE                help"
        exit 0
      ;;
    : )
        echo "Invalid Option: -$OPTARG requires an argument" 1>&2
        exit 1
        ;;
  esac
done
shift $((OPTIND -1))

IPYNB_FILES=$(find . -name "*.${FILE_FORMAT}" -not -path "./envs/*" -not -path "./.ipynb_checkpoints/*")
for f in $IPYNB_FILES
do
    echo "Removing $f..."
    rm -f "$f"
done