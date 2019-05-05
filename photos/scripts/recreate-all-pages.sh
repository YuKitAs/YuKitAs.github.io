#!/bin/bash

RESOURCES=(`ls ./resources`)

for name in ${RESOURCES[@]}
do
  if [ -e $name.html ]
   then cp $name.html $name.html.backup
  fi
  ./scripts/create-page.sh $name
done
