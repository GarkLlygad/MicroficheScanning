#!/bin/bash
cd /home/gark/MicroficheScanning/
if [[ -z $(git status -s) ]]; then
  echo "No changes to commit."
  exit 0
fi
git add .
git commit -m "RaspberryPi auto update $(date +'%Y-%m-%d %H:%M:%S')"
git push -u origin master
