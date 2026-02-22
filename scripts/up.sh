#!/usr/bin/env bash
set -euo pipefail

mkdir -p data/prometheus data/loki

# Prometheus container writes as UID 65534
sudo chown -R 65534:65534 data/prometheus

docker compose up -d --build
docker ps