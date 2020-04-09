#!/bin/bash
# takes in a URL 
# sends a GET reques 
# displays the body response
curl -s $1 -H "X-HolbertonSchool-User-Id: 98"
