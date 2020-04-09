#!/bin/bash
# takes in a URL
curl -s "$1" | wc -c
