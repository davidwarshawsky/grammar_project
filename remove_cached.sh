#!/bin/bash

gitignore=".gitignore"

while IFS= read -r line; do
  git rm --cached "$line"
done < "$gitignore"
