#!/bin/bash
#Accepts URL, sends DELETE request, display response body; Usage: ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
curl -s "$1" -X DELETE
