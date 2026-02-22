#!/usr/bin/env bash
set -euo pipefail
curl -sS -X POST http://localhost:9090/-/reload
echo