#!/bin/bash
# This script takes a URL as input, sends a request to that URL
curl -s "$1" | wc -c
