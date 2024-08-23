#!/bin/bash

# Startup Ping
curl -X POST https://grzxx1q7wd.execute-api.us-east-1.amazonaws.com/default/codespace-tracker \
  -H "Content-Type: application/json" \
  -d "{
    \"type\": \"com.dynatrace.devrel.handson.codespace.started\",
    \"repo\": \"$GITHUB_REPOSITORY\",
    \"demo\": \"obslab-otel-collector-data-ingest\",
    \"codespace.name\": \"$CODESPACE_NAME\"
  }"