#!/bin/bash
REPO_URL="https://github.com/wersplat/rt25k-statbot.git"
git init
git remote add origin $REPO_URL
git add .
git commit -m 'init'
git branch -M main  # Added branch creation step
git push -u origin main