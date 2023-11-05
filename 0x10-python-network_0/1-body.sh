#!/bin/bash
#Accepts URL, displays  a 200 response; Usage: ./1-body.sh 5B0.0.0.0:5000/route_1 ; echo ""
curl -Ls "$1"
