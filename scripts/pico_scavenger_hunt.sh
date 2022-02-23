#!/bin/bash

alias cmd='grep -i part | sed "s/^.*: //" | sed "s/ .*$//" '
url='http://mercury.picoctf.net:55079'

curl -s ${url} | cmd
curl -s ${url}/mycss.css | cmd
curl -s ${url}/robots.txt | cmd
curl -s ${url}/.htaccess | cmd
curl -s ${url}/.DS_Store | cmd
