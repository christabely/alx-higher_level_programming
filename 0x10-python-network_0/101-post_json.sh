#!/bin/bash
# Script sends JSON POST request to a URL, displays body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
