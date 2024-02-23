#!/bin/bash

if [ "$2" == "-c" ]; then
    clear
fi

if [ -z "$1" ]; then
    echo "Usage: $0 <dossier>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: Path not found"
    exit 1
fi

for dir in "$1"/*; do
    if [ -d "$dir" ]; then
        if [[ "$dir" != *"__"* ]]; then
            echo "Run tests for : $dir"
            cd "$dir" || exit 1
            pytest
            cd - || exit 1
            echo ""
        fi
    fi
done
