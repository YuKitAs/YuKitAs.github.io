#!/bin/bash

RESOURCES=(`ls ./resources`)

for name in ${RESOURCES[@]}
do
  ./scripts/create-page.sh $name
done
