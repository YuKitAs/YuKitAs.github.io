#!/bin/bash

cp "manifest.json" "manifest.json.backup"

for filename in ../*.html
do cp "$filename" "$filename.backup"
done
