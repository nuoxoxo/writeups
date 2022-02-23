#!/bin/bash

alias cmd='grep -i flag | sed "s/^.*flag: //" | sed "s/ .*$//" '
url='https://jupiter.challenges.picoctf.org/problem/41511'

curl -s ${url}/index.html | cmd
curl -s ${url}/mycss.css | cmd
curl -s ${url}/myjs.js | cmd
