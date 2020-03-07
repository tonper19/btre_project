#!/bin/bash
git show-branch -a \
| grep '\*' \
| grep -v `git rev-parse --abbrev-ref HEAD` \
| head -n1 \
| sed 's/[^\[]*//' \
| awk 'match($0, /\[[a-zA-Z0-9\/-]+\]/) { print substr( $0, RSTART+1, RLENGTH-2 )}'
