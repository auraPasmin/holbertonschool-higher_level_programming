#!/bin/bash
# displays all HTTP methods 
# the server will accept.
curl -sI -X OPTIONS "$1" | grep -i Allow | cut --complement -d ' ' -f 1 
