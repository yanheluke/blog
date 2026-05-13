#!/bin/bash
# Auto-rebuild when gallery/ or content/ changes
# Requires: brew install fswatch
# Usage: bash watch.sh

cd "$(dirname "$0")"

echo "Watching for changes... (Ctrl+C to stop)"
fswatch -o gallery/ content/ covers/ template.html css/ js/ | while read; do
  echo "$(date '+%H:%M:%S') Rebuilding..."
  python3 build.py 2>&1 | grep -v "MKL WARNING"
  echo "Done."
done
