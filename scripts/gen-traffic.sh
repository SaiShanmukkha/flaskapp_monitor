#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://localhost:8080/}"
N="${2:-200}"

for i in $(seq 1 "$N"); do
  curl -s "$URL" >/dev/null || true
done

echo "Sent $N requests to $URL"