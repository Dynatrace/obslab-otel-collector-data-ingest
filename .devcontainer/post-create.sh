#!/bin/bash

# Install
kind create cluster --config .devcontainer/kind-cluster.yml --wait 300s

# Creation Ping
# tenant is not available at startup
# hence missing tenant key below
curl -X POST https://grzxx1q7wd.execute-api.us-east-1.amazonaws.com/default/codespace-tracker \
  -H "Content-Type: application/json" \
  -d "{
    \"repo\": \"$GITHUB_REPOSITORY\",
    \"demo\": \"obslab-otel-collector-data-ingest\",
    \"codespace.name\": \"$CODESPACE_NAME\"
  }"
