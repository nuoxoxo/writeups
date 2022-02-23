#!/bin/bash

echo 'utf-8 -> utf-16LE :'
iconv -f UTF-8 -t UTF-16LE enc

echo '\n\nutf-8 -> utf-16BE :'
iconv -f UTF-8 -t UTF-16BE enc 
