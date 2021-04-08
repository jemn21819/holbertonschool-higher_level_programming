#!/bin/bash
# sends a request to a URL passed as an argument displays only status response
curl -so /dev/null -w "%{http_code}" "$1"
