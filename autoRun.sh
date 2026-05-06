#!/bin/bash
git fetch
git status
git commit -am "Bash test automation $(date +'%Y-%m-%d %H:%M:%S')"
git push
